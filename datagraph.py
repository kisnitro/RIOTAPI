import matplotlib.pyplot as plt
import csv
import os

#region init
#open csv, create list, data is the list
with open('stats.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

if not os.path.exists('Statistics'):
    os.mkdir('Statistics')
    print("Directory " , 'Statistics' ,  " Created ")
else:    
    print("Directory " , 'Statistics' ,  " already exists")
#endregion    
#region GET number of matches
    #number of analyzed matches
    #print(new_match)
    #new_match, stats only
new_match = []
x = (len(data))
number_of_matches = []
for k in range(1, x+1):
    number_of_matches.append(k)
print("Number of matches: ", x)
#endregion
#region GET lists
kills = []
deaths = []
assists = []
kda = []
vscore = []
wplaced = []
controlw = []
wkilled = []
for z in range(0, x):
    match = data[z]
    kills.append(float(match[2]))

for z in range(0, x):
    match = data[z]
    deaths.append(float(match[3]))

for z in range(0, x):
    match = data[z]
    assists.append(float(match[4]))

for z in range(0, x):
    match = data[z]
    kda.append(float(match[5]))

for z in range(0, x):
    match = data[z]
    vscore.append(float(match[6]))

for z in range(0, x):
    match = data[z]
    wplaced.append(float(match[7]))

for z in range(0, x):
    match = data[z]
    controlw.append(float(match[8]))    

for z in range(0, x):
    match = data[z]
    wkilled.append(float(match[9]))      
#endregion
# XAXIS: number_of_matches          YAXIS: kills, deaths, assists, kda, vscore, wplaced, controlw, wkilled
#region CHOOSE GRAPH and CREATE
while(True):
    gomb = int(input("Choose an option below:\n[1]: Kills\t[2]: Deaths\t[3]: Assists\n[4]: KDA\t[5]: Vision Score\t[6]: Wards placed\n[7]: Control wards purchased\t[8]: Wards killed\n"))
    if(gomb == 1):
        plt.plot(number_of_matches, kills)
        plt.plot(number_of_matches, kills, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Kills")
        plt.title("Kills in matches")
        plt.savefig('Statistics/Kills.png')
        plt.show()
    elif(gomb == 2):
        plt.plot(number_of_matches, deaths)
        plt.plot(number_of_matches, deaths, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Deaths")
        plt.title("Deaths in matches")
        plt.savefig('Statistics/Deaths.png')
        plt.show()
    elif(gomb == 3):
        plt.plot(number_of_matches, assists)
        plt.plot(number_of_matches, assists, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Assists")
        plt.title("Assists in matches")
        plt.savefig('Statistics/Assists.png')
        plt.show()
    elif(gomb == 4):
        plt.plot(number_of_matches, kda)
        plt.plot(number_of_matches, kda, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("KDA")
        plt.title("KDA[(K+A)/D] in matches")
        plt.savefig('Statistics/Deaths.png')
        plt.show()
    elif(gomb == 5):
        plt.plot(number_of_matches, vscore)
        plt.plot(number_of_matches, vscore, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Vision score")
        plt.title("Vision score in matches")
        plt.savefig('Statistics/VisionScore.png')
        plt.show()
    elif(gomb == 6):
        plt.plot(number_of_matches, wplaced)
        plt.plot(number_of_matches, wplaced, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Wards placed")
        plt.title("Wards placed in matches")
        plt.savefig('Statistics/WardsPlaced.png')
        plt.show()
    elif(gomb == 7):
        plt.plot(number_of_matches, controlw, 'ro')
        plt.plot(number_of_matches, controlw)
        plt.xlabel("Matches")
        plt.ylabel("Control Wards purchased")
        plt.title("Control Wards purchased in matches")
        plt.savefig('Statistics/ControlWardsPurchased.png')
        plt.show()
    elif(gomb == 8):               
        plt.plot(number_of_matches, wkilled)
        plt.plot(number_of_matches, wkilled, 'ro')
        plt.xlabel("Matches")
        plt.ylabel("Wards killed")
        plt.title("Wards killed in matches")
        plt.savefig('Statistics/WardsKilled.png')
        plt.show()
    else:
        exit()
#endregion




"""for z in range(0, x):
    match = data[z]
    for y in range(2,10):
        new_match.append(float(match[y]))
 print(new_match)       
        
        """