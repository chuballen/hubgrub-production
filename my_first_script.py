import mysql.connector

db_config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'db_admin_password',
        'database': 'mariadb-doordash-db-prod'
}


try:
    conn = mysql.connector.connect(**db_config)

    if conn.is_connected():
        print("success!")

except mysql.connector.Error as err:
    print(f"error:{err}")

finally:
    conn.close()
