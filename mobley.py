#mobley, the discord music bot from the vera team

import json
import discord

# load the settings

f = open("settings.json", "r")
settings = json.load(f)
token = settings['token']
webhook_url = settings['webhook']
status = settings['status']
prefix = settings['prefix']
