# 서울의 오늘 날짜를 "YYYY-MM-DD" 형식으로 출력한다.
import datetime
print((datetime.datetime.now() + datetime.timedelta(hours=9)).strftime('%Y-%m-%d'))