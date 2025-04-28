import datetime
"""输入日期， 判断这一天是这一年的第几天？"""
def dayofyear():
	year = input("请输入年份: ")
	month = input("请输入月份: ")
	day = input("请输入天: ")
	date1 = datetime.date(year=int(year),month=int(month),day=int(day))
	date2 = datetime.date(year=int(year),month=1,day=1)
	print((date1-date2).days+1)
	return (date1-date2).days+1
if __name__ == '__main__':
	dayofyear()