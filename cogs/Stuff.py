from discord.ext import commands
from src.stats import Weapons
import discord

class Stuff(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def peacekeeper(self, ctx):
        wp = Weapons("peacekeeper")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)
    
    @commands.command()
    async def mozambique(self, ctx):
        wp = Weapons("mozambique")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)
    
    @commands.command(aliases=["eva8", "eva8auto"])
    async def eva(self, ctx):
        wp = Weapons("eva-8-auto")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command(aliases=["mastif"])
    async def mastiff(self, ctx):
        wp = Weapons("mastiff")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command(aliases=["g7scout"])
    async def g7(self, ctx):
        wp = Weapons("g7-scout")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def r99(self, ctx):
        wp = Weapons("r-99")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def r301(self, ctx):
        wp = Weapons("r-301")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def alternator(self, ctx):
        wp = Weapons("alternator")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)
    
    @commands.command()
    async def prowler(self, ctx):
        wp = Weapons("prowler")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def flatline(self, ctx):
        wp = Weapons("flatline")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command(aliases=["hemlock"])
    async def hemlok(self, ctx):
        wp = Weapons("hemlok")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def havoc(self, ctx):
        wp = Weapons("havoc")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def spitfire(self, ctx):
        wp = Weapons("spitfire")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def devotion(self, ctx):
        wp = Weapons("devotion")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def lstar(self, ctx):
        wp = Weapons("l-star")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command(aliases=["re"])
    async def re45(self, ctx):
        wp = Weapons("re-45")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def p2020(self, ctx):
        wp = Weapons("p2020")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def wingman(self, ctx):
        wp = Weapons("wingman")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def longbow(self, ctx):
        wp = Weapons("longbow")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command(aliases=["triple", "triplet"])
    async def tripletake(self, ctx):
        wp = Weapons("triple-take")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def kraber(self, ctx):
        wp = Weapons("kraber")
        embed = wp.embed_w(ctx, wp.weapon())
        await ctx.send(embed=embed)

    @commands.command()
    async def weapons(self, ctx):
        embed = discord.Embed(
                    title="Listed commands for weapons",
                    description="All commands to get informations about a weapon.",
                    colour=0xff0004
                )
        embed.add_field(name="Peacekeeper", value="**a!peacekeeper**", inline=False)
        embed.add_field(name="R-99", value="**a!r99**", inline=False)
        embed.add_field(name="Alternator", value="**a!alternator**", inline=False)
        embed.add_field(name="Prowler", value="**a!prowler**", inline=False)
        embed.add_field(name="Hemlok", value="**a!hemlok**", inline=False)
        embed.add_field(name="R-301", value="**a!r301**", inline=False)
        embed.add_field(name="Havoc", value="**a!havoc**", inline=False)
        embed.add_field(name="Spitfire", value="**a!spitfire**", inline=False)
        embed.add_field(name="Devotion", value="**a!devotion**", inline=False)
        embed.add_field(name="L-Star", value="**a!lstar**", inline=False)
        embed.add_field(name="RE-45", value="**a!re45**", inline=False)
        embed.add_field(name="P2020", value="**a!p2020**", inline=False)
        embed.add_field(name="Wingman", value="**a!wingman**", inline=False)
        embed.add_field(name="Mozambique", value="**a!mozambique**", inline=False)
        embed.add_field(name="Eva 8 Auto", value="**a!eva**", inline=False)
        embed.add_field(name="Mastiff", value="**a!mastiff**", inline=False)
        embed.add_field(name="G7 Scout", value="**a!g7**", inline=False)
        embed.add_field(name="Longbow", value="**a!longbow**", inline=False)
        embed.add_field(name="Triple Take", value="**a!tripletake**", inline=False)
        embed.add_field(name="Kraber", value="**a!kraber**", inline=False)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Stuff(bot))