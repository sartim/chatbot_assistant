from chatterbot.trainers import ChatterBotCorpusTrainer


class Trainer:
    @classmethod
    def train_bot(cls, bot):
        trainer = ChatterBotCorpusTrainer(bot)
        trainer.train(
            "chatterbot.corpus.english",
            "chatterbot.corpus.english.greetings",
            "chatterbot.corpus.english.conversations"
        )
