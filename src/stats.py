from src.utils import platform_convert, _request, headers

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
            raise PlayerNotFound(r.status_code)

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
