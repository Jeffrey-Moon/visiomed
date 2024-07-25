from datetime import datetime
import requests
import time

access = time.strftime('%Y-%m-%d %H:%M')
now = datetime.now()
print(access)
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
print(month)
print(now)
res = requests.post('http://172.30.1.43:8091/controller/mkbox.do', json={
  "MED_SERIAL": "1234567",
  "MED_BOX": "box1"
})

print(res.text)

#MED_SEQ	         1      약통 순번

#USER_ID		   2     장애인 시리얼

#MED_BOX	         3	   약보관함 번호

#MED_NAME 	   4	   보관약 이름

#MED_HOSP 	   5	   처방 의료기관

#MED_WAY 	   6	   투약 방법

#MED_TIMES 	   7	   투약 횟수

#MED_DATE	   8	   처방 일자

#MED_ALARM       9     알람 시간

#MED_UPDATE    10	   업데이트 시간

#MED_MEMO 	  11	   보관함 메모

#MED_SERIAL 	  12	   보관함 시리얼

#MED_LOG	DATE  13    보관함 로그



