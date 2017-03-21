#!/usr/bin/python

import praw
import re
import os


reddit = praw.Reddit('read_reply_bot')
subreddit = reddit.subreddit('pythonforengineers')


# get the top 10 op's
for op in subreddit.hot(limit=12):
    print(op.title)
    print('\n')

    # case insensitive search
    if re.search("scales", op.title, re.IGNORECASE):

        for comment in subreddit.stream.comments():
            if re.search("soap", comment.body, re.IGNORECASE):
                # reply to the post
                comment.reply("Argargarg! Pirate bot mespeaks! Me python is grimy!")
                print("Bot replying to: ", op.title)
