import os

from dotenv import load_dotenv

from discord.ext import commands

load_dotenv(dotenv_path="config")

#Permet de mieux gérer le code et de ne pas à avoir à mettre les identifier
class DocBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="/")

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté au serveur.")

doc_bot = DocBot()
doc_bot.run(os.getenv("TOKEN"))