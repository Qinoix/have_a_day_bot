import praw
reddit = praw.Reddit(client_id ='my client id',  
                     client_secret ='my client secret',  
                     user_agent ='u/have_a_day_bot by u/Inoix',  
                     username ='have_a_day_bot',  
                     password ='MEbCa8WXQ5FZ4P6')  #logging


subreddit = reddit.subreddit("memes")


a = True

while a == True: # Main loop
    print('How many posts  do we comment? (for all of subreddits)')
    num = input()
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
