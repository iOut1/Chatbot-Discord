import discord
from Chatbot import Response
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

client = discord.Client()

# Tells that it the bot has signed in#
@client.event()
async def on_ready():
  print("We have logged in as {0.user}".format(client))

# Checks newest message, checks if that message was sent by it. Then makes the chatbot send a response#
@client.event()
async def on_message(message):
  if message.author == client.user:
    return
  else:
    await message.channel.send(Response(message))
     
