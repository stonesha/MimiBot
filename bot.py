
import discord
import sys
import youtube_dl

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

    if message.content.startswith('!jockbutt'):
        msg = ':flag_us: playing *American Jock Butt* :flag_us: '
        msg.format(message)
        await client.send_message(message.channel, msg)
        author = message.author
        voice_channel = author.voice_channel
        voice = await client.join_voice_channel(voice_channel)
        player = await voice.create_ffmpeg_player('American Jock Butt.mp3')
        player.start()
        if player.is_done() == True:
            player.stop()
            client.disconnect


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)