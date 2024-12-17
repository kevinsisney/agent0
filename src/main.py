# main.py - the main entry point for the bot.

import argparse
import asyncio
import os

from dotenv import load_dotenv

from discord_bot import bot
from sandbox import chat_loop

load_dotenv()

def parse_args():
    parser = argparse.ArgumentParser(description='Run Discord bot or sandbox chat interface')
    parser.add_argument('--sandbox', action='store_true', help='Run in sandbox mode instead of Discord bot mode')
    return parser.parse_args()

def main():
    load_dotenv()
    args = parse_args()

    if not os.getenv("OPENROUTER_API_KEY"):
        print("❌ Error: OPENROUTER_API_KEY not found in environment variables")
        return
    
    if args.sandbox:
        print("Starting in sandbox mode...")
        asyncio.run(chat_loop())
    else:
        print("Starting Discord bot...")
        if not os.getenv("DISCORD_TOKEN"):
            print("❌ Error: DISCORD_TOKEN not found in environment variables")
            return
        bot.run(os.getenv("DISCORD_TOKEN"))

if __name__ == "__main__":
    main() 