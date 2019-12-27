import wikipedia


class WikipediaSearch:
    @staticmethod
    def get_summary(input_statement):
        wiki = wikipedia.page(input_statement)
        return wiki.summary

    @staticmethod
    def get_categories(input_statement):
        wiki = wikipedia.page(input_statement)
        return wiki.categories
