# uwu
#
from urllib.request import urlopen
import json
import os
API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')
hypixeldict = {
    'SkyWars':
        {'overall':  # this isnt displayed, used to check category
             ['wins', 'losses', 'W/L', 'kills', 'deaths', 'K/D'],
         'solo':  # also known as solos, ones
             ['wins_solo', 'losses_solo', 'W/L',
              'kills_solo', 'deaths_solo', 'K/D'],
         'team':  # also known as doubles, duos, teams
             ['wins_team', 'losses_team', 'W/L',
              'kills_team', 'deaths_team', 'K/D'],
         'mega':  # WIP
             ['wins', 'losses', 'kills', 'deaths'],
         'ranked':  # aka rankedsw, ranked_normal
             ['wins_ranked', 'losses_ranked', 'kills_ranked', 'deaths_ranked']
         },  # end of sw
    'Bedwars':
        {'overall':
             ['wins_bedwars', 'losses_bedwars', 'W/L',
              'final_kills_bedwars', 'final_deaths_bedwars', 'K/D'],
         },  # end of bw
    'Duels':
        {
            'overall':
                ['wins', 'losses', 'W/L', 'kills', 'deaths', 'K/D']
        }  # end of duels
}  # dictionary of gamemodes is hypixeldict{}
visualdict = {
    'SkyWars':
        {'color': 'discord.Color.blue()',
         'imageurl': 'https://imgur.com/BJS8r5H',
         'level': 'skywars_you_re_a_star',
         },
    'Bedwars':
        {'color': 'discord.Color.red()',
         'imageurl': 'https://imgur.com/ZbDcW34',
         'level' : 'bedwars_level', # these are in achivements
         },
    'Duels':
        {'color': 'discord.Color.gold()',
         'imageurl': 'https://imgur.com/FS5MMMt',
         }

}  # colors and images dict, seperated for my own use
#   https://api.hypixel.net/player?key=86cbc8cf-c6c6-428c-a17a-c273c710485f&uuid=cffe420233a448289719f62ffcde53e4
#   testjson = json.loads(urlopen(name_link).read().decode("utf-8"))
ign = 'XCRunnerS'
game_id = 0
current_page = 0
ctx = 0

gamename = (list(hypixeldict.keys())[game_id])
subgames = (hypixeldict[f'{gamename}'].keys())  # list of subgames
subname = (list(subgames)[current_page])# gets current subgame name (example skywars: overall)
embedcolor = (visualdict[f'{gamename}']['color'])
embedimg = (visualdict[f'{gamename}']['imageurl'])

uuidurl = json.loads(urlopen(f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
uuid = uuidurl["id"]

jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))

print(jsonurl)
print(uuid)
#print(jsondump['player']['stats']['skywars'])

(visualdict[f'{gamename}']['level'])
levelraw = jsondump['player']['achievements'][f'{(visualdict[f"{gamename}"]["level"])}']
print(f'[{levelraw}] {jsondump["player"]["displayname"]}')
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