import discord,asyncio, datetime, time
from discord.ext import commands
import ressources.mail_handler as mail


class Feedback(commands.Cog):
    """Send feedback to the dev"""
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

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
            await ctx.send(embed=embed)
            return
        message = ' '.join(message)
        mail.send_msg(ctx.author, message, "SUGGESTION")
        embed = discord.Embed(title='**Suggestion**',
                            colour=self.colour,
                            description=f"{ctx.author.mention} Your suggestion has been sent!\nThanks for the feedback",
                            icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

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
            await ctx.send(embed=embed)
            return
        message = ' '.join(message)
        mail.send_msg(ctx.author, message, "BUG REPORT")
        embed = discord.Embed(title='**Bug Report**',
                            colour=self.colour,
                            description=f"{ctx.author.mention} Your bug report has been sent!\nThanks for the feedback",
                            icon_url=ctx.guild.me.avatar_url)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Feedback(bot))
    print("Added Feedback")
