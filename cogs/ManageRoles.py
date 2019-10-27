import discord
from discord.ext import commands
from src.sql import select, addUser
import time
import datetime

class ManageRoles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.colour = 0xff0004

    def embed_save_profile(self, ctx):
        embed=discord.Embed(title="⚠️Profile not registered!",
                        description=f'{ctx.author.mention} Your profile is not yet registered in the database',
                        timestamp=datetime.datetime.utcfromtimestamp(time.time()),
                        colour=self.colour)
        embed.set_thumbnail(url=ctx.guild.me.avatar_url)
        embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                        icon_url=ctx.guild.me.avatar_url)
        return embed


    def db(self, ctx):
        try:
            user = select("users", "id", str(ctx.author.id))[0][1]
            if len(user) > 1:
                return True
            return False
        except Exception:
            addUser(str(ctx.author.id),"NAN")
            return self.embed_save_profile(ctx)

    @commands.bot_has_permissions()
    async def update(self, ctx):
        pass

def setup(bot):
    bot.add_cog(ManageRoles(bot))