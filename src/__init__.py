from reddit_scrapper import RedditCrawler
from data.data import RedditCredentials, RedditData
from reddit_analysis import RedditAnalysis
import time


def main():
    cred = RedditCredentials()
    rd = RedditData()
    reddit = RedditCrawler(cred.CLIENT_AUTH2, cred.SECRET, cred.USER_AGENT)
    start_time = time.time()
    dict = reddit.get_info_from(
        stock_names=rd.KEYWORDS, subreddits=rd.CHANNELS, limit=20)
    redditAnalysis = RedditAnalysis()
    redditAnalysis.run_analysis(dict=dict)
    print("--- %s seconds ---" % (time.time() - start_time))
    print("Well thats a wrap")


if __name__ == "__main__":
    main()
