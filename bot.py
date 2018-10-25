
import asyncio
import time
import sys
import os

import discord
import youtube_dl

from opus_loader import load_opus_lib
import constants

TOKEN = 'NTAzMTcyNDY3NjI4NTcyNjcy.DqynmA.BYrf_t4wtQV8emw0UoTS_hQhj1g'
#bot id: 

client = discord.Client()
load_opus_lib()


@client.event
async def on_message(message):
    author = message.author
    voice_channel = author.voice_channel   
    
    # we do not want the bot to reply to itself
    if author == client.user:
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
    
    '''if message.content.startswith('!join'):
        await voice
        msg = 'Joining Voice Lobby'
        msg.format(message)
        await client.send_message(message.channel, msg)
        print("Connected to Voice Channel")'''

    if message.content.startswith('!jockbutt'):
        msg = ':flag_us: playing *American Jock Butt* :flag_us: '
        msg.format(message)
        await client.send_message(message.channel, msg)
        voice = await client.join_voice_channel(voice_channel)
        player = await voice.create_ytdl_player("https://www.dropbox.com/s/41cui25bgw3iwbw/American%20Jock%20Butt.mp3")
        player.start()
        time.sleep(13)
        player.stop()
        await client.disconnect() # dont work


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
