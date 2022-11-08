from .private.credentials import CLIENT_AUTH2, SECRET, USER_AGENT
import praw


class RedditCrawler:
    def __init__(self, client_id=CLIENT_AUTH2, client_secret=SECRET,
                 user_agent=USER_AGENT) -> None:
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def get_info_from(self, subreddit="wallstreetbets"):
        sub = self.reddit.subreddit(subreddit)
        for submission in sub.hot(limit=10):
            print(submission.title)


reddit = RedditCrawler()
reddit.get_info_from()
