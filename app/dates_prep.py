# import datetime, calendar
# import pandas as pd

# def properDates():
#     end_year, end_month = datetime.datetime.today().year, datetime.datetime.today().month
#     start_year, start_month = datetime.datetime.today().year-1, datetime.datetime.today().month+1
#     dates = [(date//12,date % 12+1) for date in range(12*end_year+end_month-1,12*start_year+start_month-2,-1)]
#     return dates

# def getProperEndDay(year,month):
#     end_day = calendar.monthrange(year,month)[1]
#     print(end_day)

# def dateToUnix(as_date):
#     pass