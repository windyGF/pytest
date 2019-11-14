#定义月份
months=[
	'january',
	'February',
	'March',
	'April',
	'May',
	'June',
	'July',
	'August',
	'September',
	'October',
	'November',
	'December'
	]
#定义日期后缀
endings=['st','nd','rd']+17*['th']+['st','nd','rd']+7*['th']+['st']

#输入年月日
year = input("Year:")
month = input("Month:")
day  = input("Day:")

#整型转换
month_num = int(month)
day_num = int(day)

#日期月份换算
month_name = months[month_num-1]
day_name = day+endings[day_num-1]

print(month_name+' '+day_name+','+year)
