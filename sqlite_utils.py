import sqlite3, sys, json, argparse
def init(db):
    con = sqlite3.connect(db); cur = con.cursor()
    cur.execute("create table if not exists kv(k text primary key, v text)")
    con.commit(); con.close()
def set_kv(db, k, v):
    con = sqlite3.connect(db); cur = con.cursor()
    cur.execute("insert or replace into kv(k,v) values (?,?)",(k,v))
    con.commit(); con.close()
def get_all(db):
    con = sqlite3.connect(db); cur = con.cursor()
    rows = cur.execute("select k,v from kv").fetchall()
    con.close(); return dict(rows)
def main():
    p = argparse.ArgumentParser()
    p.add_argument("db"); p.add_argument("--set", nargs=2); p.add_argument("--list", action="store_true")
    a = p.parse_args()
    init(a.db)
    if a.set: set_kv(a.db, a.set[0], a.set[1])
    if a.list: print(json.dumps(get_all(a.db)))
if __name__ == "__main__": main()
