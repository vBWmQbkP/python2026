import datetime
from chinese_calendar import is_holiday

today = datetime.date.today()

if is_holiday(today):
    print("今天是休息日")
else:
    print("今天是工作日")