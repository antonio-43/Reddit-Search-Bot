import sys
import praw
from time import sleep


print('Reddit Search Bot')
print()

MAIN = 'https://www.reddit.com/r/'

print('SUB-REDDIT: ')
name_sub_reddit = input()

url = MAIN+name_sub_reddit+'/'
print('TO SEE THE URL')
print(url)


def find_stuff():

    try:
        # api client data
        client_id = 'TK93O0bGrbPT0Q'
        client_secret = 'MxEXTQljTWdJHvzOonZSfaB1fhY'
        user_agent = 'bot'
        username = 'BotDoReddit43'
        password = 'BotDoReddit43'
                    
        reddit = praw.Reddit(client_id = client_id,
                            client_secret = client_secret,
                            user_agent = user_agent,
                            username = username,
                            password = password)

        print('HOW MANY POSTS?')
        post_quant = int(input())
        subreddit_info = reddit.subreddit('Python')
            
        print()
        print('SOME SUBREDDIT INFORMATIONS: ')
        print()
        print()
        print(subreddit_info.title)
        print(subreddit_info.description)
        print()
        print()

                    
        print()
        print(f'HOT CONTENT ON SUBREDDIT: {name_sub_reddit}')
        print(40*'=')
                    
        for submission in reddit.subreddit(name_sub_reddit).hot(limit=post_quant):
            print(submission.title, '    SCORE: ', submission.score)
            print()

        print()
        print('NEW:')
        print()
        print()

        for i in reddit.subreddit(name_sub_reddit).new(limit=post_quant):
            print(i.title, '    SCORE: ', i.score)
            print()
                    
        print()
        print('TOP:')
        print()
        print()

        for j in reddit.subreddit(name_sub_reddit).top(limit=post_quant):
            print(j.title, '    SCORE: ', j.score)
            print()                   

    except:
        print('REQUEST ERROR...')
