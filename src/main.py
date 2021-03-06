# Built-in libraries
import time

# External library for reddit use
import praw

# Personal scripts and files
import config
from functions import srch

# Reddit instace initialization
reddit = praw.Reddit(client_id=config.client_id,
                     client_secret=config.client_secret,
                     username=config.username,
                     password=config.password,
                     user_agent=config.user_agent)

# Subreddit initializations
subreddit_name = 'dankmemes'
subreddit = reddit.subreddit(subreddit_name)

KEYWORDS = ['heck', 'frick', 'darn', 'h**k', 'f***', 's**t']

while True:
    srch(subreddit, KEYWORDS)
    time.sleep(601)  # 10 min., 1 sec due to Reddit restrictions
