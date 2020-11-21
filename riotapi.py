import requests
import keyboard
import time
api_key = "RGAPI-85866b95-a0ee-4d1c-8073-e04baebc613b"

def matchlist():
    base_link = "https://eun1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{name}?api_key={api_key}"
    match_list = "https://eun1.api.riotgames.com/lol/match/v4/matchlists/by-account/{accountId}?api_key={api_key}"
    gomb = int(input("Please choose from the following options \n [1]: Summoner name: SdnamrA \n [2]: Custom summoner name\n"))
    if (gomb == 1):
        name = "SdnamrA"
        print("Option [Q] selected")
    elif (gomb == 2):
        print("Option [W] selected")
        name = input("Please enter your summoner name: ")

        """try:
            if keyboard.is_pressed('q'):
                name = "SdnamrA"
                print("Option [Q] selected")
                break
            elif keyboard.is_pressed('w'):
                print("Option [W] selected")
                name = input("Please enter your summoner name: ")
                break
        except:
            break     """      

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
                gameId = x['gameId']
                gameId_text = str(gameId) + "\n"
                text_file = open("BARD.txt", "a")
                text_file.write(gameId_text)
                text_file.close()

def matchdetails():
    baseLink = "https://eun1.api.riotgames.com/lol/match/v4/matches/{matchId}?api_key={api_key}"
    d = ";"
    temp = open("BARD.txt",'r').read().split('\n')
    #Last 7 match
    first = int(input("How many matches you want to be analyzed?(last match is first) \nFrom: "))
    last = int(input("To: "))
    last = last + 1
    for x in range(first, last):
        matchId = temp[x]
        newLink = baseLink.format(matchId=matchId, api_key=api_key)
        request = requests.get(newLink)
        r = request.json()
        lista = r['participantIdentities']
        for z in lista:
            player = z['player']
            partId = z['participantId']
            summoner = player['summonerName'], partId
            if (summoner == ('SdnamrA', partId)):
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
        output = "Match number #:" + str(x) + "; Stats: ;" + kills + d + deaths + d + assists + d + kda + d + visionScore + d + wardsPlaced + d + controlwards + d + wardsKilled + d + win + "\n"
        f = open("stats.txt", "a")
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