#!/usr/bin/env python3
#coding:utf-8

import discord
from discord.ext import commands

stats_commands = """**`a!stats <username> <platform>`** - returns apex stats
**`a!profile save <username> <platform>`** - link your discord account to your apex stats
**`a!profile display`** - returns your current saved profile
**`a!profile unlink`** - unlink your profile
**`a!leaderboard`** (soon)"""

apex_commands = """**`a!news`** - returns 6 last apex legends news
**`a!servers`** - returns apex legends status server
**`a!reddit <hot/top>`** - returns reddit recents post by categorie
**`a!drop`** - returns a random place to land
**`a!legend`** - returns random legend to pick for the next game
**`a!team`** - returns a random team for Apex Legends"""

other_commands = """**`a!ping`** - retuns bot latency
**`a!about`** - returns bot info
**`a!donate`** - returns link to support me
**`a!vote`** - returns link to vote
**`a!support`** - returns discord support
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
                            description="[Commands website](https://apexstatistics.gitbook.io/workspace/)",
                            icon_url=ctx.guild.me.avatar_url)
        embed.add_field(name="Stats commands:",value=stats_commands)
        embed.add_field(name="Apex Commands:",value=apex_commands)
        embed.add_field(name="Other commands:",value=other_commands)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)

        await ctx.author.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
    print("Added Help cog from cogs")
