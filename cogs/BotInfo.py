#coding: utf-8
import discord
from discord.ext import commands
import time
import datetime

class Bot_Info(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.colour = 0xff0004

    @commands.command(pass_context=True)
    async def donate(self,ctx):
        embed = discord.Embed(title='**Donate** :',
                              colour=self.colour)
        embed.add_field(name="Patreon", value='[Patreon](https://www.patreon.com/takitsu)', inline=False)
        embed.add_field(name="Buy me a Kofi", value="[Click here](https://ko-fi.com/takitsu)")
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
        embed = discord.Embed(
                        title='**Invite me** :',
                        description='[**here**](https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=8)',
                        colour=self.colour
                    )
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
    async def about(self, ctx):
        embed = discord.Embed(
                            timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                            color=self.colour
                        )
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.add_field(name="Vote",
                        value="[Click here](https://discordbots.org/bot/551446491886125059/vote)")
        embed.add_field(name="Invite Apex Stats",
                        value="[Click here](https://discordapp.com/oauth2/authorize?client_id=551446491886125059&scope=bot&permissions=1543825472)")
        embed.add_field(name="Discord Support",
                        value="[Click here](https://discordapp.com/invite/wTxbQYb)")
        embed.add_field(name="Donate",value="[Click here](https://www.patreon.com/takitsu)")
        embed.add_field(name = "Source code and commands", value="[Click here](https://takitsu21.github.io/ApexStats/)")
        embed.add_field(name="Help command",value="a!help")
        nb_users = 0
        for s in self.bot.guilds:
            nb_users += len(s.members)

        embed.add_field(name="Servers", value=len(self.bot.guilds))
        embed.add_field(name="Members", value=nb_users)
        embed.add_field(name="**Creator**", value="Taki#0853")
        embed.add_field(name="*Contributor*", value="RedstonedLife#0001")
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)

        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """Ping's Bot"""
        before = time.monotonic()
        message = await ctx.send("🏓Pong!")
        ping = (time.monotonic() - before) * 1000
        embed = discord.Embed(colour=0xff00,
                            title="Apex Stats ping",
                            description=f"🏓{int(ping)} ms")
        await message.edit(content="", embed=embed)

def setup(bot):
    bot.add_cog(Bot_Info(bot))