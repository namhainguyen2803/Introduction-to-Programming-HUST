import datetime

def add_days(cur_date,n):
    # cur_date = date(year = cur_date.year, day = cur_date.day, month = cur_date.month)
    delta = datetime.timedelta(days=n)
    res = cur_date + delta
    return res

cur_date = datetime.date(year=2016,month=2,day=10)
print(add_days(cur_date, 30))