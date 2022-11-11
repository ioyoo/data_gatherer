from .reddit_scrapper import RedditCrawler
#from .private.credentials import CLIENT_AUTH2, SECRET, USER_AGENT
import time


def main():
    # reddit = RedditCrawler(CLIENT_AUTH2, SECRET, USER_AGENT)
    start_time = time.time()
    # reddit.get_info_from(
    #     stock_names=["TSLA", "tesla", "short", "HBO"], limit=20, )
    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
