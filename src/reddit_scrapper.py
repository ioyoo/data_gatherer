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
                      stock_names=["GME", "gamestop"],
                      subreddits=["wallstreetbets"],
                      filter="day"):
        """ Given stock names and subreddits, returns how many times it was mentioned, given a time lot

        Args:
            stock_names (list, optional): list with names to look for. Defaults to ["GME"].
            subreddits (list, optional): list of subreddit names.
                        Defaults to ["wallstreetbets"].
            timefilter (int, optional): Number of . Defaults to 5.

        Returns: dict[<name>] = [<post = {text, upvotes, downvotes, awards, category}>, ... , ...]
        """
        for subreddit in subreddits:
            sub = self.reddit.subreddit(subreddit)
            for submission in sub.top(time_filter=filter):
                for word in stock_names:
                    if find_in_text(word, submission.selftext):
                        try:
                            self.posts[word].append(
                                self._create_posts_dict(submission))
                        except KeyError:
                            self.posts[word] = [
                                self._create_posts_dict(submission)]
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

    def read_from_reddit(self,
                         stock_names=["GME", "gamestop"],
                         subreddits=["wallstreetbets"],
                         filter="day"):
        """ Given stock names and subreddits, returns how many times it was mentioned, given a time lot

        Args:
            stock_names (list, optional): list with names to look for. Defaults to ["GME"].
            subreddits (list, optional): list of subreddit names.
                        Defaults to ["wallstreetbets"].
            timefilter (int, optional): Number of . Defaults to 5.

        Returns: dict[<name>] = [<post = {text, upvotes, downvotes, awards, category}>, ... , ...]
        """
        for subreddit in subreddits:
            sub = self.reddit.subreddit(subreddit)
            for submission in sub.top(time_filter=filter):
                text = submission.selftext
                for word in stock_names:
                    if find_in_text(word, text):
                        print(text + "\n")

    def get_data(self):
        return self.posts
