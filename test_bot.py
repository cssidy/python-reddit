#!/usr/bin/python

import praw
import re


reddit = praw.Reddit('test_bot')
subreddit = reddit.subreddit('pythonforengineers')

# verify user login
# print(reddit.user.me())

# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    if re.search("soap", comment.body, re.IGNORECASE):
        # reply to posts matching keywords
        comment.reply("Argargarg! Pirate bot mespeaks! Me python is grimy!")
        print("Bot replying to comment: ", comment.body)