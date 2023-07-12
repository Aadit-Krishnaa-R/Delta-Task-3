import sqlite3
import hashlib

conn = sqlite3.connect("userdata1.db")

cur = conn.cursor()

cur.execute("""
        CREATE TABLE IF NOT EXISTS userdata (
            id INTEGER PRIMARY KEY,
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL
    )
"""
)
            
username1, password1 = "aadit", hashlib.sha256("aadit@1805".encode()).hexdigest()
username2, password2 = "krishnaa", hashlib.sha256("krishnaa@2209".encode()).hexdigest()
username3, password3 = "simp", hashlib.sha256("simp@77".encode()).hexdigest()
username4, password4 = "thalaiva", hashlib.sha256("thalaiva@1112".encode()).hexdigest()

cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username1,password1))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username2,password2))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username3,password3))
cur.execute("INSERT INTO userdata (username,password) VALUES (?,?)",(username4,password4))

conn.commit()