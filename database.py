import psycopg2
from psycopg2.extras import RealDictCursor
from contextlib import contextmanager

DB_CONFIG = {
    'host': 'localhost',
    'database': 'escuela_db',
    'user': 'postgres',
    'password': '123456'  
}

@contextmanager
def get_db_connection():
    conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
    try:
        yield conn
        conn.commit()  
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        conn.close()
