from sportsreference.ncaab.teams import Teams
import time
import datetime
import data
import discord
from discord.ext.commands import bot
from discord.ext import commands
from discord.ext import tasks
import asyncio

token = data.token
client = discord.Client()


@client.event
async def on_ready():
    def timegrabber():
        currenttime = time.time_ns()
        return currenttime
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
        now = timegrabber()
        toggle = 0
        while toggle == 0:
            later = timegrabber()
            if later - now > 900000000000:
                print(datetime.datetime.now().strftime('%b-%d-%I%M%p-%G'))
                newarray = datagather()
                toggle = 1
        

        list_difference = []
        for item in oldarray:
            if item not in newarray:
                list_difference.append(item)
        
        if len(list_difference) > 0:
            location = oldarray.index(list_difference[0]) #gets position of what is different
            message = "@everyone " + teamnames[location] + " wins!"
            await channel.send(message)

client.run(token)
    
