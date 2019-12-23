import os
from datetime import datetime

from chatbot.core.base import Base
from chatbot.core.reply import Reply
from chatbot.core.train import Trainer

bot = Base.create_bot()
# Trainer.train_bot(bot)

continue_discussion = True
while continue_discussion:
    user_input = input()
    user_input = user_input.lower()
    if user_input != 'bye':
        if user_input == 'thanks' or \
                user_input == 'thank you very much' or \
                user_input == 'thank you':
            continue_discussion = False
            print("Chatbot: Most welcome")
        else:
            response = Reply.get_response(bot, user_input)
            print(response)
    else:
        continue_discussion = False
        print("Chatbot: Take care, bye ..")
