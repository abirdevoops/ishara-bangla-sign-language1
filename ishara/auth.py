import sqlite3, hashlib, os, re
DB='ishara.db'
def conn(): return sqlite3.connect(DB,check_same_thread=False)
def init_db():
 c=conn(); c.execute('CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,email TEXT UNIQUE NOT NULL,password_hash TEXT NOT NULL)'); c.execute('CREATE TABLE IF NOT EXISTS history(id INTEGER PRIMARY KEY AUTOINCREMENT,user_id INTEGER NOT NULL,mode TEXT NOT NULL,text TEXT NOT NULL,confidence INTEGER NOT NULL,created_at TEXT DEFAULT CURRENT_TIMESTAMP)'); c.commit(); c.close()
def _hash(p): return hashlib.sha256((os.getenv('ISHARA_PASSWORD_SALT','ishara-local-salt')+p).encode()).hexdigest()
def register_user(name,email,password):
 if not name.strip() or not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$',email): return False,'Enter a valid name and email.'
 try:
  c=conn(); c.execute('INSERT INTO users(name,email,password_hash) VALUES(?,?,?)',(name.strip(),email.strip().lower(),_hash(password))); c.commit(); c.close(); return True,'Account created. You can now sign in.'
 except sqlite3.IntegrityError: return False,'An account with this email already exists.'
def authenticate_user(email,password):
 c=conn(); row=c.execute('SELECT id,name,email FROM users WHERE email=? AND password_hash=?',(email.strip().lower(),_hash(password))).fetchone(); c.close(); return row
