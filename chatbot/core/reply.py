from chatbot.core.base import Base


class Reply(Base):
    @classmethod
    def get_response(cls, bot, text):
        response = bot.get_response(text)
        return response
