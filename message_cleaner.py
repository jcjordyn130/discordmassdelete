import discord
import asyncio
import json
import sys
import time

client = discord.Client()
with open("config.json", "r") as handle:
    config = json.load(handle)
    token = (config["token"])
    if token == "Token_Here":
        print ("You Haven't set up the config.json. Please set it up and then run the program again.")
        time.sleep(5)
        sys.exit()
    cleanphrase = (config["cleanphrase"])
    print ("Logging in with token: " + str(token))
    print ("The selected cleanphrase is " + str(cleanphrase))

@client.event
async def on_message(message):
    counter = 0
    if message.content.startswith(str(cleanphrase)) and message.author == client.user:
        activationchannel = message.channel.name
        activationguild = message.guild.name
        print(f"#### Receieved clean command for {message.channel.name} in guild {message.guild.name} ####")
        async for delete_message in message.channel.history(limit = 99999):
            if delete_message.author == client.user:
                counter += 1
                await delete_message.delete()
                print(f"{counter}")
                #await asyncio.sleep(1)
        msg = f"#### Cleaned {counter} messages for {activationchannel} in {activationguild} ####"
        print(msg)

client.run(token, bot = False)
