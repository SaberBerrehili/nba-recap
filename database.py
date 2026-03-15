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
                        visitor_score INTEGER
        )""")
    
def insert_game(game):
    with sqlite3.connect('database.db') as connexion :
        curseur = connexion.cursor()
        curseur.execute(
            "INSERT OR IGNORE INTO games(id,date,season,home_team,home_score,visitor_team,visitor_score) VALUES (?,?,?,?,?,?,?)",(game.id,game.date,game.season,game.home_team.full_name,game.home_team_score,game.visitor_team.full_name,game.visitor_team_score))
          
        