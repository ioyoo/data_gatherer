from ..reddit_scrapper import RedditCrawler


def test_redditCrawler():
    redditCrawler = RedditCrawler("test", "test", "test")
    assert redditCrawler is not None
