import discord
from discord.ext import commands

class Feedback(commands.Cog):
    """Send feedback to me"""
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004
        self._id = 162200556234866688
        self.dm_me = self.bot.get_user(self._id)

    @commands.command(pass_context=True)
    async def suggestion(self, ctx, *message):
        if not len(message) or len(message) < 3:
            embed = discord.Embed(title='**Suggestion**',
                                colour=self.colour,
                                description=f"{ctx.author.mention} Message too short!\nAt least 3 words required",
                                icon_url=ctx.guild.me.avatar_url)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=ctx.guild.me.avatar_url)
            return await ctx.send(embed=embed)
        message = ' '.join(message)
        await self.dm_me.send(f"[{ctx.author} - SUGGEST] -> {message}")
        embed = discord.Embed(title='**Suggestion**',
                            colour=self.colour,
                            description=f"{ctx.author.mention} Your suggestion has been sent @Taki#0853\nThanks for the feedback",
                            icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        return await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def bug(self, ctx, *message):
        if not len(message) or len(message) < 3:
            embed = discord.Embed(title='**Bug Report**',
                    colour=self.colour,
                    description=f"{ctx.author.mention} Message too short!\nAt least 3 words required",
                    icon_url=ctx.guild.me.avatar_url)
            embed.set_thumbnail(url=ctx.guild.me.avatar_url)
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=ctx.guild.me.avatar_url)
            return await ctx.send(embed=embed)
        message = ' '.join(message)
        await self.dm_me.send(f"[{ctx.author} - BUG] -> {message}")
        embed = discord.Embed(title='**Bug Report**',
                            colour=self.colour,
                            description=f"{ctx.author.mention} Your bug report has been sent @Taki#0853\nThanks for the feedback",
                            icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Feedback(bot))