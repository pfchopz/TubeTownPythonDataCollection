import requests
import json
from firebase import firebase

#Declare Variables
coin = 'bitcoin'
firebase = firebase.FirebaseApplication("https://tradingapp-61df0-default-rtdb.firebaseio.com/", None)

#Pull data from Firebase
response = requests.get('https://api.coingecko.com/api/v3/coins/' + coin + '/market_chart?vs_currency=usd&days=1')
result = firebase.post(coin, response.json())

print(result)

#STORES DATA IN JSON FILE, NOT NEEDED FOR THIS PROJECT
#with open("data_file.json", "w") as write_file:
#    json.dump(response.json(), write_file)
