import sqlite3

def init_db():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect("microblog.db")
    cursor = conn.cursor()

    # Create posts table
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL
        )
        '''
    )

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("Database initialized successfully.")