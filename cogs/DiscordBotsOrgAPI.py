import dbl
from discord.ext import commands

import asyncio
import logging


class DiscordBotsOrgAPI(commands.Cog):
    """Handles interactions with the discordbots.org API"""

    def __init__(self, bot):
        self.bot = bot
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjU1MTQ0NjQ5MTg4NjEyNTA1OSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTY5MjU2NjUyfQ.QOv2Anb7ykWxyI09QYArSZFmFb1wVsHFJMjjfHRl-vA" # set this to your DBL token
        self.dblpy = dbl.Client(self.bot, self.token)
        self.updating = self.bot.loop.create_task(self.update_stats())

    async def update_stats(self):
        """This function runs every 30 minutes to automatically update your server count"""
        while not self.bot.is_closed():
            logger.info('Attempting to post server count')
            try:
                await self.dblpy.post_guild_count()
                logger.info('Posted server count ({})'.format(self.dblpy.guild_count()))
            except Exception as e:
                logger.exception('Failed to post server count\n{}: {}'.format(type(e).__name__, e))
            await asyncio.sleep(1800)

def setup(bot):
    global logger
    logger = logging.getLogger('apex-stats')
    bot.add_cog(DiscordBotsOrgAPI(bot))