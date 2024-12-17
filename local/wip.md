
# To Do


- Automatically select a free model from OpenRouter and use it. If model returns HTTP 429 (throttled) or out of credit, try the next one.
- Fix bot conversation history, tracking this differently now...
- Prompt to set both personality
- Use tool to search the web
- Use tool to send messages deciding whether or not to respond at all.



# To create private bot in Discord
- Had to set instlall link under the bot in the discord developer to None


# To get this working I had to
- Enable intents for the bot:  Presence, Server Members, Message Content intents.
- Generate an OAuth link with scope bot and open the URL to invidate the bot to the server.

# Use context with Docker to deploy bot to server.