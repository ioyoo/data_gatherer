from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from .tools.reddit_sentimental_words import REDDIT_WORDS


class RedditAnalysis:
    def __init__(self) -> None:
        self.results = {}

    def run_analysis(self, posts: dict):
        analyzer = SentimentIntensityAnalyzer()
        analyzer.lexicon.update(REDDIT_WORDS)

        for key, post_list in posts.items():
            for post in post_list:
                self.sentiment_analyzer_scores(
                    key, post['text'], post['upvotes'], post['downvotes'], analyzer)
            self.results[key] /= len(post_list)

        return self.results

    def sentiment_analyzer_scores(self, key, text, upvotes, downvotes, analyzer: SentimentIntensityAnalyzer):
        score = analyzer.polarity_scores(text)
        try:
            self.results[key] = self.results[key] + \
                self.get_comment_value(score, upvotes, downvotes)
        except KeyError:
            self.results[key] = self.get_comment_value(
                score, upvotes, downvotes)

    def get_comment_value(self, score, upvotes, downvotes):
        score.popitem()
        max_value = max(score.values())
        max_key = max(score, key=score.get)
        match max_key:
            case 'neg':
                return -max_value + (0.1 * upvotes) - (0.1 * downvotes)
            case 'neu':
                return (0.5 * max_value) + (0.2 * upvotes) - (0.2 * downvotes)
            case 'pos':
                return max_value + (0.1 * upvotes) - (0.1 * downvotes)
