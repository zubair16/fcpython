import asyncio
import json
import aiohttp
import numpy as np
import pandas as pd
from understat import Understat
import matplotlib.pyplot as plt


async def main():
    async with aiohttp.ClientSession() as session:
        understat = Understat(session)
        players = await understat.get_league_players(
            "epl",
            2019,
            team_title="Chelsea"
        )
        json_dump = json.dumps(players)
        json_data = json.loads(json_dump)
        # print(json_data)
        player_name = []
        minutes = []
        xg = []
        xa = []
        for players in json_data:
            player_name.append(players['player_name'])
            minutes.append(players['time'])
            xg.append(players['xG'])
            xa.append(players['xA'])

        the_array = np.array((player_name, minutes, xg, xa))
        df = pd.DataFrame(data=the_array, index=player_name, columns=minutes)
        print(the_array)

        # leagueWins = {'Team': ['Manchester United', 'Blackburn Rovers', 'Arsenal',
        #                       'Chelsea', 'Manchester City', 'Leicester City'],
        #              'Championships': [13, 1, 3, 4, 2, 1]}

        # df = pd.DataFrame(leagueWins, columns=['Team', 'Championships'])
        # print(df)
        # plt.pie(df['Championships'])

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
