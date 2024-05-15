from dotenv import load_dotenv
import discord
import asyncio
import os

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
CHANNEL_ID = int(os.getenv('DISCORD_CHANNEL_ID'))

client = discord.Client()

async def send_to_discord_channel(message):
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(message)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

async def read_logs():
    with open('some/log/file', 'r') as logfile:
        while True:
            line = logfile.readline().strip()
            if line:
                await send_to_discord_channel(line)
            else:
                await asyncio.sleep(0.1)

async def main():
    await client.wait_until_ready()
    await read_logs()

client.loop.create_task(main())
client.run(TOKEN)

