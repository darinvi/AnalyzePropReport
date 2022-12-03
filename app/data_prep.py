import pandas as pd
import dates_prep as dat
import client_csv as cl
import math


# def computeIntradayData(symbol):
#     # finnhub returns intraday data for 1 month, i need to call the api 12 times in order to get data for the whole year
#     all_data = []
#     dates = dat.properDates()
#     for d in dates:
#         current_date = pd.to_datetime(f'{d[0]}-{d[1]}-1')
#         end_day = dat.getProperDates(current_date.year,current_date.month)
#         print(end_day)
#         # all_data = 

def cleanReportValues(lst):
    # Remove "Opened,Closed..." and "Equities..." rows as they are noise.
    nan = lst[0][1]
    lst = [clean for clean in lst if clean[0] not in ("Opened","Equities")]
    # Remove empty rows as they only contain nan values
    no_empty = [no_nan for no_nan in lst if len(set(no_nan))>1]
    # Only leave date in rows that represent date of report (date,nan,nan...)
    nan_lst = [[nonan[0]] if len(set(nonan))==2 else nonan for nonan in no_empty]
    return nan_lst


def intradayTradesOnly(lst):
    # A trade is an intraday trade if it is opened and closed in the same day. The way the report is shown is, a trade is reported at the day of closing.
    # Based on that, a trade is intraday if the date of the report is the same the value in the "Opened column" 
    intraday_trades = []
    date_today = ''
    for element in lst:
        if len(element)==1:
            date_today = element[0]
            print(date_today)

trades = cl.readCSV()
trades = cleanReportValues(trades)
intradayTradesOnly(trades)