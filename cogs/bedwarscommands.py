import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
from bot import API_KEY, DISCORD
from minecraftfunctionality import hypixelstats
# this is ok for apis


class Bedwarscommands(commands.Cog):


    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="bedwars", aliases=["bedwar", "bws", "bw"])
    async def bedwars(self, ctx, ign, *pg):
        #if pg:
            #await hypixelstats(ign, 1, {pg}, ctx)
        #else:
            await hypixelstats(ign, 1, 0, ctx)


    @bedwars.error
    async def bedwars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')



def setup(bot):
    bot.add_cog(Bedwarscommands(bot))

