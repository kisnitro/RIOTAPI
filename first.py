import requests
import keyboard
import time

api_key = "RGAPI-6f903780-3c33-4b73-8d15-3511c2749d6c"
base_link = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}"
match_list = "https://eun1.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={api_key}"
print("Please choose from the following options \n [Q]: Summoner name: SdnamrA \n [W]: Custom summoner name")
while True:
    try:
        if keyboard.is_pressed('q'):
            name = "SdnamrA"
            print("Option [Q] selected")
            break
        elif keyboard.is_pressed('w'):
            print("Option [W] selected")
            name = input("Please enter your summoner name: ")
            break
    except:
        break           

#   GET accountId
full_link = base_link.format(name=name,api_key=api_key)
request = requests.get(full_link)
r = request.json()
accountId = r["accountId"]
print ("Your account id is: ",accountId)
print("Getting your match list ...")
#   GET match history
full_link = match_list.format(accountId=accountId,api_key=api_key)
request = requests.get(full_link)
r = request.json()
#   show BARD matches only
for x in r['matches']:
    if (int(x['queue']) == 400):
        if(int(x['champion']) == 432):
            print(x)
