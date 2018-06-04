from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import os

bot = ChatBot('Test')

bot.set_trainer(ListTrainer)

for _file in os.listdir('file'):
    chats = open('file/' + _file, 'r').readlines()

    bot.train(chats)

while True:
      request = input('You:')
      response = bot.get_response(request)
   
      print('SmartBot:' ,response)
