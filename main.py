from sportsreference.ncaab.teams import Teams
import time
import data
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext import tasks

token = data.token
client = discord.Client()


@client.event
async def on_ready():
    while True:

        channel = client.get_channel(data.channel)
        
        teamnames = []
        teamwins = []
        newarray = []

        #gathers all team names
        for team in Teams():
            teamnames.append(team.name)

        def datagather():
            for team in Teams():
                teamwins.append(team.wins)
            return teamwins

        oldarray = datagather()
        time.sleep(300)
        newarray = datagather()

        list_difference = []
        for item in oldarray:
            if item not in newarray:
                list_difference.append(item)
        
        if len(list_difference) > 0:
            location = oldarray.index(list_difference[0]) #gets position of what is different
            message = "@everyone " + teamnames[location] + " wins!"
            await channel.send(message)

client.run(token)
    
