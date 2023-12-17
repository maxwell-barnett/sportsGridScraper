from bs4 import BeautifulSoup
import requests

sport = input("fb or bb? ")
team1 = input("Team 1: ")
team2 = input("Team 2: ")
if sport == "fb":
    url1 = "https://www.pro-football-reference.com/teams/" + team1 + "/career-av.htm"
    url2 = "https://www.pro-football-reference.com/teams/" + team2 + "/career-av.htm"
else:
    url1 = "https://www.basketball-reference.com/teams/" + team1 + "/players.html"
    url2 = "https://www.basketball-reference.com/teams/" + team2 + "/players.html"
result1 = requests.get(url1)
result2 = requests.get(url2)
page1 = BeautifulSoup(result1.text, "html.parser")
page2 = BeautifulSoup(result2.text, "html.parser")

players1 = page1.findAll("td", attrs={"data-stat":"player"})
players2 = page2.findAll("td", attrs={"data-stat":"player"})
years1 = page1.findAll("td", attrs={"data-stat":"year_max"})
years2 = page2.findAll("td", attrs={"data-stat":"year_max"})

index = 0
playerList1 = []
for player in players1:
    if (int(years1[index].text) >= 1999):
        playerList1.append(player.text)
    index += 1

index = 0
playerList2 = []
for player in players2:
    if (int(years2[index].text) >= 1999):
        playerList2.append(player.text)
    index += 1

print(set(playerList1).intersection(playerList2))