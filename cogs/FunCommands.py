import discord,asyncio,random, time, datetime
from discord.ext import commands

colour = 0xc8db

landings = {
    "Airbase": {
        "Name": "Airbase",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748164545052702/Airbase.jpg"
    },
    "Artillery": {
        "Name": "Artillery",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/377846848465010692/554742726952878080/artillery.jpg"
    },
    "Bridges": {
        "Name": "Bridges",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748223315640331/Bridges.jpg"
    },
    "Bunker": {
        "Name": "Bunker",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748287312199695/Bunker.jpg"
    },
    "Cascades": {
        "Name": "Cascades",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748334540062750/Cascades.jpg"
    },
    "Hydro Dam": {
        "Name": "Hydro Dam",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748399916679191/HydroDam.jpg"
    },
    "Market": {
        "Name": "Market",
        "Tier": "Low Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748461732331521/Market.jpg"
    },
    "Relay": {
        "Name": "Relay",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748519538229252/Relay.jpg"
    },
    "Repulsor": {
        "Name": "Repulsor",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748592221454396/Repulsor.jpg"
    },
    "Runoff": {
        "Name": "Runoff",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748716137840649/Runoff.jpg"
    },
    "Skull Town": {
        "Name": "Skull Town",
        "Tier": "Mid Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748775374258186/SkullTown.jpg"
    },
    "Slum Lakes": {
        "Name": "Slum Lakes",
        "Tier": "Mid Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748832307740682/SlumLakes.jpg"
    },
    "Swamps": {
        "Name": "Swamps",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748887508844544/Swamps.jpg"
    },
    "The Pit": {
        "Name": "The Pit",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748941581680643/ThePit.jpg"
    },
    "Thunderdome": {
        "Name": "Thunderdome",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554748988004368390/Thunderdome.jpg"
    },
    "Water Treatment": {
        "Name": "Water Treatment",
        "Tier": "High Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554749038998847499/Watertreatment.jpg"
    },
    "Wetlands": {
        "Name": "Wetlands",
        "Tier": "Mid Tier Loot",
        "ICON_URL": "https://cdn.discordapp.com/attachments/547488986239860739/554749091129851905/WetLands.jpg"
    }
}

class FunCommands(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def drop(self,ctx):
        land = random.choice(list(landings.keys()))
        embed = discord.Embed(title="Next game land at",color=colour, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="__Location__",value=landings[land]["Name"],inline=True)
        embed.add_field(name="__Loot Tier__",value=landings[land]["Tier"],inline=True)
        embed.set_image(url=landings[land]["ICON_URL"])
        embed.set_footer(text="command created by RedstonedLife#8787 | Bot created by Taki#0853 (WIP)",
                         icon_url = ctx.guild.me.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def legend(self,ctx):
        legends = ["Bangalore","Bloodhound","Lifeline","Pathfinder","Gibraltar","Wraith","Caustic","Mirage", "Octane"]
        await ctx.author.send(" Next game choose `{}`".format(random.choice(legends)))

def setup(bot):
    bot.add_cog(FunCommands(bot))
    print("Added Apex Cog from cogs")
