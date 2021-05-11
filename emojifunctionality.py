"""import os
import discord
from discord.ext import commands
import asyncio
from urllib.request import urlopen
import json
from bot import API_KEY, DISCORD
from minecraftfunctionality import hypixelstats, hypixeldict, visualdict

class Emojifunctionality(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    async def reactionnav(self, igns, gameid, current_pages, ctxx, msgs):
        msg = msgs
        ign = igns
        game_id = gameid  # set this value in the game's class, for example 2 would be duelsnotused
        # sets the page number, configure in game's class, for example in duels, 0 would be overall
        current_page = current_pages

        ctx = ctxx
        buttons = [u"\u2B05", u"\u27A1", u"\uFE0F"]
        gamename = (list(hypixeldict.keys())[game_id])
        subgames = (hypixeldict[f'{gamename}'].keys())  # list of subgames
        subname = (list(subgames)[current_page])  # gets current subgame name (example skywars: overall)
        embedcolor = (visualdict[f'{gamename}']['color'])
        embedimg = (visualdict[f'{gamename}']['imageurl'])

        for button in buttons:
            await msg.add_reaction(button)

        while True:
            try:
                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in buttons


                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
            except:
                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)
                return
            else:
                previous_page = current_page
                if reaction.emoji == u"\u2B05":
                    if current_page > 0:
                        current_page -= 1

                if reaction.emoji == u"\u27A1":
                    if current_page < len(subname) - 1:
                        current_page += 1

                if reaction.emoji == u"\uFE0F":
                    emojiloop = False
                    current_page = 0
                    return

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)

                if current_page != previous_page:
                    await msg.edit()  # idfk what to do in here

def setup(bot):
    bot.add_cog(Emojifunctionality(bot))"""
