import sqlite3

def startdb():
    conn = sqlite3.connect(r"./database/database.db")
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin(
            adminID TEXT NOT NULL,
            adminPASSWORD TEXT NOT NULL,
            adminPOSITION TEXT NOT NULL
    )''')