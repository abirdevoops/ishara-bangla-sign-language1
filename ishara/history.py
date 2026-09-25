from .auth import conn
def add_history(uid,mode,text,confidence):
 c=conn(); c.execute('INSERT INTO history(user_id,mode,text,confidence) VALUES(?,?,?,?)',(uid,mode,text,int(confidence))); c.commit(); c.close()
def get_history(uid):
 c=conn(); r=c.execute('SELECT text,mode,created_at,confidence FROM history WHERE user_id=? ORDER BY id DESC LIMIT 50',(uid,)).fetchall(); c.close(); return r
def clear_history(uid):
 c=conn(); c.execute('DELETE FROM history WHERE user_id=?',(uid,)); c.commit(); c.close()
