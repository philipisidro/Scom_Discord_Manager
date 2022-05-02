import discord
from discord.ext import commands
import os

import settings

intents = discord.Intents.default()

cogs: list = ["modules.roleReactionManager"]

client = commands.Bot(command_prefix=settings.Prefix, help_command=None, intents=intents)

@client.event
async def on_ready():
    print(f"Bot is now running")
    # await client.change_prescenece(status=discord.Status.online, activity=discord.Game(settings.BotStatus))
    for cog in cogs:
        try:
            print(f"Loading module {cog}")
            client.load_extension(cog)
            print(f"Loaded module {cog}")
        except Exception as e:
            exc = "{}: {}".format(type(e).__name__, e)
            print("Failed to load cog {}\n{}".format(cog, exc))

my_secret = os.environ["TOKEN"]
client.run(my_secret)