import os
from dotenv import load_dotenv
from balldontlie import BalldontlieAPI
import sys
from database import init_db, insert_game, insert_stats
from stats import get_top_scorer
from report import create_report


load_dotenv()

API_KEY = os.getenv("API_KEY")
if API_KEY is None : 
    sys.exit("Missing API KEY")
api = BalldontlieAPI(api_key=API_KEY)
init_db()


games = api.nba.games.list(dates = ["2025-03-14"])
top_scorer_name = ""
top_scorer_stats = 0
# Determine winner based on score
for game in games.data : 
    winner,winner_score, loser, loser_score = (game.home_team.full_name,game.home_team_score,game.visitor_team.full_name, game.visitor_team_score) if (game.home_team_score > game.visitor_team_score) else (game.visitor_team.full_name,game.visitor_team_score,game.home_team.full_name,game.home_team_score)
    insert_game(game)
    name, pts, reb, ast = get_top_scorer(game_date="2025-03-14", home_team_name=game.home_team.full_name)
    insert_stats(game.id,name,pts,reb,ast)
    print(f"{winner} won ({int(winner_score)} - {int(loser_score)}) against {loser}")
    print(f"TOP SCORER : {name} — {pts} pts, {reb} reb, {ast} ast")
create_report("2025-03-14")
    
        
            
            


    

