import sqlite3 as sq

def login(login, passw, signal):
    con = sq.connect('handler/users')
    cur = con.cursor()



    cur.close()
    con.close()


def register(login, passw, signal):
    con = sq.connect('handler/users')
    cur = con.cursor()



    con.close()
    cur.close()