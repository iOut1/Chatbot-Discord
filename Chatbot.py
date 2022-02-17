from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

#Creates a chatbot but and trains it in English#
chatbot = ChatBot('Communicator')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

#Creates a function to truly communicate with chatbot#
def Response(Inputs):
  Reply = chatbot.get_response(Inputs)
  return Reply
