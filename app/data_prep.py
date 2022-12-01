import datetime, calendar

def properDates():
    end_year = datetime.datetime.today().year
    end_month = datetime.datetime.today().month
    start_year = datetime.datetime.today().year-1
    start_month = datetime.datetime.today().month+1
    dates = [(date//12,date % 12+1) for date in range(12*end_year+end_month-1,12*start_year+start_month-2,-1)]
    return dates

def computeIntradayData(symbol):
    # finnhub returns intraday data for 1 month, i need to call the api 12 times in order to get data for the whole year
    all_data = []
    dates = properDates()
    for d in dates:
        getProperEndDay(d)

def getProperEndDay(year_month):
    dt = datetime.strptime(year_month[0], '%Y')
    dt1 = datetime.strptime(year_month[1], '%m')
    end_day = calendar.monthrange(dt,dt1)
    print(end_day)

computeIntradayData("SPY")