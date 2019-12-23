import logging

from chatterbot import ChatBot

logging.basicConfig(level=logging.INFO)

logic_adapters = [
    {
        'import_path': 'chatterbot.logic.BestMatch',
        'default_response': 'I am sorry, but I do not understand.',
        'maximum_similarity_threshold': 0.90
    },
    {
        'import_path': 'google_adapter.GoogleLogicAdapter'
    }
]


class Base:
    @classmethod
    def create_bot(cls):
        bot = ChatBot(
            "Info Bot",
            storage_adapter="chatterbot.storage.SQLStorageAdapter",
            logic_adapters=logic_adapters
        )
        return bot
