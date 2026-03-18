from nba_api.stats.endpoints import boxscoretraditionalv2, leaguegamefinder
from nba_api.library.http import NBAStatsHTTP
import time

NBAStatsHTTP.HEADERS = {
    "Host": "stats.nba.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": "https://www.nba.com/",
    "Origin": "https://www.nba.com",
}

def get_top_scorer(game_date: str, home_team_name: str):
    time.sleep(1)

    finder = leaguegamefinder.LeagueGameFinder(
        date_from_nullable=game_date,
        date_to_nullable=game_date,
    )
    games_df = finder.get_data_frames()[0]

    match = games_df[games_df["TEAM_NAME"].str.contains(home_team_name.split()[-1])]

    if match.empty:
        return None, None, None, None

    nba_game_id = match.iloc[0]["GAME_ID"]

    time.sleep(1)
    boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=nba_game_id)
    players_df = boxscore.get_data_frames()[0]

    top = players_df.loc[players_df["PTS"].idxmax()]

    return top["PLAYER_NAME"], int(top["PTS"]), int(top["REB"]), int(top["AST"])
