from .src.reddit_scrapper import RedditCrawler
from .src.data.credentials import RedditCredentials, RedditData, APICredentials
from .src.reddit_analysis import RedditAnalysis
from .src.post_agent import PostAgent
from .src.stock_worder import StockKeyworder
import time


def main():

    # Initialize Instances
    cred = RedditCredentials()
    rd = RedditData()
    api = APICredentials()
    keyworder = StockKeyworder()
    redditAnalysis = RedditAnalysis()
    # start timer
    start_time = time.time()
    # get keywords
    keywords = keyworder.get_dict_keywords(rd.get_top100())
    # get info
    reddit = RedditCrawler(cred.CLIENT_AUTH2, cred.SECRET, cred.USER_AGENT)
    posts = reddit.get_info_from(
        stock_keywords=keywords, subreddits=rd.CHANNELS, filter="day")
    # run analysis
    results = redditAnalysis.run_analysis(posts)
    # get time
    print("--- %s seconds ---" % (time.time() - start_time))
    # post results
    agent = PostAgent(api.PATH)
    agent.post(results)


if __name__ == "__main__":
    main()
