# Given a ticker this file should perform operations shouls as return a set of words based on that
# and  any other information needed from the ticker symbol or a stock name.

import nltk
import requests
from nltk.tokenize import word_tokenize
from .tools.text_tools import only_letters, STOPWORDS
# Run once
# nltk.download('all')


class StockKeyworder:

    def __init__(self) -> None:
        try:
            nltk.data.find('tokenizers/punkt')
        except LookupError:
            nltk.download('all')

    def get_keywords(self, ticker):
        
        
        tokens = word_tokenize(c_info)
        pos_tags = nltk.pos_tag(tokens)

        keywords = [
            *set([word for word, pos in pos_tags if pos in ['NNP'] and only_letters(word.lower(), "+") not in STOPWORDS])]
        keywords.append(ticker)
        return keywords

    def get_dict_keywords(self, tickers):
        ticker_dict = {}
        for ticker in tickers:
            ticker_dict[ticker] = self.get_keywords(ticker)
        return ticker_dict
