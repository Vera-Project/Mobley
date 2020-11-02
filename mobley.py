#mobley, the discord music bot from the vera team

import json
import discord

# load the settings

f = open("settings.json", "r")
settings = json.load(f)
token = settings['token']
status = settings['status']
prefix = settings['prefix']

print('trying to run on token "'+token+'"')

# the discord shit

client = discord.Client()

@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')




client.run(token)
