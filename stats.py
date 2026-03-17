from nba_api.stats.endpoints import boxscoretraditionalv2, leaguegamefinder
import time

def get_top_scorer(game_date: str, home_team_name: str):
    time.sleep(0.6)  # avoids rate limiting on the NBA API
    
    finder = leaguegamefinder.LeagueGameFinder(
        date_from_nullable=game_date,
        date_to_nullable=game_date,
    )
    games_df = finder.get_data_frames()[0]
    
    # Filter by home team name
    match = games_df[games_df["TEAM_NAME"].str.contains(home_team_name.split()[-1])]
    
    if match.empty:
        return None, None, None, None
    
    nba_game_id = match.iloc[0]["GAME_ID"]
    
    time.sleep(0.6)
    boxscore = boxscoretraditionalv2.BoxScoreTraditionalV2(game_id=nba_game_id)
    players_df = boxscore.get_data_frames()[0]
    
    top = players_df.loc[players_df["PTS"].idxmax()]
    
    return top["PLAYER_NAME"], int(top["PTS"]), int(top["REB"]), int(top["AST"])
