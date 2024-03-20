import discord
import random

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('-hello'):
        await message.channel.send(f'Hola, soy {client.user}!, aqui está mi lista de comandos:')
        await message.channel.send('-randomnumber')
    elif  message.content.startswith('-randomnumber'):
        await message.channel.send(random.randint(-10000, 10000))
        
client.run("MTIxNzI1Njg1NDExMjE3ODIyNw.GJA19o.PpkbWe7c9K5vZxpzOTWWsQ2KsXzmebKKDh1A-A")