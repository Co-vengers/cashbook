import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()
class Database:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = os.getenv('db_host'),
                user = os.getenv('db_user'),
                password = os.getenv('db_password'),
                database = os.getenv('db_name')
            )
            if self.connection.is_connected():
                print("Connected to MySQL database")
        except Error as e:
            print(f"Error: {e}")
            self.connection = None

    def get_entries(self):
        if self.connection is None or not self.connection.is_connected():
            print("No database connection. Attempting to reconnect...")
            self.connect()
            if self.connection is None:
                return []

        try:
            with self.connection.cursor(dictionary=True) as cursor:
                cursor.execute('SELECT * FROM entries')
                return cursor.fetchall()
        except Error as e:
            print(f"Error fetching entries: {e}")
            return []

    def add_entry(self, date, description, amount, entry_type):
        if self.connection is None or not self.connection.is_connected():
            print("No database connection. Attempting to reconnect...")
            self.connect()
            if self.connection is None:
                return

        try:
            with self.connection.cursor() as cursor:
                cursor.execute('INSERT INTO entries (date, description, amount, type) VALUES (%s, %s, %s, %s)',
                               (date, description, amount, entry_type))
                self.connection.commit()
        except Error as e:
            print(f"Error adding entry: {e}")
            self.connection.rollback()
            
    def delete_entry(self, entry_id):
        if self.connection is None or not self.connection.is_connected():
            print("No database connection. Attempting to reconnect...")
            self.connect()
            if self.connection is None:
                return

        try:
            with self.connection.cursor() as cursor:
                cursor.execute('DELETE FROM entries WHERE id = %s', (entry_id,))
                self.connection.commit()
                print(f"Entry with id {entry_id} deleted.")
        except Error as e:
            print(f"Error deleting entry: {e}")
            self.connection.rollback()

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("MySQL connection closed.")