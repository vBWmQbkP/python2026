import datetime
from chinese_calendar import is_holiday

# 假设这是你的字符串日期
date_str = "2026-01-22" 

test1 = datetime.datetime.strptime(date_str, "%Y-%m-%d")
print(test1)
print(test1.date())
# 方法：使用 strptime 解析字符串为 date 对象
test_date = datetime.datetime.strptime(date_str, "%Y-%m-%d").date()

print(is_holiday(test_date))


# 1. datetime.datetime.strptime(...)
#    - 作用：将字符串解析为“日期+时间”对象。
#    - 原因：Python 的 date 类没有 strptime 方法，只有 datetime 类有。
#    - 结果：生成一个包含时间部分（默认为 00:00:00）的对象。
#
# 2. .date()
#    - 作用：从上面的对象中“切”出纯日期部分，丢弃时间信息。
#    - 原因：chinese_calendar 库严格要求传入 datetime.date 类型，不能带时间。
#    - 最终结果：得到一个纯粹的 datetime.date(2026, 3, 22) 对象。

# .date() 方法从 datetime 对象中“切”出日期部分，丢弃时间部分
# .date() 方法无法直接处理字符串, 因此需要通过 datetime.datetime.strptime(...) 先解析为 datetime 对象, 再使用 .date() 方法切出日期部分

# datetime.datetime.strptime(...)的作用是将字符串解析为 datetime 对象
# datetime.datetime 包含年月日 时分秒