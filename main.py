import praw

reddit = praw.Reddit('visualizer_for_reddit')
print(reddit.read_only)

# for submission in reddit.subreddit('horizon').hot(limit=10):
#     print(submission.title)
