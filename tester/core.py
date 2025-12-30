# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import os
import psycopg2
from dotenv import load_dotenv

def test_connection():
    load_dotenv()
    
    dsn = os.getenv("POSTGRES_DSN")
    if not dsn:
        print("Error: POSTGRES_DSN not found in .env")
        return False

    try:
        print("Connecting to PostgreSQL...")
        conn = psycopg2.connect(dsn)
        
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()[0]
        
        print(f"Success! Connected to:\n{version}")
        
        cursor.close()
        conn.close()
        return True
    
    except psycopg2.Error as e:
        print(f"Connection Failed: {e}")
        return False

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
