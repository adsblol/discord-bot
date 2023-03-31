import discord
import os
import datetime
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
    if message.channel.id != 1090256133429674006:
        return
    async for m in message.channel.history(limit=100):
        if m.created_at < message.created_at - datetime.timedelta(hours=1):
            if m.pinned:
                continue
            await m.delete()

client.run(os.environ["ADSBLOL_DISCORD_BOT_TOKEN"])
