import sqlite3
import pandas as pd

def db_helper():
    con = sqlite3.connect("sample.db")
    cur = con.cursor()

    sql_execute(cur, con)

    con.commit()
    con.close()

def sql_result(sql_text, con):
    print(f"「{sql_text}」")
    df = pd.read_sql_query(sql_text, con)
    print(df)

def sql_execute(cur, con):
    # CREATE TABLE
    cur.execute("CREATE TABLE machines(id, name)")

    # ADD DATA
    machines_list = [(0,"スマスロ北斗の拳"), (1,"マイジャグラーV"), (2,"押忍！番長4"), (3,"バジリスク～甲賀忍法帖～絆2 天膳 BLACK EDITION"), (4,"革命機ヴァルヴレイヴ")]
    cur.executemany("INSERT INTO machines VALUES(?, ?)", machines_list)
    sql_result("SELECT * FROM machines", con)

    #cur.execute("DROP TABLE machines")

db_helper()