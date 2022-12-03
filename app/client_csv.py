import finnhub, time, pandas

def finnhubClient(symbol):
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",1664663745,1669934145)
    return data

def readCSV():
    trades = pandas.read_csv("trades.csv").values.tolist()
    return trades

# trades = readCSV()
# print(trades[:20])