# discord.py - the Discord bot itself.

import os
import discord
from discord.ext import commands
from openrouter import OpenRouterClient

# The channel the bot will communicate on.
CHANNEL_ID = int(os.getenv("CHANNEL_ID", 0))

# Initialize Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Initialize OpenRouter client
openrouter_client = OpenRouterClient()


@bot.event
async def on_ready():
    print(f"{bot.user} has connected to Discord!")
    channel = bot.get_channel(CHANNEL_ID)
    if not channel:
        print("Channel not found.")
    else:
        await channel.send("Hello!")


@bot.event
async def on_message(message):
    # Ignore messages from the bot itself
    if message.author == bot.user:
        return

    # You can check for specific channels here
    if message.channel.id == CHANNEL_ID:
        print(f'New message in monitored channel: {message.content}')
        channel = bot.get_channel(CHANNEL_ID)
        await channel.send(f"This channel is for bots only, {message.author.name}!")
        # Add your notification logic here
    
    # This line is necessary if you want to process commands as well
    await bot.process_commands(message)


@bot.command(name="chat")
async def chat(ctx, *, message):
    """Chat with the AI assistant"""
    async with ctx.typing():
        try:
            response = await openrouter_client.get_chat_response(message)
            
            # Split response if it's too long for Discord
            if len(response) > 2000:
                chunks = [response[i:i + 2000] for i in range(0, len(response), 2000)]
                for chunk in chunks:
                    await ctx.send(chunk)
            else:
                await ctx.send(response)
                
        except Exception as e:
            await ctx.send(f"An error occurred: {str(e)}")
