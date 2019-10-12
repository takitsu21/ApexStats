from src.utils import platform_convert, _request, headers
from src.enums import WeaponIcon, AmmoType
import discord
import datetime as dt
import time as t
from src.config import _wapi_token

class PlayerNotFound(Exception):
    pass

class Stats:
    """Stats object"""
    def __init__(self, player: str, platform: str):
        self.player = player
        self.base_platform = platform.lower()
        self.platform = platform_convert(platform)

    def data(self) -> dict:
        """Returns player's data"""
        URL = f"https://public-api.tracker.gg/v2/apex/standard/profile/{self.platform}/{self.player}"
        try:
            r = _request(URL, headers=headers, call="json")
            return r["data"]
        except Exception:
            raise PlayerNotFound("Request failed")

    def exists(self) -> bool:
        """Check if a player exist"""
        try:
            data = self.data()
            return True
        except PlayerNotFound:
            return False
    
    @staticmethod
    def parse_rank_url(url):
        url = url.split("/")
        rank = url[len(url)-1]
        i = 0
        res = str()
        while rank[i].isalpha() and rank[i] != ".":
            res += rank[i]
            i += 1
        if res == "apex":
            res += " predator"
        return res.capitalize()

class Weapons:
    def __init__(self, name, _type="weapons"):
        self.api_key = _wapi_token()
        self._type = _type if _type in ["weapons", "grenades", "equipment"] else None
        self.base_url = f"https://www.apexdata.gg/api/{self.api_key}/{self._type}/name/"
        self.name = name
        self.formatted_name = self.formatted_enum(self.name)

    def weapon(self):
        try:
            r = _request(f"{self.base_url}{self.name}.json", call="json")
            return r[0]
        except IndexError:
            return r
    @staticmethod
    def f_mode(fire_modes):
        try:
            return ' or '.join(fire_modes["fire_modes"].keys()).capitalize()
        except:
            return "Unknown"
    
    @staticmethod
    def formatted_enum(weapon):
        return weapon.replace("-", "").upper()

    def embed_w(self, ctx,  weapon_data, is_weapon=True):
        embed = discord.Embed(
                    colour=0xff0004,
                    timestamp=dt.datetime.utcfromtimestamp(t.time())
                )
        if is_weapon:
            embed.set_author(name=weapon_data["name"].capitalize(),
                            icon_url=getattr(AmmoType, weapon_data["ammo_type"].upper()))
            embed.add_field(name="Damage", value=weapon_data["damage"], inline=True)
            embed.add_field(name="Headshot damage", value=weapon_data["headshot_damage"], inline=True)
            embed.add_field(name="DPS", value=weapon_data["damage_per_second"], inline=True)
            embed.add_field(name="Magazine size", value=weapon_data["ammo_capacity"], inline=True)
            try:
                embed.add_field(name="Bullets per shot", value=weapon_data["damage_modifier"], inline=True)
            except: pass
            embed.add_field(name="Fire mode", value=self.f_mode(weapon_data), inline=True)
            embed.add_field(name="RPM", value=weapon_data["rate_of_fire"], inline=True)
            embed.add_field(name="Tactical reload", value=f'{weapon_data["tactical_reload"]} s', inline=True)
            embed.add_field(name="Empty reload", value=f'{weapon_data["empty_reload"]} s', inline=True)
            embed.set_image(url=getattr(WeaponIcon, self.formatted_name))
            embed.set_footer(text="Made with ❤️ by Taki#0853 (WIP)",
                            icon_url=ctx.guild.me.avatar_url)
        else:
            pass # grenades, etc...
        return embed