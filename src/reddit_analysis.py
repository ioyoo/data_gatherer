from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class RedditAnalysis:
    def __init__(self) -> None:
        self.results = {}
        self.stock_count = {}
        
    def run_analysis(self, dict):
        analyzer = SentimentIntensityAnalyzer()

        for sentence in dict:
            self.sentiment_analyzer_scores(dict[sentence], analyzer)
        
        for key in dict.keys():
            test = dict.get(key)
            try:
                self.stock_count[test['name']] = self.stock_count[test['name']] + 1
            except KeyError:
                self.stock_count[test['name']] = 1

        for key, value in self.results.items():
            value = value / self.stock_count.get(key)
            self.results[key] = value

        print(self.results)
        return self.results

    def sentiment_analyzer_scores(self, values, analyzer: SentimentIntensityAnalyzer):
        score = analyzer.polarity_scores(values['text'])
        try:
            self.results[values['name']] = self.results[values['name']] + self.get_comment_value(score, values)
            #self.stock_count.append(values['name'])
        except KeyError:
            self.results[values['name']] = self.get_comment_value(score, values)
            #self.stock_count.append(values['name'])
    
    def get_comment_value(self, score, values):
        score.popitem()
        max_value = max(score.values())
        max_key = max(score, key=score.get)
        match max_key:
            case 'neg':
                return -max_value + (0.1 * values['upvotes']) - (0.1 * values['downvotes'])
            case 'neu':
                return (0.5 * max_value) + (0.2 * values['upvotes']) - (0.2 * values['downvotes'])
            case 'pos':
                return max_value + (0.1 * values['upvotes']) - (0.1 * values['downvotes'])
