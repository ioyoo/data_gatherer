from .tools.text_tools import find_in_text
import praw


class RedditCrawler:
    TIME_FILTERS = ["all", "day", "hour", "month", "week", "year"]

    def __init__(
        self, client_id, client_secret,
        user_agent
    ) -> None:
        self.reddit = praw.Reddit(
            client_id=client_id,
            client_secret=client_secret,
            user_agent=user_agent,
        )
        self.posts = {}

    def get_info_from(self,
                      stock_keywords: dict = {"GME": ["gamestop", "game"]},
                      subreddits=["wallstreetbets"],
                      filter="day"):
        """ Given stock names and subreddits, returns how many times it was mentioned, given a time lot

        Args:
            stock_keywords (dict, optional): key is ticker. values is list of words that can be used to reference that name
            subreddits (list, optional): list of subreddit names.
                        Defaults to ["wallstreetbets"].
            timefilter (int, optional): Number of . Defaults to 5.

        Returns: dict[<name>] = [<post = {text, upvotes, downvotes, awards, category}>, ... , ...]
        """
        for subreddit in subreddits:
            sub = self.reddit.subreddit(subreddit)
            for submission in sub.top(time_filter=filter):
                for ticker, word in stock_keywords.items():
                    if find_in_text(word, submission.selftext):
                        try:
                            self.posts[ticker].append(
                                self._create_posts_dict(submission))
                        except KeyError:
                            self.posts[word] = [
                                self._create_posts_dict(submission)]
        return self.posts

    def get_data(self):
        return self.posts

    def _create_posts_dict(self, submission):
        """ creates dictionary of given submission

        Args:
            submission (Submission): submission entry from reddit

        Returns:
            dict: post dictionary
        """
        return {
            "text": submission.selftext,
            "upvotes": submission.ups,
            "downvotes": submission.downs,
            "awards": submission.total_awards_received,
            "category": submission.category
        }
