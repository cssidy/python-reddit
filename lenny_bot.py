# Posts creeper emoji in response to creep-potential comments.


import praw

KEYWORDS = ['pythons', 'python']
REPLY_TEMPLATE = '( ͡° ͜ʖ ͡°)'


reddit = praw.Reddit('lenny_bot')
subreddit = reddit.subreddit('AskReddit')


def process_submission(submission):
    normalized_title = submission.title.lower()
    for keyword_phrase in KEYWORDS:
        if keyword_phrase in normalized_title:
            reply_text = REPLY_TEMPLATE
            print('Replying to: {}', submission.title)
            submission.reply(reply_text)
            break


for submission in subreddit.stream.submissions():
    process_submission(submission)

