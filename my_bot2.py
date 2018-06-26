import random
# import fortnite_tracker as ftn

from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = ("!", "?")
TOKEN = 'NDU5ODEyNDMzMTQ2NTQ0MTI4.Dg7pjQ.Dwuyze9_ZCqYDAEz8YuaEsmxx6Q'

client = Bot(command_prefix=BOT_PREFIX)


@client.command(name='WillIwin', pass_context=True)
async def random_ans(context):
    possible_responses = [
        'Perhaps',
        'Quite possibly',
        'Most certainly!',
        'Absolutely not!',
        "I don't see why not",
    ]
    await client.say(random.choice(possible_responses) + ", " + context.message.author.mention)


@client.command(name='Whosthebest', pass_context=True)
async def imthebest(context):
    await client.say("Clearly that's you, " + context.message.author.mention)


@client.command(name='hello', pass_context=True, aliases=['Hello', ' hello', ' Hello'])
async def hello(context):
    await client.say("Greetings, " + context.message.author.mention)


@client.command(name='ftn', pass_context=True, aliases=['fortnite'])
async def ftn_stats(context):
    await client.say("Greetings, " + context.message.author.mention)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="mit deiner Mutter"))
    print("Logged in as " + client.user.name)

client.run(TOKEN)
