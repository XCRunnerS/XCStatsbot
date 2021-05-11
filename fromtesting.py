# uwu
#
from urllib.request import urlopen
import json
API_KEY = "865d083e-6526-44c4-a236-a73ba2295dee"
# XCRunnerS

name = "cffe420233a448289719f62ffcde53e4"
name_link = f"https://api.hypixel.net/player?key={API_KEY}&uuid={name}"

#   https://api.hypixel.net/player?key=86cbc8cf-c6c6-428c-a17a-c273c710485f&uuid=cffe420233a448289719f62ffcde53e4
#   testjson = json.loads(urlopen(name_link).read().decode("utf-8"))
ign = 'XCRunnerS'

uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
uuid = uuidurl["id"]

jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))

print(jsonurl)
print(uuid)
#print(jsondump['player']['stats']['Bedwars'])
#print(jsondump['player']['stats']['Bedwars']['kills_bedwars'])
# dont ask how long the line above took...

#structure is:
# dict(base) > dict(player) > dict(stats) > dict(gamemode)


# !gamemode userign
# store ign
# convert using \/
# https://api.mojang.com/users/profiles/minecraft/{XCRunnerS} to get UUID
# use the apikey + uuid to make a jsondump
# follow template: jsondump['player']['stats']['Bedwars']['kills_bedwars']
# cry
"""
class hypixelstats:
    def __init__(self, ign, uuid, jsondump):
        self.ign = ign
        self.uuid = uuid
        self.jsondump = jsondump

"""