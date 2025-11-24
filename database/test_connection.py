from connection import get_engine

try:
    engine = get_engine()
    conn = engine.connect()
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Connection failed:", e)
