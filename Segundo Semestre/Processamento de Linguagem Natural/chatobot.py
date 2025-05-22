from collections.abc import Hashable
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
import sys
time.clock = time.perf_counter
bot = ChatBot('Bot', 
              storage_adapter='chatterbot.storage.SQLStorageAdapter',
              database_uri='sqlite:///database.sqlite3',
              logic_adapters=[
                  'chatterbot.logic.BestMatch','chatterbot.logic.MathematicalEvaluation'],)
conversa = ChatterBotCorpusTrainer(bot)
conversa.train('chatterbot.corpus.portuguese')
conversa.train('chatterbot.corpus.english')
conversa.train('chatterbot.corpus.spanish')
conversa.train('chatterbot.corpus.german')
conversa_list = ListTrainer(bot)
conversa_list.train(['Oi?','Tudo certo?','Você está bem?','Sim, obrigado.','Boa noite.', 'Para você também.',
                'Sim, gosto muito.','Acho que não.'])
while True:
    pergunta = input("Você: ")
    if pergunta.lower() == "sair":
        print("Bot: Até mais!")
        break
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else:
        print('Bot: Ainda não sei responder esta pergunta.')