import psycopg2
from dotenv import load_dotenv
import os

# Memuat variabel dari file .env
load_dotenv()

def connect_to_database():
    """
    Membuat koneksi ke database PostgreSQL
    menggunakan kredensial dari file .env.
    """
    try:
        # Membaca variabel dari lingkungan
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        host = os.getenv("DB_HOST")
        port = os.getenv("DB_PORT")
        database = os.getenv("DB_NAME")

        # Membuat koneksi
        conn = psycopg2.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database
        )
        print("Connection to PostgreSQL successful!")
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
