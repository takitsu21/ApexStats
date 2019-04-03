import requests
from ressources.tools import *
import ressources.SqlManagment as  SqlManagment

class CreateLeaderboard:
    def leaderboard_init(self, leaderboard : dict = SqlManagment.createLeaderboard()):
        data_stats = {}
        for player, platform in leaderboard.items():
            r = requests.get(f'https://public-api.tracker.gg/apex/v1/standard/profile/{platformConvert(platform)}/{player}', headers = headers).json()
            data_stats[r['data']['metadata']['platformUserHandle']] = r['data']['metadata']['level']
            print(r['data']['metadata']['platformUserHandle'], r['data']['metadata']['level'])
        return data_stats

    def sorted_leaderboard(self):#+ to - by level
         return sorted(self.leaderboard_init().items(), key = lambda kv:(kv[1], kv[0]), reverse=True)


    async def leaderboard_to_database(self):
        _leaderboard = self.sorted_leaderboard()
        SqlManagment.delete_table('leaderboard')
        SqlManagment.create_leaderboard()
        for i in range(10):
            SqlManagment.add_position_leaderboard(str(i+1), _leaderboard[i][0], str(_leaderboard[i][1]))
