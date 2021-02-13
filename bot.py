import praw, time
reddit = praw.Reddit(client_id ='my client id',  
                     client_secret ='my client secret',  
                     user_agent ='Windows:1.0 (by u/Inoix)'',  
                     username ='have_a_day_bot',  
                     password ='')  #logging


subreddit = reddit.subreddit("memes")


a = True

while a == True: # Main loop
    print('enter how many minutes do we wait?')
    wait = int(input()) * 60
    print('How many posts  do we comment? (for all of subreddits)')
    num = int(input())
    for submission in subreddit.hot(limit=num):
        try:
            submission.reply("Have a day.")
        except Exception as er:
            print(er)
        else:
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("ID: ", submission.id)
            print("---------------------------------\n")
            time.sleep(wait)
