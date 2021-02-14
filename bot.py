import praw, time

print('Loggining..')
reddit = praw.Reddit(client_id ='',
                    client_secret ='',  
                    user_agent ='Windows:1.3 (by u/Inoix)',  
                    username ='have_a_day_bot',  
                    password ='')  #logging

def reply(submission, wait, ar):
    for i in ar:
        if i == submission.id:
            print('we already replied to this post ' + submission.id)
            break
    else:
        print("we didn't replied to " + submission.id)
        print('replying')
        try:
            submission.reply("Have a day.")
        except Exception as er:
            try:
                print("ERROR: " + er)
            except:
                try:
                    print("ERROR: " + str(er))
                except:
                    print("ERROR, Can't show")
        else:
            print('SUCESS!')
            out = open('output.txt', 'a')
            out.write("Title: " + submission.title +  "\n Text:  " + submission.selftext + "ID: " + submission.id + "\n---------------------------------\n")
            out.close()
            x = open('ar.txt', 'a')
            x.write(submission.id + '\n')
            x.close()
            print("Title: ", submission.title)
            print("Text: ", submission.selftext)
            print("ID: ", submission.id)
            print("---------------------------------\n")
            ar.append(submission.id)
        finally:
            print('Waiting ' + str(wait / 60) + 'm')
            time.sleep(wait)

subreddit = reddit.subreddit("memes")


a = True
print('Loading posts we already replied')
ar = list() #ar = already replied
x = open('ar.txt', 'r')
for line in x:
    print(line.strip())
    ar.append(line.strip())
x.close()
while a == True: # Main loop
    print('enter how many minutes do we wait?')
    wait = int(input()) * 60
    print('How many posts  do we comment? (for all of subreddits)')
    num = int(input())
    for submission in subreddit.hot(limit=num):
        reply(submission, wait, ar)
