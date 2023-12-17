from bs4 import BeautifulSoup
import requests

topRowTeams = input("Type the teams or stats from the top row, separated by commas, here: ").lower()
topList = topRowTeams.split(',')
leftTeams = input("Type the teams or stats from the left side, separated by commas, here: ").lower()
leftList = leftTeams.split(',')

teamAbbreviationsMap = {
    "cardinals": "crd",
    "falcons": "atl",
    "ravens": "rav",
    "bills": "buf",
    "panthers": "car",
    "bears": "chi",
    "bengals": "cin",
    "browns": "cle",
    "cowboys": "dal",
    "broncos": "den",
    "lions": "det",
    "packers": "gnb",
    "texans": "htx",
    "colts": "clt",
    "jaguars": "jax",
    "chiefs": "kan",
    "raiders": "rai",
    "chargers": "sdg",
    "rams": "ram",
    "dolphins": "mia",
    "vikings": "min",
    "patriots": "nwe",
    "saints": "nor",
    "giants": "nyg",
    "jets": "nyj",
    "eagles": "phi",
    "steelers": "pit",
    "49ers": "sfo",
    "seahawks": "sea",
    "buccaneers": "tam",
    "titans": "oti",
    "commanders": "was",
}

names = []
count = 0
for topTeam in topList:
    for leftTeam in leftList:
        url = "https://www.pro-football-reference.com/friv/players-who-played-for-multiple-teams-franchises.fcgi?level=franch&t1=" + teamAbbreviationsMap[topTeam] + "&t2=" + teamAbbreviationsMap[leftTeam] + "&t3=--&t4=--"
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        nameList = soup.findAll('h3')
        if nameList[0] not in names:
            names.append(nameList[0])
        else:
            x = 1
            while nameList[x] in names:
                x += 1
            names.append(nameList[x])
        print(f'{topTeam} and {leftTeam} player: {names[count].text}')
        count += 1