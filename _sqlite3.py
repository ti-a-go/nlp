# import sqlite3

# con = sqlite3.connect('tutorial.db')

# cur = con.cursor()

# cur.execute("CREATE TABLE movie(title, year, score)")

# res = cur.execute()

# cur.execute("""
#     INSERT INTO movie VALUES
#         ('Monty Python and the Holy Grail', 1975, 8.2),
#         ('And Now for Something Completely Different', 1971, 7.5)
# """)

# con.commit()