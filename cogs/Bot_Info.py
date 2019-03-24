# This cog is basically all the !support, !discord, !upvote, etc....
import discord
from discord.ext import commands
import time

class Bot_Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def support(self,ctx):
        embed = discord.Embed(title='__Support me__ :',
                               description='Hey if you like my work and want to support me, you can do it here [__**Patreon**__](https://www.patreon.com/takitsu) or here [__**Buy me a Kofi**__](https://ko-fi.com/takitsu)',
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Bot created by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def discord(self,ctx):
        await ctx.send(f'{ctx.author.mention} https://discordapp.com/invite/wTxbQYb')

    @commands.command(pass_context=True)
    async def invite(self,ctx):
        await ctx.send(f'{ctx.author.mention} https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=52224')

    @commands.command(pass_context=True)
    async def apvote(self,ctx):
        await ctx.send(f'{ctx.author.mention} https://discordbots.org/bot/551446491886125059/vote')

    @commands.command(pass_context=True)
    async def apinfo(self,ctx):
        embed = discord.Embed(title="__**Apex Stats**__",description="Apex Legends statistics infos and more...",color=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.add_field(name="__Creator__",value="Taki#0853",inline=True)
        embed.add_field(name="*Contributor*",value="RedstonedLife#8787",inline=True)
        embed.add_field(name="Prefix",value="!",inline=True)

        active_servers = self.bot.guilds
        nb_users = 0
        for s in active_servers:
            nb_users += len(s.members)

        embed.add_field(name="Servers",value=len(active_servers),inline=True)
        embed.add_field(name="Members",value=nb_users,inline=True)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def apping(self,ctx):
        """Ping's Bot"""
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Bot latency : `{int(ping)}ms`")

def setup(bot):
    bot.add_cog(Bot_Info(bot))
    print("Bot Info cog was added!")
