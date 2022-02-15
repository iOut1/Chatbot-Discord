from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Messages import *


chatbot = ChatBot('Communicator')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

def Response(Inputs):
  Reply = chatbot.get_response(Inputs)
  return Reply
