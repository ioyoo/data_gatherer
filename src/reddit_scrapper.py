from .tools.text_tools import find_in_text
import praw


class RedditCrawler:
    def __init__(
        self, client_id, client_secret,
        user_agent
    ) -> None:
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )

    def get_info_from(self,
                      stock_names=["GME", "gamestop"],
                      subreddits=["wallstreetbets"],
                      limit=5):
        """ Given stock anmes and subreddits, returns how many times it was mentioned, given a time lot

        Args:
            stock_names (list, optional): _description_. Defaults to ["GME"].
            subreddits (list, optional): _description_.
                        Defaults to ["wallstreetbets"].
            timeout (int, optional): _description_. Defaults to 5.
        """
        for subreddit in subreddits:
            sub = self.reddit.subreddit(subreddit)
            for submission in sub.new(limit=limit):
                text = submission.selftext
                for word in stock_names:
                    if find_in_text(word, text):
                        print(text + "\n")
