from flaretool.holiday import JapaneseHolidays
import datetime

input_date = input("日付を入力してください(例: 2024-01-01): ")
year, month, day = map(int, input_date.split("-"))

holidays = JapaneseHolidays()
date = datetime.date(year, month, day)
is_holiday = holidays.get_holiday_name(date)
print(is_holiday)
