
import discord
import sys


import asyncio
import time

from opus_loader import load_opus_lib

TOKEN = 'NTAzMTcyNDY3NjI4NTcyNjcy.DqynmA.BYrf_t4wtQV8emw0UoTS_hQhj1g'

client = discord.Client()
load_opus_lib()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!hi'):
        msg = 'Hi {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!meow'):
        msg = 'Meow! {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    if message.content.startswith('!stop'):
        msg = 'Stopping...'
        msg.format(message)
        await client.send_message(message.channel, msg)
        await client.logout()
        print("Stopping program")

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)