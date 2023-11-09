import sqlite3

def connect_to_database(database_path):
    try:
        connection = sqlite3.connect(database_path)
        return connection
    except sqlite3.Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def query_users_ids(connection):
    if connection:
        try:
            cursor = connection.cursor()

            # Assuming "members" is the table name and "user_id" is the column you want
            cursor.execute("SELECT user_id FROM members")

            # Fetch all the rows
            rows = cursor.fetchall()

            return rows

        except sqlite3.Error as e:
            print(f"Error executing the query: {e}")
            return None
        finally:
            # Close the cursor and connection after the operation
            cursor.close()
            connection.close()

    return None

if __name__ == "__main__":
    # Replace 'your_database.db' with the path to your actual database file
    database_path = 'your_database.db'

    # Connect to the database
    connection = connect_to_database(database_path)
    
    if connection:
        # Query for user_ids
        user_ids = query_users_ids(connection)

        if user_ids:
            print("User IDs:")
            for user_id in user_ids:
                print(user_id[0])  # Assuming user_id is the first (and only) column in the result
        else:
            print("No user IDs found.")

    else:
        print("Failed to connect to the database.")
