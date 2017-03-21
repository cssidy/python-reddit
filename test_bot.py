#!/usr/bin/python

# open Reddit in browser
# run script from termina
# refresh browser to see changes
# enter ctrl+c in terminal to stop script

import praw
import re


reddit = praw.Reddit('test_bot')
subreddit = reddit.subreddit('pythonforengineers')

# verify user login
# print(reddit.user.me())

# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    if re.search('nsfw', comment.body, re.IGNORECASE):
        # reply to posts matching keywords
        comment.reply("PG13 Bot: This comment ^ above is not safe for work.")
        print("Bot replying to comment: ", comment.body)

