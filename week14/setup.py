import sqlite3

def init_system():
    
    con = sqlite3.connect(":memory:")
    cur = con.cursor()
    
    
    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT UNIQUE,
            role TEXT DEFAULT 'Student'
        )
    """)
    
    
    cur.execute("INSERT INTO users (name, email) VALUES (?, ?)", ("Lithin", "lithin@htw.de"))
    con.commit()
    
    
    cur.execute("SELECT * FROM users")
    row = cur.fetchone()
    print("DB Connection: OK")
    print("Stored Record:", row)
    
    con.close()

if __name__ == "__main__":
    init_system()
