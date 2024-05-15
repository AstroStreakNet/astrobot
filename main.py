import asyncio
import discord
from dotenv import load_dotenv
import os
import sys

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

intents = discord.Intents.default()
intents.typing = False
intents.presences = False
intents.messages = True

client = discord.Client(intents=intents)

async def send_to_discord_channel(message):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

async def read_file(file_path):
    try:
        with open(file_path, 'r') as f:
            f.seek(0, 2) # seek to the end of the file
            while True:
                line = f.readline()
                if not line:
                    await asyncio.sleep(0.1)  # Wait for new data
                    continue
                await send_to_discord_channel(line.strip())
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")

@client.event
async def on_ready():
    print(f'Starting the bot')
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send("Starting the bot")
    if len(sys.argv) != 2:
        print("Usage: python3 main.py /path/to/logfile.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    await read_file(file_path)

async def main():
    await client.start(TOKEN)

if __name__ == "__main__":
    asyncio.run(main())
