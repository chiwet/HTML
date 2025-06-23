from fastapi import FastAPI, Body
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

conn = sqlite3.connect('database.db', check_same_thread=False)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_headers=['*'],
)

@app.post("/login")
def login(data: dict = Body(...)):
    username = data["username"]
    password = data["password"]
    cur = conn.cursor()
    cur.execute("SELECT password FROM users WHERE username = ?", (username,))
    true_password = cur.fetchone()

    if true_password:
      if password == true_password[0]:
        cur.execute("SELECT username, password FROM users where username = ?", (username,))
        userdata = cur.fetchone()
        print(userdata[0], userdata[1])
        return {"ok": 1, "user_id": userdata[0], "user_pass": userdata[1]}
    return {"ok": 0}

@app.post('/register')
def register(data: dict = Body(...)):
    username = data["username"]
    password = data["password"]
    cur = conn.cursor()
    cur.execute("SELECT 1 FROM users WHERE username = ?", (username,))
    if cur.fetchone() is None:
      cur.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
      conn.commit()
      return {"reg": 1}
    else:
        return {"reg": 0}

