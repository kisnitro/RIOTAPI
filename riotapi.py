import requests
import time
import os
fa = open("apikey.txt", "a")
fa.close()
ff = open("apikey.txt", 'r+') 
line = ff.readline()
api_key = str(line)
ff.close()
#region GET REGION and SUMMONER NAME
global region
sel_region = int(input("Please select region: [1]: EUNE\t[2]: EUW"))
if(sel_region == 1):
    region = "eun1"
elif(sel_region == 2):
    region = "euw1"

global name
gomb = int(input("Please choose from the following options \n [1]: Summoner name: SdnamrA \n [2]: Custom summoner name\n"))
if (gomb == 1):
    name = "SdnamrA"
    print("Option [1] selected")
elif (gomb == 2):
    print("Option [2] selected")
    name = input("Please enter your summoner name: ")
#endregion
def matchlist():
    base_link = "https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}"
    match_list = "https://{region}.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={api_key}"
    file1 = open("champion.txt", "a")
    file1.close()
    os.remove("champion.txt")
    gomb2 = int(input("Please choose from the following options \n [1]: Normal Draft \n [2]: SoloQ\n [3]: Flex\n"))
    if (gomb2 == 1):
        queueID = 400
        print("Option [1] selected")
    elif (gomb2 == 2):
        queueID = 420
        print("Option [2] selected")
    elif (gomb2 == 3):
        queueID = 440
        print("Option [3] selected")

    gomb3 = int(input("Please choose from the following options \n [1]: Custom champion ID\n [2]: champion\n"))
    if (gomb3 == 1):
        print("Option [1] selected")
        champID = int(input("Please enter champion ID: "))
    elif (gomb3 == 2):
        champID = 432
        print("Option [2] selected")
      

    #   GET accountId
    full_link = base_link.format(region=region, name=name,api_key=api_key)
    request = requests.get(full_link)
    r = request.json()
    accountId = r["accountId"]
    print ("Your account id is: ",accountId)
    print("Getting your match list ...")
    #   GET match history
    full_link = match_list.format(region=region, accountId=accountId,api_key=api_key)
    request = requests.get(full_link)
    r = request.json()
    #   show champion matches only
    for x in r['matches']:
        if (int(x['queue']) == queueID):
            if(int(x['champion']) == champID):
                gameId = x['gameId']
                gameId_text = str(gameId) + "\n"
                text_file = open("champion.txt", "a")
                text_file.write(gameId_text)
                text_file.close()

def matchdetails():
    baseLink = "https://{region}.api.riotgames.com/lol/match/v4/matches/{matchId}?api_key={api_key}"
    file5 = open("stats.csv", "a")
    file5.close()
    os.remove("stats.csv")
    d = ","
    temp = open("champion.txt",'r').read().split('\n')
    #Last 7 match
    del temp[-1]
    first = 0
    last = int(input("To: "))
    if(last >= len(temp)):
        last = len(temp)
    else:
        last = last + 1

    print(last)
    print(temp)
    for x in range(first, last):
        matchId = temp[x]
        newLink = baseLink.format(region=region, matchId=matchId, api_key=api_key)
        request = requests.get(newLink)
        r = request.json()
        lista = r['participantIdentities']
        for z in lista:
            player = z['player']
            partId = z['participantId']
            summoner = player['summonerName'], partId
            if (summoner == ('SdnamrA', partId) or summoner == (name, partId)):
                myid = summoner
        lista2 = r['participants']
        for y in lista2:
            ids = y['participantId']
            if ids == myid[1]:
                stats = y['stats']
                controlwards = str(stats['visionWardsBoughtInGame'])
                visionScore = str(stats['visionScore'])
                kills = str(stats['kills'])
                wardsKilled = str(stats['wardsKilled'])
                assists = str(stats['assists'])
                win = str(stats['win'])
                deaths = str(stats['deaths'])
                wardsPlaced = str(stats['wardsPlaced'])
        #kda = str((int(kills)+int(assists))/int(deaths))
        if (int(deaths) == 0):
            kda = str(int(kills)+int(assists))
        else:
            kda = str((int(kills)+int(assists))/int(deaths))
        output = "Match number #:" + str(x) + d + "Stats:" + d + kills + d + deaths + d + assists + d + kda + d + visionScore + d + wardsPlaced + d + controlwards + d + wardsKilled + d + win + "\n"
        f = open("stats.csv", "a")
        f.write(output)
        f.close()
    print("Success")

def menu():
    gomb = int(input("Select an option: \n[1]: Get matchlist \n[2]: Get match details\n[3]: Exit\n"))
    if (gomb == 1):
        matchlist()
    elif (gomb == 2):
        matchdetails()
    else:
        exit()

while True:
    menu()