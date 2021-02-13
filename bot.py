import praw, time
print('Loggining..')
reddit = praw.Reddit(client_id ='arl2Sw5wQmimEQ',  
                     client_secret ='eZ6KcXUgY1M0YKMaROORUOY_tKHOFg',  
                     user_agent ='Windows:1.0 (by u/Inoix)',  
                     username ='have_a_day_bot',  
                     password ='')  #logging

def reply(submission, wait, ar): #function to reply to a posts
    for i in ar: #checking if we already replied to this post
        if i == submission.id:
            break
    else:
        try:
            submission.reply("Have a day.") #trying to reply
        except Exception as er:
            print(er)
        else:
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("ID: ", submission.id)
            print("---------------------------------\n")
            ar.append(submission.id)
        finally:
            time.sleep(wait) #waiting because limit

subreddit = reddit.subreddit("memes")


a = True
ar = list() #ar = already replied
while a == True: # Main loop
    print('enter how many minutes do we wait?')
    wait = int(input()) * 60
    print('How many posts  do we comment? (for all of subreddits)')
    num = int(input())
    for submission in subreddit.hot(limit=num):
        reply(submission, wait, ar)
