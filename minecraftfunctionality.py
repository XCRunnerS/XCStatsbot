import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
from bot import API_KEY, DISCORD

"""
-----------------------------------------
README: CLASS INFO
        Hypixeldict{} - stores list of games, divided into subgames, divided into stats

        ign = ign - supplied by the class and the command enterer
        uuid = uuidurl['id'] - gets id from ign from mojang api
        jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8")) - loads jsondtata from hypixelapi (the stats)


        game_id = game_id - this will be gotten from the class, skywars is current 0
        current = current - this is the current page of the embed, which is ALSO used to get the current subname/subgame!, for 0 0 this would be skywars overall
        subgames = list of subgames, gotten from all the values in the game's section of hypixeldict, used for subname
        subname = current subname (name of the subgame) gotten via list of subgames at current


"""  # readme
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
              'final_kills_bedwars', 'final_deaths_bedwars', 'FK/DR'],
         },  # end of bw
    'Duels':
        {
            'overall':
                ['wins', 'losses', 'W/L', 'kills', 'deaths', 'K/D']
        }  # end of duels
}  # dictionary of gamemodes is hypixeldict{}
visualdict = {
    'SkyWars':
        {'color': discord.Color.blue(),
         'imageurl': 'https://imgur.com/BJS8r5H',
         'level': 'skywars_you_re_a_star',
         },
    'Bedwars':
        {'color': discord.Color.red(),
         'imageurl': 'https://imgur.com/ZbDcW34',
         'level' : 'bedwars_level', # these are in achivements
         },
    'Duels':
        {'color': discord.Color.gold(),
         'imageurl': 'https://imgur.com/FS5MMMt',
         'level' : '-'
         }

}  # colors and images dict, seperated for my own use

async def hypixelstats(igns, gameid, current_pages, ctxx):
    ign = igns
    game_id = gameid  # set this value in the game's class, for example 2 would be duelsnotused
    # sets the page number, configure in game's class, for example in duels, 0 would be overall
    current_page = current_pages
    ctx = ctxx
    """
    #TODO:
    rework json fetching to account for errors - done
    organize list based off of order in hypixelAPI so gameorder is obvious
    figure out how tf default dict values work or make a way to send either an error or set all stats as zero - done
    add win/losses and kds to list of stats, and then if it doesnt exist and contains a /, do something
    get rid of underscores when printing the names
    """  # todo_section


    try:
        uuidurl = json.loads(urlopen(
            f"https://api.mojang.com/users/profiles/minecraft/{ign}").read().decode("utf-8"))
        uuid = uuidurl["id"]
        pass
    except Exception:
        await ctx.send('error in fetching mojang api data')
        pass
    else:
        try:
            jsonurl = f"https://api.hypixel.net/player?key={API_KEY}&uuid={uuid}"
            jsondump = json.loads(urlopen(jsonurl).read().decode("utf-8"))
            pass
        except Exception:
            await ctx.send('error in fetching hypixel api data')
            pass
        else:
            # gets game (example: skywars)
            gamename = (list(hypixeldict.keys())[game_id])
            subgames = (hypixeldict[f'{gamename}'].keys())  # list of subgames
            subname = (list(subgames)[current_page])# gets current subgame name (example skywars: overall)
            embedcolor = (visualdict[f'{gamename}']['color'])
            embedimg = (visualdict[f'{gamename}']['imageurl'])
            try:
                levelraw = jsondump['player']['achievements'][f'{(visualdict[f"{gamename}"]["level"])}']
                embed = discord.Embed(title=(f'[{levelraw}] {jsondump["player"]["displayname"]}'),
                                      color=embedcolor)
                pass
            except:
                embed = discord.Embed(title=(f'{jsondump["player"]["displayname"]}'),
                                  color=embedcolor)
                pass
            embed.set_author(name="XStats Bot", url="https://github.com/XCRunnerS",
                             icon_url=f"{embedimg}.png")  # this is the same method as the mojang api but just the url
            embed.set_thumbnail(url=f"{embedimg}.png")
            embed.add_field(name=f'{gamename}',
                            value=f'`{subname}`', inline=False)

            gameitemindex = 0  # MAKE SURE THIS IS RESET WHEN A NEW LOOP HAPPENS
            # properly loops through items in subname
            for items in (hypixeldict[f'{gamename}'][f'{subname}']):
                try:
                    try:
                        statname = (
                            hypixeldict[f'{gamename}'][f'{subname}'][gameitemindex])
                        pass
                    except:
                        # this means something is wrong with dictionary logic... hope for not this...
                        print.send('big fuckin problem oh shit')
                        pass
                    try:
                        # stores previous value
                        currentstat = (hypixeldict[f'{gamename}'][f'{subname}'][gameitemindex])
                        gamestatname = ((f'{currentstat}').replace('_', ' ')).replace(f'{(gamename).lower()}', ' ')

                        embed.add_field(
                            name=f'{gamestatname}', value=f"`{format((jsondump['player']['stats'][f'{gamename}'][f'{currentstat}']), ',')}`", inline=True)
                        pass
                    except:
                        if statname.__contains__('/'):
                            try:
                                stattwiceremoved = (
                                    hypixeldict[f'{gamename}'][f'{subname}'][gameitemindex - 2])
                                statonceremoved = (
                                    hypixeldict[f'{gamename}'][f'{subname}'][gameitemindex - 1])

                                WLVar = (jsondump['player']['stats'][f'{gamename}'][f'{stattwiceremoved}']) /\
                                        (jsondump['player']['stats']
                                         [f'{gamename}'][f'{statonceremoved}'])
                                embed.add_field(
                                    name=f'{gamestatname}', value=f"`{format(WLVar,',.2f')}`", inline=True)
                                pass
                            except Exception:
                                await ctx.send(f'divison error for {gamestatname}')
                                pass
                        else:
                            embed.add_field(
                                name=f'{gamestatname}', value=f"`0`", inline=True)
                        pass
                except Exception:
                    embed.add_field(name=f'{gamestatname}',
                                    value=f"`0`", inline=True)
                    pass
                gameitemindex += 1  # iterate loop value
                embed.set_image(
                    url=f"https://crafatar.com/renders/body/{uuid}.png")  # full body render instead of just head
            embed.set_footer(text=f"page {current_page+1} ")
            msg = (await ctx.send(embed=embed))  # sends embed
            return msg
            # return the message I thinK????
    finally:
        print('function executed')
