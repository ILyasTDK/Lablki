from datetime import datetime, timedelta, timezone

def parse_datetime(s):
    date_str, tz_str = s.split()
    dt = datetime.strptime(date_str, "%Y-%m-%d")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    tz_offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz_offset)

dt1 = parse_datetime(input())
dt2 = parse_datetime(input())

delta_seconds = abs((dt1.astimezone(timezone.utc) - dt2.astimezone(timezone.utc)).total_seconds())
delta_days = int(delta_seconds // 86400)  # полные дни
print(delta_days)