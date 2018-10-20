# Work with Python 3.6
import discord

TOKEN = 'NTAzMTcyNDY3NjI4NTcyNjcy.DqynmA.BYrf_t4wtQV8emw0UoTS_hQhj1g'

client = discord.Client()

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

    if message.content.startswith('!stop'):
        msg = 'Stopping...'
        msg.format(message)
        await client.send_message(message.channel, msg)
        exit(0)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)