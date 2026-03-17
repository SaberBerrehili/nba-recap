import sqlite3


def get_game_by_date(date):
     with sqlite3.connect('database.db') as connexion :
        curseur = connexion.cursor()
        Game_list = []
        for line in curseur.execute("SELECT home_team, home_score, visitor_team,visitor_score, top_scorer_name, top_scorer_pts, top_scorer_reb, top_scorer_ast from games WHERE date = ? ",(date,)):
            home_team = line[0]
            home_team_score = line[1] 
            visitor_team = line[2]
            visitor_team_score = line[3]
            joueur = line[4] 
            top_scorer_pts = line[5]
            top_scorer_ast = line[7]
            top_scorer_reb = line[6]
            Game_list.append((home_team,home_team_score,visitor_team,visitor_team_score,joueur,top_scorer_pts,top_scorer_ast,top_scorer_reb))
     return Game_list

def create_report(date):
    games = get_game_by_date(date)
    with open(f"Recap_{date}.md","w") as f:
        f.write(f"# NBA Recap : {date} \n")
        for game in games:
            f.write(f"## {game[0]} {game[1]} - {game[3]} {game[2]} \n")
            f.write(f"**Top Scorer** : {game[4]} with {game[5]} pts, {game[6]} ast, {game[7]} reb \n")
    
    
    
    