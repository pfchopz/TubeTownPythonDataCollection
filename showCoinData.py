import requests
import json
import datetime
from firebase import firebase

#Declare Initial Variables
coin = 'bitcoin'
firebase = firebase.FirebaseApplication("https://tradingapp-61df0-default-rtdb.firebaseio.com/", None)

#Pull data from Firebase for processing
data = firebase.get(coin, '')

#Variables for parsing
mostRecentData = str(list(data.keys())[-1])
price = data.get(mostRecentData).get('prices')
marketCap = data.get(mostRecentData).get('market_caps')
volume = data.get(mostRecentData).get('total_volumes')
length = len(price)

#Header text
print('\n\n\n' + coin.capitalize() + ' Incremental Data' + '\n') 

#Parse information from data variable for clean user readability
for i in range(0, length):
    thisTime = datetime.datetime.fromtimestamp(price[i][0]/1000).strftime('%c')
    thisPrice = '$' + str(f'{int(price[i][1]):,d}')
    thisMarketCap = '$' + str(f'{int(marketCap[i][1]):,d}')
    thisVolume = str(f'{int(volume[i][1]):,d}')

    print(coin.capitalize() + ' - ' + thisTime + ':    ' + 'Price: ' + thisPrice + '   ' + 'Market Cap: ' + thisMarketCap + '   ' + 'Total Volume: ' + thisVolume)
