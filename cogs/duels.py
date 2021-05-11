# https://imgur.com/FS5MMMt.png : game logo
# YELLOW                        : color
# stats to get:
# duels
import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json
from bot import API_KEY, DISCORD
from minecraftfunctionality import hypixelstats


class Duels(commands.Cog):


    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="duels", aliases=["duel", "1v1", "ds"])
    async def duels(self, ctx, ign, *pg):
        # if pg:
        # await hypixelstats(ign, 1, {pg}, ctx)
        # else:
        await hypixelstats(ign, 2, 0, ctx)


    @duels.error
    async def bedwars_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')



def setup(bot):
    bot.add_cog(Duels(bot))

