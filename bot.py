import discord
from discord.ext import commands
import random
import requests
import asyncio
import json

command_prefix='$furrito '
bot = commands.Bot(command_prefix)

word_site = "http://svnweb.freebsd.org/csrg/share/dict/words?view=co&content-type=text/plain"
response = requests.get(word_site)

@bot.command(pass_context=True)
async def rnick(ctx, member : discord.Member, silent : int = 1):
    counter, runs = 0, 90
    old_nick = member.display_name
    while True:
        new_nick = random.choice(response.content.splitlines()).decode("utf-8")
        if silent == 0:
            await ctx.send(str(member.name) + " "+ " is now " + new_nick)
        await member.edit(nick = new_nick)
        counter += 1
        if (counter) >= runs:
            break
        await asyncio.sleep(10)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

with open("./token.json") as json_data:
    table = json.load(json_data)
    bot.run(table["token"])
