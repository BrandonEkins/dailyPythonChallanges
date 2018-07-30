import requests
import loadDB
#api strings
bitcoin_url = "https://api.coinmarketcap.com/v2/ticker/1"
etherium_url = "https://api.coinmarketcap.com/v2/ticker/1027"
iota_url = "https://api.coinmarketcap.com/v2/ticker/1720"
ltc_url = "https://api.coinmarketcap.com/v2/ticker/2"

percent = 2
tf = "1d"#can be 1d 7d or 1h

class wallet:
    def __getattr__(self, name):
        return self[name]
    def __init__(self, w):
        self.id = w.id
        self.walletDate = w.walletDate
        self.btc = w.btc
        self.iot = w.iot
        self.ltc = w.ltc
        self.eth = w.eth
        self.ubtc = w.ubtc
        self.uiot = w.uiot
        self.ultc = w.ultc
        self.ueth = w.ueth

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

def trade(w, to, fr, amount):
    w[to] + amount
    w[fr] - amount
    loadDB.updateWallet(w, getCryptoValues())

def compareValues(a,b):
    if a[tf] - b[tf] > percent:
        return True
    else:
        return False

def tradeLogic(w):
    c = getCryptoValues()
    if compareValues(c['btc'],c['iot']):
        return trade(w,'btc','iot',w['iot'])
    elif compareValues(c['iot'],c['btc']):
        return trade(w,'iot','btc',w['btc'])
    return w

def main():
    #get wallet
    currentWallet = wallet(loadDB.getWallet())
    print(currentWallet.btc)
    currentWallet = tradeLogic(currentWallet)
    print(currentWallet.btc)

if __name__ == "__main__":
    main()
#maybe look at pushing this information to a database.
#https://coinmarketcap.com/api/
#logic: so have a couple var that change percent & timeline. So essentialy ill have it take percent differences
# 2 currencies and when they are a certain amount say 3% then we will trade all to the lower currency