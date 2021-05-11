# this is the central bot file
import os
import discord
from discord.ext import commands
import hypixel
import asyncio
from urllib.request import urlopen
import json

API_KEY = os.environ.get('HYPIXEL_API')
DISCORD = os.environ.get('DISCORD_KEY')
# testing git changes

bot = commands.Bot(command_prefix=['.', 'h!'])


for extension in os.listdir('./cogs'):
    if extension.endswith('.py'):
        bot.load_extension("cogs." + extension[:-3])
# all my commands are in ./cogs/filename.py :) [prefix]help will show you in discord

# prints bot message in console


@bot.event
async def on_ready():
    print('Bot Ready')
    await bot.wait_until_ready()
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='XStats || h!'))
    channel = bot.get_channel(804132338438766613)
    await channel.send('👀')

# 376900391440220174

# non-existing commands


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('command does not exist, type `.help` for a list of commands!')

bot.run(f'{DISCORD}')
