import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """Create a database connection to the SQLite database."""
    try:
        conn = sqlite3.connect(db_file)
        print(f"Connected to SQLite database: {db_file}")
        return conn
    except Error as e:
        print(f"Error connecting to database: {e}")
        return None

def create_table(conn):
    """Create a sample table if it doesn't exist."""
    try:
        sql_create_table = """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER CHECK(age >= 0)
        );
        """
        conn.execute(sql_create_table)
        print("Table 'users' created or already exists.")
    except Error as e:
        print(f"Error creating table: {e}")

def insert_user(conn, name, age):
    """Insert a new user into the users table."""
    try:
        sql_insert = "INSERT INTO users (name, age) VALUES (?, ?)"
        conn.execute(sql_insert, (name, age))
        conn.commit()
        print(f"User '{name}' added successfully.")
    except Error as e:
        print(f"Error inserting user: {e}")

def fetch_users(conn):
    """Fetch and display all users."""
    try:
        cursor = conn.execute("SELECT id, name, age FROM users")
        rows = cursor.fetchall()
        print("\nUsers in database:")
        for row in rows:
            print(row)
    except Error as e:
        print(f"Error fetching users: {e}")

def update_user_age(conn, user_id, new_age):
    """Update a user's age."""
    try:
        conn.execute("UPDATE users SET age = ? WHERE id = ?", (new_age, user_id))
        conn.commit()
        print(f"User ID {user_id} age updated to {new_age}.")
    except Error as e:
        print(f"Error updating user: {e}")

def delete_user(conn, user_id):
    """Delete a user by ID."""
    try:
        conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
        conn.commit()
        print(f"User ID {user_id} deleted.")
    except Error as e:
        print(f"Error deleting user: {e}")

if __name__ == "__main__":
    database = "example.db"

    # Create a connection
    conn = create_connection(database)
    if conn:
        create_table(conn)

        # Insert sample data
        insert_user(conn, "Alice", 30)
        insert_user(conn, "Bob", 25)

        # Fetch and display data
        fetch_users(conn)

        # Update a record
        update_user_age(conn, 1, 31)

        # Delete a record
        delete_user(conn, 2)

        # Final fetch
        fetch_users(conn)

        conn.close()
