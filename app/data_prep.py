import pandas as pd
import dates_prep as dat
import client as cl


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
    lst = [clean for clean in lst if clean[0] not in ("Opened","Equities")]
    print(lst[:20])

def intradayTradesOnly(lst):
    date_today = ''
    for row in lst:
        

trades = cl.readCSV()
cleanReportValues(trades)