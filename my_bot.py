import discord

TOKEN = 'NDU5ODEyNDMzMTQ2NTQ0MTI4.Dg7pjQ.Dwuyze9_ZCqYDAEz8YuaEsmxx6Q'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!Hello') or message.content.startswith('!hello'):
        msg = 'Greetings Master {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)

    elif message.content.startswith('!James'):
        msg = 'You rang Master {0.author.mention}?'.format(message)
        await client.send_message(message.channel, msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)