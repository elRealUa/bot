import discord
import random
import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
TOKEN = ''

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('-hola'):
        await message.channel.send(f'Hola, soy {client.user}!, aqui está mi lista de comandos:')
        await message.channel.send('-numero')
        await message.channel.send('-hora')
    elif  message.content.startswith('-numero'):
        x = random.randint(-10000, 10000)
        await message.channel.send(f'El número generado es: {x}')
    elif message.content.startswith('-hora'):
        hora = datetime.datetime.now()
        horaA = hora.strftime('La hora actual es: %H: %M: %S')
        await message.channel.send(horaA)

        
client.run(TOKEN)
