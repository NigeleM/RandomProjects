


# Get info on crypto
import coinmarketcapapi
cmc = coinmarketcapapi.CoinMarketCapAPI("API Key ")
data = cmc.cryptocurrency_quotes_latest(symbol='BTC', convert='USD')
request = data.data.get('BTC')
print(request.get('name'))
print(request.get('symbol'))
quote = request.get('quote')
usd = quote.get('USD')
print(usd.get('price'))



# Crypto Code 
cmc = coinmarketcapapi.CoinMarketCapAPI("API Key ")
data = cmc.cryptocurrency_quotes_latest(symbol='ALGO', convert='USD')
request = data.data.get('ALGO')
print(request.get('name'))
print(request.get('symbol'))
quote = request.get('quote')
usd = quote.get('USD')
print(usd.get('price'))
    
