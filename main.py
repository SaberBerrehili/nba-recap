import os
import sys
from dotenv import load_dotenv
from balldontlie import BalldontlieAPI
from database import init_db, insert_game, insert_stats
from stats import get_top_scorer
from report import create_report

load_dotenv()

date = sys.argv[1]

API_KEY = os.getenv("API_KEY")
if API_KEY is None:
    sys.exit("Missing API_KEY")

api = BalldontlieAPI(api_key=API_KEY)
init_db()

games = api.nba.games.list(dates=date)

for game in games.data:
    if game.home_team_score > game.visitor_team_score:
        winner, winner_score, loser, loser_score = game.home_team.full_name, game.home_team_score, game.visitor_team.full_name, game.visitor_team_score
    else:
        winner, winner_score, loser, loser_score = game.visitor_team.full_name, game.visitor_team_score, game.home_team.full_name, game.home_team_score

    insert_game(game)
    name, pts, reb, ast = get_top_scorer(game_date=date, home_team_name=game.home_team.full_name)
    insert_stats(game.id, name, pts, reb, ast)
    print(f"{winner} won ({int(winner_score)} - {int(loser_score)}) against {loser}")
    print(f"Top scorer: {name} — {pts} pts, {reb} reb, {ast} ast")

create_report(date)
