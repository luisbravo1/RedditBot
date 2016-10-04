import praw
from praw.helpers import comment_stream

r = praw.Reddit("luisbravo1 test")
r.login()

target_text = "Hello"
response_text = "Welcome to our subreddit!"

processed = []
while True:
    for c in comment_stream(r, 'BotTestBravo'):
        if target_text in c.body and c.id not in processed:
            c.reply(response_text)
            processed.append(c.id)

