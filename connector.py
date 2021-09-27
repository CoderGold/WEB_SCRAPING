import sqlite3
def connect(db):
    conn=sqlite3.connect(db)
    conn.execute("CREATE TABLE IF NOT EXISTS OYO_HOTELS (NAME TEXT,ADDRESS TEXT,PRICE INT,AMENITIES TEXT,RATING TEXT)")
    conn.close()

def insert_into_table(db,values):
    conn=sqlite3.connect(db)
    conn.execute("INSERT INTO OYO_HOTELS (NAME,ADDRESS,PRICE,AMENITIES,RATING) VALUES (?,?,?,?,?)")
    conn.commit()
    conn.close()
def get_hotel_info(db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute("SELECT * FROM OYO_HOTELS")
    table_data=cur.fetchall()
    for record in table_data:
        print(record)
    conn.close()
