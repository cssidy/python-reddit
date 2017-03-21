#!/usr/bin/python

import praw
import re
import os


reddit = praw.Reddit('read_reply_bot')
subreddit = reddit.subreddit('pythonforengineers')


# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    if re.search("soap", comment.body, re.IGNORECASE):
        # reply to the post
        comment.reply("Argargarg! Pirate bot mespeaks! Me python is grimy!")
        print("Bot replying to comment: ", comment.body)

