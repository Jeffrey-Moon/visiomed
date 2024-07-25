import pymysql as ps

conn = ps.connect(host = 'localhost', user='root',passwd='1234', db='test')
curs=conn.cursor() #커서객체 데이터베이스 안에 값을 저장
sql = "select * from tstable"
curs.execute(sql)
result = curs.fetchall()
print(result)
conn.close()