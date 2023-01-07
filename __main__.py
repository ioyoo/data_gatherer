from .src.reddit_scrapper import RedditCrawler
from .src.data.credentials import RedditCredentials, RedditData, APICredentials
from .src.reddit_analysis import RedditAnalysis
from .src.post_agent import PostAgent
import time


def main():
    cred = RedditCredentials()
    rd = RedditData()
    api = APICredentials()
    reddit = RedditCrawler(cred.CLIENT_AUTH2, cred.SECRET, cred.USER_AGENT)
    start_time = time.time()
    posts = reddit.get_info_from(
        stock_names=rd.get_top100(), subreddits=rd.CHANNELS, limit=20)
    redditAnalysis = RedditAnalysis()
    results = redditAnalysis.run_analysis(posts)
    print("--- %s seconds ---" % (time.time() - start_time))
    agent = PostAgent(api.PATH)
    agent.post(results)


if __name__ == "__main__":
    main()
