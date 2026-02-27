from datetime import datetime, timedelta, timezone

def parse_datetime(s):
    dt_str, tz_str = s.rsplit(' ', 1)
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M:%S")
    sign = 1 if tz_str[3] == '+' else -1
    hours = int(tz_str[4:6])
    minutes = int(tz_str[7:9])
    tz_offset = timezone(timedelta(hours=sign*hours, minutes=sign*minutes))
    return dt.replace(tzinfo=tz_offset)

start = parse_datetime(input())
end = parse_datetime(input())

duration = int((end.astimezone(timezone.utc) - start.astimezone(timezone.utc)).total_seconds())
print(duration)