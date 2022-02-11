from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from Messages import Inputs


chatbot = ChatBot('Communicator')
trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train("chatterbot.corpus.english")

chatbot.get_response(Inputs)