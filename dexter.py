import discord
import asyncio
import random
import datetime
from discord.ext.commands import Bot
from discord.ext import commands
import keys #File that contains the bot's token
import pokedex_database

class Bot(discord.Client):
    async def on_ready(self):
        '''Similar to __init__ for Bot'''
        print("ONLINE")
        self.pokedex = pokedex_database.PokedexDatabase()
        await client.change_presence()
    
    async def on_message(self, message):
        '''Handles message input'''
        if message.content.lower() == "hello dexter" or message.content.lower() == "hi dexter":
            await message.channel.send("<@{}> Hello!".format(message.author.id))

        if message.content.lower() == "!ping":
            await message.channel.send("<@{}> Pong!".format(message.author.id))

        if message.content.lower().startswith("!entry "):
            try:
                dexNum = int(message.content.lower().split()[1])
                data = self.pokedex.get_entry(dexNum)
                await message.channel.send(f"Pokédex Entry #{data[0]}: {data[1]}\n{data[2]}")

            except ValueError:
                await message.channel.send("ERROR: Invalid Dex Number!")

            except TypeError:
                await message.channel.send("ERROR: Dex Number Out Of Range!")

        


if __name__ == "__main__":
    client = Bot()
    client.run(keys.TOKEN)
