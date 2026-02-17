import sqlite3
import json

class UserStore:
    def __init__(self, db_path=":memory:"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.init_db()

    def init_db(self):
        
        self.conn.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, data TEXT)")
        self.conn.commit()

    def save(self, user_id, user_dict):
        
        user_json = json.dumps(user_dict)
        self.conn.execute("INSERT OR REPLACE INTO users (id, data) VALUES (?, ?)", (user_id, user_json))
        self.conn.commit()

    def load(self):
        
        cursor = self.conn.execute("SELECT data FROM users")
        return [json.loads(row[0]) for row in cursor.fetchall()]

    def find_by_id(self, user_id):
        
        cursor = self.conn.execute("SELECT data FROM users WHERE id = ?", (user_id,))
        row = cursor.fetchone()
        return json.loads(row[0]) if row else None

    def delete_user(self, user_id):
        
        self.conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()
        return True


print("Connecting to SQLite database (In-Memory)...")
store = UserStore()


store.save(1, {"id": 1, "name": "Lithin", "role": "Student"})
print("Test: User saved successfully.")


users = store.load()
print(f"Test: Total users in DB: {len(users)}")


user = store.find_by_id(1)
print(f"Test: Found user: {user['name']}")


store.delete_user(1)
print("Test: User deleted. Final count:", len(store.load()))

print("\nDatabase CRUD Operations Successful")
