import os

import discord
import coinbase
from dotenv import load_dotenv

#qqch dans les parenthèses de laod_dotenv() car le fichier s'appelle pas '.env' comme c'est le cas
#par défaut car ici c'est le nom de l'env virtuel donc on l'appelle config (il comprend que le fichier
#est dans le fichier courant -> permet de pas déployer le fichier config sur git et donner l'accès au bot
load_dotenv(dotenv_path="config")
default_intents = discord.Intents.default()
default_intents.members = True

client = discord.Client(intents=default_intents)

@client.event
async def on_ready():
    print("Le bot est prêt.")

@client.event
async def on_message(message):
    if message.content.lower() == "ping":
        await message.channel.send("pong", delete_after=5)
    if message.content.startswith("!del"):
        number = int(message.content.split()[1])
        messages = await message.channel.history(limit=number+1).flatten()

        for each_message in messages:
            await each_message.delete()

@client.event
async def on_member_join(member):
    general_channel: discord.TextChannel = client.get_channel(850376716933267498)
    await general_channel.send(content=f"Bienvenue sur le serveur {member.display_name} !")

#Récupère la variable d'env qui est accède au fichier config
client.run(os.getenv("TOKEN"))


