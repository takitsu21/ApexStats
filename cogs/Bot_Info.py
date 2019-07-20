#coding: utf-8
import discord
from discord.ext import commands
import time, datetime

class Bot_Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def donate(self,ctx):
        embed = discord.Embed(title='**Donate** :',
                               description='[__**Patreon**__](https://www.patreon.com/takitsu)',
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def support(self,ctx):
        embed = discord.Embed(title='**Discord support**',
                               description='[**Click here**](https://discordapp.com/invite/wTxbQYb)',
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)

        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def invite(self,ctx):
        embed = discord.Embed(title='**Invite me** :',
                               description='[**here**](https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=52224)',
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)

        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def vote(self,ctx):
        embed = discord.Embed(title='**Vote for Apex Stats**',
                               description='[**Click here**](https://discordbots.org/bot/551446491886125059/vote)',
                                colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)", icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed = embed)

    @commands.command(pass_context=True)
    async def about(self,ctx):
        embed = discord.Embed(timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                              color=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.add_field(name="Vote",
                        value="[**here**](https://discordbots.org/bot/551446491886125059/vote)",inline=True)
        embed.add_field(name="Invite Apex Stats",
                        value="[**here**](https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=52224)",inline=True)
        embed.add_field(name="Support",
                        value="[**here**](https://discordapp.com/invite/wTxbQYb)",inline=True)

        embed.add_field(name="Prefix",value="a!",inline=True)

        nb_users = 0
        for s in self.bot.guilds:
            nb_users += len(s.members)

        embed.add_field(name="Servers",value=len(self.bot.guilds),inline=True)
        embed.add_field(name="Members",value=nb_users,inline=True)
        embed.add_field(name = "Website", value="[**here**](https://apexstatistics.gitbook.io/workspace/)")
        embed.add_field(name="**Creator**",value="Taki#0853",inline=True)
        embed.add_field(name="*Contributor*",value="RedstonedLife#8787",inline=True)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                         icon_url=ctx.guild.me.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """Ping's Bot"""
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Bot latency : `{int(ping)}ms`")

def setup(bot):
    bot.add_cog(Bot_Info(bot))
    print("Bot Info cog was added!")
