# !/usr/bin/env python3
# coding:utf-8
import discord
import os
import asyncio
import configparser
from discord.ext import commands
from cogs import *
import logging
from aiohttp import ClientSession
from src.config import _dt_token, _do_token

logger = logging.getLogger("apex-stats")
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='apex-stats.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class ApexStats(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='a!', activity=discord.Game(name='Updating...'),
                        status=discord.Status('dnd'))
        self.remove_command("help")
        self._load_extensions()

    def _load_extensions(self):
        for file in os.listdir("cogs/"):
            try:
                if file.endswith(".py"):
                    self.load_extension(f'cogs.{file[:-3]}')
                    logger.info(f"{file} loaded")
            except:
                logger.exception(f"Fail to load {file}")

    async def on_ready(self):
        await self.wait_until_ready() # waiting internal cache to be ready
        logger.info(f"Logged in as {self.user}")
        while True:
            await self.change_presence(
                                activity=discord.Activity(
                                        name=f'[a!help] | {len(self.guilds)} servers',
                                        type=3)
                            )
            await asyncio.sleep(60*3)

    def run(self, *args, **kwargs):
        try:
            self.loop.run_until_complete(self.start(_dt_token()))
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
        except discord.LoginFailure:
            logger.critical("Invalid token")
        except Exception:
            logger.critical("Fatal exception", exc_info=True)

if __name__ == "__main__":
    bot = ApexStats()
    bot.run()