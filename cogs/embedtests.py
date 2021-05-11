import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
from bot import API_KEY, DISCORD
from minecraftfunctionality import hypixelstats


# from emojifunctionality import Emojifunctionality
# import hypixeltemplates
# this is decent
# if this gets fucked up use bedwars as a backup


class EmbedTests(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="embed", aliases=["eb", "nbd", "ebd"])
    async def embed(self, ctx):

        # list of pages
        page1 = discord.Embed(title="Bot 1", description="Page 1")
        page2 = discord.Embed(title="Bot 2", description="Page 2", color=discord.Color.blue())

        commands.pages_embedtests = [page1, page2] # makes list of what I need

        buttons = [u"\u2B05", u"\u27A1"]  # left, right
        current = 0 # current page will be changeable
        msg = await ctx.send(embed=commands.pages_embedtests[current])
        # send first message (idk if I will need to change this)

        for button in buttons:
            await msg.add_reaction(button)

        while True:

            try:

                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in buttons

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                #print('check passed')

            except:
                for button in buttons:
                    await msg.clear_reactions()
            # then check if:
            # person reacting is the same as original sender
            # reaction is on the right message
            # reaction is in list

            # logic for switching tabs
            else:
                previous = current
                if reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1

                if reaction.emoji == u"\u27A1":
                    if current < len(commands.pages_embedtests) - 1:
                        current += 1

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)
                #print('all reactions removed')

                if current != previous:
                    await msg.edit(embed=commands.pages_embedtests[current])
        # emoji navigation

    """    # Get skywars stats
        @commands.command(name="skywars", aliases=["skywar", "skw", "sw", 's'])
        async def skywars(self, ctx, ign, *pg):
            await hypixelstats(ign, 0, 0, ctx)
            # await reactionnav(ign, 0, 0, ctx, ())
            # emoji logic will go here, need message returned from ^

        # Embed Pages prototype"""



def setup(bot):
    bot.add_cog(EmbedTests(bot))
