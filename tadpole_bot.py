#!/usr/bin/python

# open Reddit in browser
# run script from terminal
# refresh browser to see changes
# enter ctrl+c in terminal to stop script

# Posts tadpole emoji in response to comments with the word "tadpole".
# (°°)～


import praw
import re


reddit = praw.Reddit('test_bot')
subreddit = reddit.subreddit('frogs')

# verify user login
# print(reddit.user.me())

# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    if re.search('wash', comment.body, re.IGNORECASE):
        # reply to posts matching keywords
        comment.reply("(°°)～")
        print("Bot replying to ", comment.author, 's comment ', comment.body, '.')
