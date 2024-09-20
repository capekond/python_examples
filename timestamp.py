times = ['07:00', '09:00', '11:00', '13:00', '15:00', '17:00', '19:00', '21:00']
dates = ['20131218']

from datetime import datetime, timezone
dt_prices = 1387393200000
print(dt_prices)
dt_object = datetime.fromtimestamp(dt_prices/1000, timezone.utc)
print(dt_object)
dt = datetime(2013, 12, 18, 19, 0o0)
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()
print(int(timestamp*1000))