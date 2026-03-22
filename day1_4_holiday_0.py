import datetime
from chinese_calendar import is_holiday, is_workday

test_date = datetime.date(2026, 3, 22)

print(is_holiday(test_date))
print(is_workday(test_date))