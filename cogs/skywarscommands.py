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


class Skywarscommands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Get skywars stats
    @commands.command(name="skywars", aliases=["skywar", "skw", "sw", 's'])
    async def skywars(self, ctx, ign, *pg):
        await hypixelstats(ign, 0, 0, ctx)

        #await reactionnav(ign, 0, 0, ctx, ())
        # emoji logic will go here, need message returned from ^


    @skywars.error
    async def skywar_serror(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')

    @commands.command(name="ranked", aliases=["rsw", "rs", "rankedsw", "badgame", 'r'])
    async def ranked(self, ctx, ign):
        await hypixelstats(ign, 0, 4, ctx)

    @ranked.error
    async def ranked_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')


def setup(bot):
    bot.add_cog(Skywarscommands(bot))
