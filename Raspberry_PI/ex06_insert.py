import pymysql as ps
import ex04_spidevRead as sr
import time
while (True):
    readData = sr.analog_read(0)

    conn = ps.connect(host = 'localhost', user='root',
           passwd='1234', db='test')
    curs=conn.cursor() #커서객체 데이터베이스 안에 값을 저장
    sql = f"insert into sensordb(sensing) values({str(readData)})"
    curs.execute(sql)
    conn.commit()
    time.sleep(100)


