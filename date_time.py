from datetime import datetime
# s = '2014-02-16'
# # a = datetime(s, "%Y-%d-%m").timestamp()
#
# def get_date_time(timestamp: int, date_format="%Y-%m-%d", time_format="%H:%M"):
#     dt = datetime.fromtimestamp(timestamp / 1000, timezone.utc)
#     return dt.strftime(date_format), dt.strftime(time_format)
#
# date = datetime.strptime(s, '%Y-%m-%d').timestamp()
# print(date)
# a = datetime(int(s[:4]), int(s[6:7]), int(s[9:10])).timestamp()
# print(get_date_time(1672531200000))


print("-------")
s = '2014-02-16'
date = datetime.strptime(s, '%Y-%m-%d').date()
print(type(date))
date0 = datetime(2014, 2, 16).date()
print(date)
print(date0)
print(date == date0)


a= '1'
print(str(a))


