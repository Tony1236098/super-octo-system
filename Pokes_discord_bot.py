import discord
from discord.ext import commands
import requests as r


TOKEN = 'Your own code :)'
PREFIX = "!"
BANNEND_WORDS = [
    "pizza hawaii",
    "chocolate pizza",
    "pineapple pizza",
    "scriptie",
    "marc rutte",
    "hugo de jonge"

]

KAN_ECHT_NIET = [
    "pokemon is a bad anime",
    "crucio",
    "poke has small pipie",
    "valorant"

]

intents = discord.Intents.default()
intents.members = True
# Roep de bot
# client = discord.Client(intents=intents)
client = commands.Bot(intents=intents, command_prefix=PREFIX)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")


@client.command()
async def Poke(context):
    await context.message.reply("Ewa Niffo")


@client.command()
async def cat(context):
    req = r.get("https://api.thecatapi.com/v1/images/search")
    res = req.json()
    await context.message.reply(res[0]["url"])


@client.command()
async def coffee(context):
    req = r.get("https://coffee.alexflipnote.dev/random.json")
    res = req.json()
    await context.message.reply(res["file"])


@client.command()
async def noris(context):
    req = r.get("https://api.chucknorris.io/jokes/random")
    res = req.json()
    await context.message.reply(res["value"])

@client.command()
async def dog(context):
    req = r.get("https://dog.ceo/api/breeds/image/random")
    res = req.json()
    await context.message.reply(res["message"])

@client.command()
async def poke(context, argument):

    msg = ""
    req = r.get(f"https://pokeapi.co/api/v2/pokemon/{argument}")
    res = req.json()

    msg += f"{res['name'].title()}:\n"
    types = res["types"]
    for tp in types:
        msg += f"Type {tp['slot']}: {tp['type']['name'].title()}\n"

    stats = res["stats"]
    for st in stats:
        msg += f"{st['stat']['name'].title()}: {st['base_stat']}\n"

    await context.message.reply(msg)

@client.command()
async def mock(context, *argument):
    arg = "_".join(argument)
    await context.message.reply(f"https://mockingspongebob.org/{arg}.jpg")


@client.event
async def on_member_join(member):
    guild = member.guild
    if guild.system_channel is not None:
        res = f"Welkom {member.mention} in de {guild.name} server!"
        await guild.system_channel.send(res)


@client.event
async def on_message(message):
    if message.author.id == client.user.id:
        return

    for woord in BANNEND_WORDS:
        if woord in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention} das pech bericht weg to much of a small pipie")

    for woord in KAN_ECHT_NIET:
        if woord in message.content.lower():
            await message.delete()
            await message.channel.send("YEET")
            await message.author.ban()

    await client.process_commands(message)


# run de bot
client.run(Token)
