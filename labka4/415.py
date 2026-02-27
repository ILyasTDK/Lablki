from datetime import datetime, timedelta, timezone
import sys
import re
import calendar

def parse_datetime(s):
    date_str, tz_str = s.strip().split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    m = re.match(r'UTC([+-])(\d{2}):(\d{2})', tz_str)
    sign = 1 if m.group(1) == '+' else -1
    offset = timezone(timedelta(hours=sign*int(m.group(2)), minutes=sign*int(m.group(3))))
    return dt.replace(tzinfo=offset)

def days_to_next_birthday(birth, current):
    year = current.year
    month, day = birth.month, birth.day
    if month == 2 and day == 29 and not calendar.isleap(year):
        day = 28
    next_bday = datetime(year, month, day, tzinfo=birth.tzinfo)
    if next_bday < current.astimezone(birth.tzinfo):
        year += 1
        if month == 2 and day == 29 and not calendar.isleap(year):
            day = 28
        next_bday = datetime(year, month, day, tzinfo=birth.tzinfo)
    delta_seconds = (next_bday.astimezone(timezone.utc) - current.astimezone(timezone.utc)).total_seconds()
    return int(delta_seconds // 86400)

birth = parse_datetime(sys.stdin.readline())
current = parse_datetime(sys.stdin.readline())
print(days_to_next_birthday(birth, current))