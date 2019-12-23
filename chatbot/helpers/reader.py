import bs4 as bs
import logging
import nltk
import re
import urllib.request
import urllib.error

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


def get_and_clean_html_data(url):
    try:
        raw_data = urllib.request.urlopen(url)
    except urllib.error.HTTPError as err:
        logger.warning(str(err))
        # TODO Set whitelist for these domains to be remove from results
        return ['*This page is forbidden*']
    raw_data = raw_data.read()
    html_data = bs.BeautifulSoup(raw_data, 'lxml')
    all_paragraphs = html_data.find_all('p')
    article_content = ""
    for p in all_paragraphs:
        article_content += p.text
    article_content = article_content.lower()
    article_content = re.sub(
        r'\[[0-9]*\]', ' ', article_content
    )
    article_content = re.sub(r'\s+', ' ', article_content)
    sentence_list = nltk.sent_tokenize(article_content)
    article_words = nltk.word_tokenize(article_content)
    return sentence_list
