import wikipedia
from chatterbot.conversation import Statement
from chatterbot.logic import LogicAdapter

from chatbot.helpers.wikipedia_search import WikipediaSearch


class GoogleLogicAdapter(LogicAdapter):
    def can_process(self, statement):
        return True

    def process(
            self, input_statement,
            additional_response_selection_parameters=None):
        import random
        search_result = WikipediaSearch.get_summary(input_statement)
        confidence = random.uniform(0, 1)
        selected_statement = Statement(
            text=search_result, in_response_to=input_statement,
            confidence=1
        )
        selected_statement.confidence = confidence
        return selected_statement
