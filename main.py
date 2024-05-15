
import asyncio
import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Starting the bot')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Starting the bot")

async def send_to_discord_channel(message):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

async def read_logs():
    with open('logfile_pipe', 'r') as logfile:
        while True:
            line = logfile.readline().strip()
            if line:
                await send_to_discord_channel(line)

async def main():
    await client.start(TOKEN)
    await client.wait_until_ready()
    await read_logs()

if __name__ == "__main__":
    asyncio.run(main())

