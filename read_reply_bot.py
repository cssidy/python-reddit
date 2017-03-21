#!/usr/bin/python

import praw
import pprint

reddit = praw.Reddit('bot1')
subreddit = reddit.subreddit("askreddit")

for submission in subreddit.hot(limit=10):
    pprint.pprint("Title: ", submission.title)
    pprint.pprint("Text: ", submission.selftext)
    pprint.pprint("Score: ", submission.score)