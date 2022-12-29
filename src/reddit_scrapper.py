from tools.text_tools import find_in_text
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
        self.posts = {}

    def get_info_from(self,
                      stock_names=["GME", "gamestop"],
                      subreddits=["wallstreetbets"],
                      limit=5):
        """ Given stock names and subreddits, returns how many times it was mentioned, given a time lot

        Args:
            stock_names (list, optional): _description_. Defaults to ["GME"].
            subreddits (list, optional): _description_.
                        Defaults to ["wallstreetbets"].
            timeout (int, optional): _description_. Defaults to 5.

        Returns: dict[<name>] = [<post = {text, upvotes, downvotes, awards, category}>, ... , ...]
        """
        for subreddit in subreddits:
            sub = self.reddit.subreddit(subreddit)
            for submission in sub.new(limit=limit):
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
                         limit=5):
        """ Given stock names and subreddits, print in terminal the found messages

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

    def get_data(self):
        return self.posts
