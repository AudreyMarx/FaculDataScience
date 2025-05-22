from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import time
import sys
time.clock = time.perf_counter

bot = ChatBot('Bot')
conversa = ListTrainer(bot)
conversa.train(['Oi?','Tudo certo?','Você está bem?','Sim, obrigado.','Boa noite.', 'Para você também.',
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
        print('Bot: Não compreendo')
    