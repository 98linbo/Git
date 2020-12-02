import pymysql
while True:

    args = {
        "host": "localhost",
        "port": 3306,
        "user": "root",
        "password": "123456",
        "database": "dict",
        "charset": "utf8"
    }

    data=input("请输入单词：")
    db = pymysql.connect(**args)
    cur = db.cursor()
    sql=f"select * from word where word='{data}'"
    cur.execute(sql)
    print(cur.fetchall())