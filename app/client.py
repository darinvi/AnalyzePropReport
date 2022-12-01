import finnhub, time

def finnhubClient(symbol):
    epoch = int(time.time())
    client = finnhub.Client(api_key="caq8suiad3iecj6adq7g")
    data = client.stock_candles(symbol,"1",epoch-4000000,epoch)
    return data