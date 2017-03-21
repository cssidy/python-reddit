#!/usr/bin/python

# open Reddit in browser
# run script from termina
# refresh browser to see changes
# enter ctrl+c in terminal to stop script

# Posts Lenny emoji in response to creep-potential comments.
# ( ͡° ͜ʖ ͡°)


import praw
import re


reddit = praw.Reddit('test_bot')
subreddit = reddit.subreddit('pythonforengineers')

# verify user login
# print(reddit.user.me())

# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    if re.search('wash', comment.body, re.IGNORECASE):
        # reply to posts matching keywords
        comment.reply("( ͡° ͜ʖ ͡°)")
        print("Bot replying to comment: ", comment.body)



