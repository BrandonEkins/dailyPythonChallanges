import requests
#api strings
bitcoin_url = "https://api.coinmarketcap.com/v2/ticker/1"
etherium_url = "https://api.coinmarketcap.com/v2/ticker/1027"
iota_url = "https://api.coinmarketcap.com/v2/ticker/1720"
ltc_url = "https://api.coinmarketcap.com/v2/ticker/2"
wallet = {btc=25,iot=25,eth=25,ltc=25} 

def getReleventInfo(crypto):
    cleancrypto = {}
    simplecrypto =  crypto.get('data').get('quotes').get('USD')
    cleancrypto['price'] = simplecrypto.get('price')
    cleancrypto['7d'] = simplecrypto.get('percent_change_7d')
    cleancrypto['1d'] = simplecrypto.get('percent_change_24h')
    cleancrypto['1h'] = simplecrypto.get('percent_change_1h')
    return cleancrypto


#getting information from the API
def getCryptoValues():
    cryptValue = {}
    cryptValue['btc'] = getReleventInfo(requests.get(bitcoin_url).json())
    cryptValue['eth'] = getReleventInfo(requests.get(etherium_url).json())
    cryptValue['iot'] = getReleventInfo(requests.get(iota_url).json())
    cryptValue['ltc'] = getReleventInfo(requests.get(ltc_url).json())
    return cryptValue 
    
def trade(fr,to) 
    
def compareCurrencies(c1,c2,p)
    if(c1-c2 > p):
        trade(c1,c2)
    elif(c2-c1 > p):
        trace(c2,c1)
    return
print(getCryptoValues())
#maybe look at pushing this information to a database.
#https://coinmarketcap.com/api/
#logic: so have a couple var that change percent & timeline. So essentialy ill have it take percent differences 
# 2 currencies and when they are a certain amount say 3% then we will trade all to the lower currency
# 