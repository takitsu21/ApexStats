# !/usr/bin/env python3
# coding:utf-8
import discord
import os
import asyncio
from discord.ext import commands
import logging
from src.config import _d_token
from discord.utils import find
import datetime
import time


logger = logging.getLogger("apex-stats")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='apex-stats.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


class ApexStats(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=commands.when_mentioned_or('a!'),
            activity=discord.Game(name='Updating...'),
            status=discord.Status('dnd')
            )
        self.remove_command("help")
        self._load_extensions()
        self.colour = 0xff0004

    async def on_guild_join(self, guild):
        general = find(lambda x: x.name == "general", guild.text_channels)
        if general and general.permissions_for(guild.me).send_messages:
            embed = discord.Embed(
                    title="Nice to meet you!",
                    description="Below are the infos about Apex Stats",
                    timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                    color=self.colour
                )
            embed.set_thumbnail(url=guild.me.avatar_url)
            embed.add_field(name="Vote",
                            value="[Click here](https://discordbots.org/bot/551446491886125059/vote)")
            embed.add_field(name="Invite Apex Stats",
                            value="[Click here](https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=1543825472)")
            embed.add_field(name="Discord Support",
                            value="[Click here](https://discordapp.com/invite/wTxbQYb)")
            embed.add_field(name="Donate",value="[Click here](https://www.patreon.com/takitsu)")
            embed.add_field(name = "Source code and commands", value="[Click here](https://github.com/takitsu21/ApexStats)")
            embed.add_field(name="Help command",value="a!help")
            nb_users = 0
            for s in self.guilds:
                nb_users += len(s.members)

            embed.add_field(name="Servers", value=len(self.guilds))
            embed.add_field(name="Members", value=nb_users)
            embed.add_field(name="**Creator**", value="Taki#0853")
            embed.add_field(name="*Contributor*", value="RedstonedLife#0001")
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=guild.me.avatar_url)
            await general.send(embed=embed)

    def _load_extensions(self):
        for file in os.listdir("cogs/"):
            try:
                if file.endswith(".py"):
                    self.load_extension(f'cogs.{file[:-3]}')
                    logger.info(f"{file} loaded")
            except Exception:
                logger.exception(f"Fail to load {file}")

    def _unload_extensions(self):
        for file in os.listdir("cogs/"):
            try:
                if file.endswith(".py"):
                    self.unload_extension(f'cogs.{file[:-3]}')
                    logger.info(f"{file} unloaded")
            except Exception:
                logger.exception(f"Fail to unload {file}")

    async def on_ready(self):
        await self.wait_until_ready() # waiting internal cache to be ready
        logger.info(f"Logged in as {self.user}")
        while True:
            await self.change_presence(
                            activity=discord.Activity(
                                    name=f'[a!help] | {len(self.guilds)} servers',
                                    type=discord.ActivityType.watching
                                    ),
                            status=discord.Status.online
                            )
            await asyncio.sleep(60)

    def run(self, *args, **kwargs):
        try:
            self.loop.run_until_complete(self.start(_d_token(debug=True)))
        except KeyboardInterrupt:
            self.loop.run_until_complete(self.logout())
            for task in asyncio.all_tasks(self.loop):
                task.cancel()
            try:
                self.loop.run_until_complete(
                    asyncio.gather(*asyncio.all_tasks(self.loop))
                )
            except asyncio.CancelledError:
                logger.debug("Pending tasks has been cancelled.")
            finally:
                logger.error("Shutting down")

if __name__ == "__main__":
    bot = ApexStats()
    bot.run()