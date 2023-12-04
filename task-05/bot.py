
import discord
import os
import requests

from bs4 import BeautifulSoup
from discord.ext import commands
from dotenv import find_dotenv, load_dotenv
from scraper import score, resultant, generator, upcoming

class MyHelpCommand(commands.DefaultHelpCommand):
    async def send_command_help(self, command):
        pass

intents = discord.Intents.all()
client = commands.Bot(command_prefix='/', intents=intents, help_command=MyHelpCommand())
path = find_dotenv()
load_dotenv(path)
token = os.getenv("token")

@client.event
async def on_ready():
    print('ready...')

@client.command(help = 'Say hello to Crickey')
async def hello(ctx):
    await ctx.send("Hey I'm Crickey, how can I help you?")


@client.command(help = 'Live Cricket score')
async def livescore(ctx):
    url = "https://www.espncricinfo.com/live-cricket-score"
    src = requests.get(url)
    src.raise_for_status()
    parse = BeautifulSoup(src.text, 'html.parser')

    header = parse.find('div', class_="ds-flex ds-justify-between ds-items-center")
    status = header.find('span', class_="ds-text-tight-xs ds-font-bold ds-uppercase ds-leading-5").text

    if status not in ['Live', 'Innings break', 'Drinks', 'Tea break', 'Lunch']:
        await ctx.send("Match data currently unavailable!\n")
        await ctx.send(status)


@client.command(help = 'Gives the result of a match')
async def result(ctx):
    result = resultant()

    for key, value in result.items():
        print(f'{key}: {value}')


@client.command(help = 'Generates a .csv file of the live match score')
async def generate(ctx):
    generator()

@client.command(help = "Fetches data of the upcoming cricket match")
async def upcoming(ctx):
    result = upcoming()
    for i in result:
        print(i)


client.run(token)


