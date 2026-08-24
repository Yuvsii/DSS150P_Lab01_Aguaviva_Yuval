"""Minimal PostgreSQL inspection starter."""

import psycopg
from config import DB_CONFIG

def main():
    with psycopg.connect(**DB_CONFIG) as conn:
        with conn.cursor() as cur:
            # Get Row Count
            cur.execute("SELECT COUNT(*) FROM support_tickets;")
            print("=== support_tickets rows ===")
            print(cur.fetchone()[0])
            
            # Get Columns, Data Types, and Nullability
            print("\n=== Columns, Types, Nullability ===")
            cur.execute("""
                SELECT column_name, data_type, is_nullable 
                FROM information_schema.columns 
                WHERE table_name = 'support_tickets'
                ORDER BY ordinal_position;
            """)
            for row in cur.fetchall():
                print(row)
                
            # Get 5 Sample Rows
            print("\n=== 5 Sample Rows ===")
            cur.execute("SELECT * FROM support_tickets LIMIT 5;")
            for row in cur.fetchall():
                print(row)

if __name__ == "__main__":
    main()