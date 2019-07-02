#!/usr/bin/env python3
#coding:utf-8

import discord
from discord.ext import commands

stats_commands = """**`a!stats`** - Explanation about stats
**`a!stats <username>`** - View Apex Legends statistics on PC only (shorter version)
**`a!stats <username> <pc | xbox | psn>`** - View Apex Legends statistics
**`a!profile`** - View your Apex Legends profile if registered before
**`a!profile save <username> <pc | xbox | psn>`** - Link your Discord account to your Apex Legends stats
**`a!profile display`** - View the current saved profile
**`a!profile unlink`** - Unlink your profile
**`a!leaderboard`** - Top 10 from database"""

apex_commands = """**`a!news`** - View 6 last news on Apex Legends
**`a!servers`** - View all Apex Legends server status (ping, status, server name)
**`a!map`** - View Apex Legends map and his tier loot
**`a!reddit <hot | top>`** - Recents post by categorie
**`a!drop`** - Random place to land for the next game
**`a!legend`** - Random legend to pick for the next game
**`a!team`** - Entire random team for the next game
**`a!patch`** - View live patch note
**`a!ranked`** - View info about how ranked works"""

other_commands = """**`a!bug <message>`** - Send me a bug report, this will helps to improve the bot
**`a!suggestion <message>`** - Suggestion to add for the bot, all suggestions are good don't hesitate
**`a!ping`** - View bot latency
**`a!about`** - Bot info
**`a!donate`** - Link to support me
**`a!vote`** - An other way to support me
**`a!support`** - Discord support if you need help or want to discuss with me
**`a!invite`** - returns bot link invite"""

class Help(commands.Cog):
    """Help commands"""
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def help(self,ctx):
        embed = discord.Embed(title='**Available commands:**',
                            colour=self.colour,
                            description="Required argument : <>\n[Commands website](https://apexstatistics.gitbook.io/)")
        embed.add_field(name="Stats commands:",value=stats_commands)
        embed.add_field(name="Apex Commands:",value=apex_commands)
        embed.add_field(name="Other commands:",value=other_commands)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)

        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Added Help")
