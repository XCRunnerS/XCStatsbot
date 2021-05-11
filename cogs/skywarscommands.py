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

    # Embed Pages prototype

    @commands.command(name="embed", aliases=["eb", "nbd", "ebd"])
    async def embed(self, ctx):

        # list of pages
        page1 = discord.Embed(title="Bot 1", description="Page 1")
        page2 = discord.Embed(
            title="Bot 2", description="Page 2", color=discord.Color.blue())

        commands.skywars_pages = [page1, page2]

        buttons = [u"\u2B05", u"\u27A1"]  # left, right
        current = 0
        msg = await ctx.send(embed=commands.skywars_pages[current])

        # I need to: (add the reactions)
        for button in buttons:
            await msg.add_reaction(button)
            # works up to here ^^^^

        while True:

            try:

                def check(reaction, user):
                    return user == ctx.author and str(reaction.emoji) in buttons

                reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)
                print('check passed')
                """
                def check(reaction, user):
                            return user == ctx.author and str(reaction.emoji) == '👍'
                
                        try:
                            reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                        except asyncio.TimeoutError:
                            await channel.send('👎')
                        else:
                            await channel.send('👍')
                
                """
            except:
                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)
                return

        # then check if:
        # person reacting is the same as original sender
        # reaction is on the right message
        # reaction is in list

        # logic for switching tabs
            else:
                print("entered else")
                previous = current
                print(current)
                print(previous)
                if reaction.emoji == u"\u2B05":
                    if current > 0:
                        current -= 1
                        print('left emoji')
                        print(current)
                        print(previous)

                if reaction.emoji == u"\u27A1":
                    if current < len(commands.skywars_pages)-1:
                        current += 1
                        print('right emoji')
                        print(current)
                        print(previous)

                for button in buttons:
                    await msg.remove_reaction(button, ctx.author)
                    print('reaction removed')
                    print(current)
                    print(previous)
                print('all reactions removed')

                if current != previous:
                    print('entered into loop to reset')
                    print(current)
                    print(previous)
                    await msg.edit(embed=commands.skywars_pages[current])
                    print(current)
        # emoji navigation

    @skywars.error
    async def skywar_serror(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')

    @commands.command(name="rating", aliases=["rsw", "rs", "ranked", "badgame", 'r'])
    async def rating(self, ctx, ign):
        await hypixelstats(ign, 0, 4, ctx)

    @rating.error
    async def rating_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('missing arguments! please follow this context:\n`!command ign`')


def setup(bot):
    bot.add_cog(Skywarscommands(bot))
