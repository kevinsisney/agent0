# openrouter.py - a simple client for the OpenRouter API.

import os
import aiohttp
from dotenv import load_dotenv

class OpenRouterClient:

    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("OPENROUTER_API_KEY")
        self.base_url = "https://openrouter.ai/api/v1"
        self.model = "meta-llama/llama-3.1-70b-instruct:free"
        # Initialize conversation history as an empty list
        self.conversation_history = []

    async def get_chat_response(self, message):
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "HTTP-Referer": "https://github.com/yourusername/your-repo",  # Replace with your repo
            "Content-Type": "application/json"
        }
        
        # Add the new message to conversation history
        self.conversation_history.append({"role": "user", "content": message})
        
        payload = {
            "model": self.model,
            "messages": self.conversation_history
        }

        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/chat/completions",
                headers=headers,
                json=payload
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    assistant_message = data["choices"][0]["message"]["content"]
                    # Add assistant's response to conversation history
                    self.conversation_history.append({"role": "assistant", "content": assistant_message})
                    return assistant_message
                else:
                    error_data = await response.text()
                    print(f"Error: {response.status} - {error_data}")
                    return None

    def clear_history(self):
        """Clear the conversation history"""
        self.conversation_history = []

