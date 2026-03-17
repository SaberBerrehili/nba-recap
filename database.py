import sqlite3

def init_db():
    with sqlite3.connect('database.db') as connexion :
        curseur = connexion.cursor()
        curseur.execute("""CREATE TABLE IF NOT EXISTS games
                        (id INTEGER PRIMARY KEY, 
                        date TEXT,
                        season INTEGER,
                        home_team TEXT,
                        home_score INTEGER,
                        visitor_team TEXT,
                        visitor_score INTEGER,
                        top_scorer_name TEXT,
                        top_scorer_pts INTEGER,
                        top_scorer_reb INTEGER,
                        top_scorer_ast INTEGER
            )""")
    
def insert_game(game):
    with sqlite3.connect('database.db') as connexion :
        curseur = connexion.cursor()
        curseur.execute(
            "INSERT OR IGNORE INTO games(id,date,season,home_team,home_score,visitor_team,visitor_score) VALUES (?,?,?,?,?,?,?)",(game.id,game.date,game.season,game.home_team.full_name,game.home_team_score,game.visitor_team.full_name,game.visitor_team_score))
          
def insert_stats(game_id,name,pts,reb,ast):
    with sqlite3.connect('database.db') as connexion :
        curseur = connexion.cursor()
        curseur.execute(
            "UPDATE games SET top_scorer_name = ?, top_scorer_pts = ?, top_scorer_reb = ? , top_scorer_ast= ? WHERE id = ?",(name,pts,reb,ast,game_id))

        