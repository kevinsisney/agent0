# sandbox.py - A simple CLI chat interface for testing the bot.

import asyncio
import os
from dotenv import load_dotenv
from openrouter import OpenRouterClient

async def chat_loop():

    client = OpenRouterClient()
    print("Sandbox Chat Interface")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type your message and press Enter:")
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() in ['/exit', '/quit']:
            print("\nGoodbye! 👋")
            break
            
        if not user_input:
            continue
            
        print("\nBot: ", end="", flush=True)
        response = await client.get_chat_response(user_input)
        print(response)

def main():
    load_dotenv()
    if not os.getenv("OPENROUTER_API_KEY"):
        print("❌ Error: OPENROUTER_API_KEY not found in environment variables")
        return
        
    asyncio.run(chat_loop())

if __name__ == "__main__":
    main() 