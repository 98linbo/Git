import pymysql
import re



args={
    "host":"localhost",
    "port":3306,
    "user":"root",
    "password":"123456",
    "database":"dict",
    "charset":"utf8"
}

db=pymysql.connect(**args)
cur = db.cursor()

dict_text=open("../day01/dict.txt")

word_list=[]
for line in dict_text:
    result=re.findall(r"(\w+)\s+(.*)",line)
    word_list.extend(result)
try:
    sql="insert into word (word,mean) values (%s,%s);"
    cur.executemany(sql,word_list)
    db.commit()
except:
    db.rollback()

# 关闭
cur.close()
db.close()