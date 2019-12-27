from googlesearch import search


class GoogleSearch:
    def get_search_result(query):
        """Returns urls which matches search query"""
        search_result_urls = list(
            search(query, tld="com", num=10, stop=9, pause=2))
        search_results = []
        for result in search_result_urls:
            search_results.append(
                dict(
                    title=" : ".join(result.split('/')[2:]),
                    url=result
                )
            )
        return search_results