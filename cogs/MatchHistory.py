import discord
from discord.ext import commands
from src.match_history import *
import datetime as dt
import time
import logging

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

class MatchHistory(commands.Cog):
    def __init__(self, bot):
        """Display apex stats"""
        self.bot = bot
        self.colour = 0xff0004

    def embed_matches(self, ctx, player, matches):
        m, old_m = str(), str()
        length_m = 0
        for i, c in enumerate(matches, start=1):
            if length_m >= 2000:
                m = old_m
                break
            old_m = m
            m += c + " | "
            if i % 2 == 0:
                m += "\n"
            length_m = len(m)

        embed = discord.Embed(
                    colour=self.colour,
                    timestamp=dt.datetime.utcfromtimestamp(time.time()),
                    description=m
                    )
        embed.set_author(name=player + " - Recent matches")
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        return embed

    @staticmethod
    def parse_user(args, platform):
        if len(args) > 1:
            platform = args.pop().lower()
        if platform in ["pc", "xbox", "psn"]:
            user = '%20'.join(args)
        return user, platform

    @commands.command(pass_context=True)
    async def history(self, ctx, *args, platform="pc"):
        try:
            finding = await ctx.send("`📡Fetching data...📡`")
            info = self.parse_user(list(args), platform)
            player, platform = info[0], info[1]
            if platform in ["pc", "xbox", "psn"]:
                matches = parse_history(get_match_history(player, platform))
                if len(player) >= 1:
                    embed = self.embed_matches(ctx, player, matches)
                    return await finding.edit(content="", embed=embed)
            else:
                embed = discord.Embed(
                            title="❌Wrong platform!❌",
                            colour=self.colour,
                            description=f'{ctx.author.mention} Wrong platform! retry with `pc` | `xbox` | `psn`'
                        )
        except discord.errors.HTTPException:
            embed = discord.Embed(title="**Too Many Stats to show!**",
                    description=f"Sorry, but i couldn't show your stats. It's too big.\nYou can see your profile [__**here**__]({generate_url_profile(player, platform)})",
                    timestamp=dt.datetime.utcfromtimestamp(time.time()), colour=self.colour)
        except PlayerNotFound:
            embed = discord.Embed(
                            title="❌Stats not found!❌",
                            description="Sorry but i couldn't found your Apex Legends history.\nYou may have made a foul of strikes.\n\nIf you spelled it right then the API might be down.",
                            colour=self.colour,
                            timestamp=dt.datetime.utcfromtimestamp(time.time())
                        )
            embed.set_thumbnail(url = ctx.guild.me.avatar_url)
        except KeyError:
            embed = discord.Embed(
                            title="No history found!",
                            description="This champion has no matches in his history",
                            timestamp=dt.datetime.utcfromtimestamp(time.time()),
                            colour=self.colour
                        )
        except Exception as e:
            print(type(e).__name__, e)
            embed = discord.Embed(
                                title="**Command**: **`a!history`**",
                                description="**`a!history [USERNAME] <pc | xbox | psn>`**",
                                timestamp=dt.datetime.utcfromtimestamp(time.time()),
                                colour=self.colour
                            )
            embed.add_field(name="Unknown error", value=f"{type(e).__name__} : {e}\nIf you can, try to report this error with `a!bug [MESSAGE]` Thank you!")
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP) | apex.tracker.gg", icon_url=ctx.guild.me.avatar_url)
        await finding.edit(content="",embed=embed)


def setup(bot):
    bot.add_cog(MatchHistory(bot))