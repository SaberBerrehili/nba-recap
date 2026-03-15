import os
from dotenv import load_dotenv
from balldontlie import BalldontlieAPI
import sys
from database import init_db, insert_game


load_dotenv()
API_KEY = os.getenv("API_KEY")
if API_KEY is None : 
    sys.exit("Missing API KEY")
api = BalldontlieAPI(api_key=API_KEY)
init_db()


games = api.nba.games.list(dates = ["2025-03-14"])
# Determine winner based on score
for game in games.data : 
    winner,winner_score, loser, loser_score = (game.home_team.full_name,game.home_team_score,game.visitor_team.full_name, game.visitor_team_score) if (game.home_team_score > game.visitor_team_score) else (game.visitor_team.full_name,game.visitor_team_score,game.home_team.full_name,game.home_team_score)
    print(f"{winner} won ({int(winner_score)} - {int(loser_score)}) against {loser} ")
    insert_game(game)
    
    

