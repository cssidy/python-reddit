#!/usr/bin/python

# author: cssidy
# Posts Lenny emoji in response to creeper-potential comments.
# ( ͡° ͜ʖ ͡°)

# open Reddit in browser
# run script from terminal
# refresh browser to see changes
# enter ctrl+c in terminal to stop script

# WARNING! may get your account suspended, or many angry inbox messages
# for educational purposes only

import praw

# list possible innuendo phrases here
KEYWORDS = ['uranus']

reddit = praw.Reddit('test_bot')
subreddit = reddit.subreddit('all')

# monitor subreddit for new comments matching string
for comment in subreddit.stream.comments():
    for k in KEYWORDS:
        if k in comment.body:
            print("Bot replying to commenter: ", comment.author)
            comment.reply("( ͡° ͜ʖ ͡°)")

