# !/usr/bin/env python3
# coding:utf-8

import discord
from discord.ext import commands
import asyncio
import datetime as dt
import time as t
from src.decorators import trigger_typing
import logging

logger = logging.getLogger("apex-stats")

class Help(commands.Cog):
    """Help commands"""
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    def embed_pagination(self, ctx):
        embed = discord.Embed(title="Help hub",
                            description="[Vote here](https://top.gg/bot/551446491886125059) to support me if you ❤️ the bot\n"
                            "[Source code and commands](https://takitsu21.github.io/ApexStats/)\n"
                            "`[RequiredArgument] <ParameterToChoose>`",
                            color=self.colour)
        embed.add_field(name='📊 Stats', value="View commands to get Apex Legends statistics.")
        embed.add_field(name='<:a_:632338231349739521> Apex Legends', value="View commands about Apex")
        embed.add_field(name='📃 News', value="View commands about Apex news")
        embed.add_field(name=u"\u2699 About Apex Stats", value="View commands about the bot")
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        return embed    

    @commands.command(aliases=["h"])
    @commands.bot_has_permissions(manage_messages=True, add_reactions=True)
    @trigger_typing
    async def help(self, ctx):
        await ctx.message.delete()
        stats_commands = """**`<a!stats | a!s>`** - Explanation about stats\n
        **`<a!stats | a!s> [USERNAME] <pc | xbox | psn>`** - View Apex Legends statistics -> Example `a!s nicehat_taki pc`\n
        **`<a!stats | a!s> [USERNAME]`** - View Apex Legends statistics for PC only (shortcut) -> Example `a!s nicehat_taki\n
        **`<a!profile | a!p>`** - View your Apex Legends profile if registered before\n
        **`<a!profile | a!p> save [USERNAME] <pc | xbox | psn>`** - Link your Discord account to your Apex Legends stats -> Example `a!p save nicehat_taki pc`\n
        **`<a!profile | a!p> display`** - View the current saved profile\n
        **`<a!profile | a!p> unlink`** - Unlink your profile\n
        **`a!history [USERNAME] <pc | xbox | psn>`** - View player's recent matches"""
        apex_commands = """**`a!drop`** - Random place to land for the next game (outdated for now)\n
        **`a!map`** - Apex Legends season 3 map with it's tier loot\n
        **`a!legend`** - Random legend to pick for the next game\n
        **`a!team`** - Entire random team for the next game\n
        **`a!weapons`** - List all weapon commands to get their informations"""
        news_command = """**`a!servers`** - View all Apex Legends server status (ping, status, server name)\n
        **`a!reddit <hot | top>`** - Recents post by categorie\n
        **`a!patch`** - View live patch note\n
        **`a!news`** - View last 6 news on EA website\n
        **`a!ranked`** - View info about how ranked works (updated)"""
        other_commands = """**`a!bug [MESSAGE]`** - Send me a bug report, this will helps to improve the bot\n
        **`a!suggestion [MESSAGE]`** - Suggestion to add for the bot, all suggestions are good don't hesitate\n
        **`a!ping`** - View bot latency\n
        **`a!about`** - Bot info\n
        **`a!donate`** - Link to support me\n
        **`a!vote`** - An other way to support me\n
        **`a!support`** - Discord support if you need help or want to discuss with me\n
        **`a!invite`** - returns bot link invite\n
        **`<a!help | a!h>`** - returns bot's commands"""

        toReact = ['⏪', '📊', '<:a_:632338231349739521>', '📃', u"\u2699"]
        # emojis = await ctx.guild.fetch_emojis()
        embed = self.embed_pagination(ctx)
        pagination = await ctx.send(embed=embed)
        while True:
            for reaction in toReact:
                await pagination.add_reaction(reaction)
            def check(reaction, user):
                return user == ctx.message.author and str(reaction.emoji) in toReact
            try:
                reaction, user = await self.bot.wait_for('reaction_add', check=check, timeout=180.0)
            except asyncio.TimeoutError:
                return await pagination.delete()
            if '⏪' in str(reaction.emoji):
                embed = self.embed_pagination(ctx)
            elif '📊' in str(reaction.emoji):
                embed = discord.Embed(title="📊 Stats",
                                    description=stats_commands,
                                    color=self.colour)
            elif '<:a_:632338231349739521>' in str(reaction.emoji):
                embed = discord.Embed(title="<:a_:632338231349739521> Apex",
                                    description=apex_commands,
                                    color=self.colour)
            elif '📃' in str(reaction.emoji):
                embed = discord.Embed(title="📃 News",
                                    description=news_command,
                                    color=self.colour)
                
                await pagination.edit(embed=embed)
            elif u"\u2699" in str(reaction.emoji):
                embed = discord.Embed(title=u"\u2699 Bot",
                                    description=other_commands,
                                    color=self.colour)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=ctx.guild.me.avatar_url)
            await pagination.edit(embed=embed)

    @help.error
    async def old_help(self, ctx, error):
        logger.error(error)
        stats_commands = """**`<a!stats | a!s>`** - Explanation about stats
        **`<a!stats | a!s> [USERNAME] <pc | xbox | psn>`** - View Apex Legends statistics -> Example `a!s nicehat_taki pc`
        **`<a!profile | a!p>`** - View your Apex Legends profile if registered before
        **`<a!profile | a!p> save [USERNAME] <pc | xbox | psn>`** - Link your Discord account to your Apex Legends stats -> Example `a!p save nicehat_taki pc`
        **`<a!profile | a!p> display`** - View the current saved profile
        **`<a!profile | a!p> unlink`** - Unlink your profile
        **`a!history [USERNAME] <pc | xbox | psn>`** - View player's recent matches"""
        apex_commands = """**`a!drop`** - Random place to land for the next game (outdated for now)
        **`a!map`** - Apex Legends season 3 map with it's tier loot
        **`a!legend`** - Random legend to pick for the next game
        **`a!team`** - Entire random team for the next game
        **`a!weapons`** - List all weapon commands to get their informations"""
        news_command = """**`a!servers`** - View all Apex Legends server status (ping, status, server name)
        **`a!reddit <hot | top>`** - Recents post by categorie
        **`a!patch`** - View live patch note
        **`a!news`** - View last 6 news on EA website
        **`a!ranked`** - View info about how ranked works (updated)"""
        other_commands = """**`a!bug [MESSAGE]`** - Send me a bug report, this will helps to improve the bot
        **`a!suggestion [MESSAGE]`** - Suggestion to add for the bot, all suggestions are good don't hesitate
        **`a!ping`** - View bot latency
        **`a!about`** - Bot info
        **`a!donate`** - Link to support me
        **`a!vote`** - An other way to support me
        **`a!support`** - Discord support if you need help or want to discuss with me
        **`a!invite`** - returns bot link invite
        **`<a!help | a!h>`** - returns bot's commands"""
        embed = discord.Embed(title='**Available commands:**',
                            colour=self.colour,
                            description="`[RequiredArgument] <ParameterToChoose>`\n[Source code and commands](https://takitsu21.github.io/ApexStats/)")
        embed.add_field(name="Stats commands", value=stats_commands)
        embed.add_field(name="Apex Commands", value=apex_commands)
        embed.add_field(name="News commands", value=news_command)
        embed.add_field(name="Bot commands", value=other_commands)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.author.send(embed=embed)
        embed = discord.Embed(title="Permissions missing",
                            description="Please could you provide the following permissions "
                            "to Apex Stats to have access to all of the features\n-> Manage messages, Add reactions, Manage nicknames\nThank you!",
                            colour=self.colour)
        
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)

        await ctx.guild.owner.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))
