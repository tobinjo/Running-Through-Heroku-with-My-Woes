import praw
import pdb
import re
import os

REDDIT_USERNAME = 'comeonspurs'
REDDIT_PASSWORD = '305223'
r = praw.Reddit(user_agent = 'John Tobin')
r.login(REDDIT_USERNAME, REDDIT_PASSWORD)
subreddit = r.get_subreddit('pythonforengineers')
for submission in subreddit.get_hot(limit=5):
    titletext = submission.title
    if titletext.find('fam') != -1:
        submission.add_comment('Yo what''s good fam')
    else:
        print 'No fam in this title fam'
