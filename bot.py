import tweepy, time, sys
from os import environ
from datetime import datetime, timedelta
from email.utils import parsedate_tz

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def to_datetime(datestring):
    time_tuple = parsedate_tz(datestring.strip())
    dt = datetime(*time_tuple[:6])
    return dt - timedelta(seconds=time_tuple[-1])

def tweet_test():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    
    reply_text = 'We are a support group for workers affected by COVID19. Please follow us and join the FB group at https://www.facebook.com/groups/329192668038673/'

    api.update_status(status=reply_text)

def tweet_reply():
    interval = 60 * 60 # run the app every hour

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    hashtags = ['#COVID19walkout', '#COVID19WALKOUT', '#covid19walkout']

    reply_text = 'We are a support group for workers affected by COVID19. Please follow us and join the FB group at https://www.facebook.com/groups/329192668038673/'

    tweet_history = []

    while True: # the main loop to run the app

        for hashtag in hashtags: # cycle through the hashtags

            for tweet in tweepy.Cursor(api.search, q=hashtag, count=100).items(): # cycle through the tweets found with the hashtag
                # Ignore tweets already replied to, and only look at those in the last hour and in the UK
                if ( tweet.id not in tweet_history ) and ( tweet.place.country_code == 'GB' ) and ( to_datetime(tweet.created_at) > (datetime.now() - timedelta(hours = 1)) ):
                    
                    # Add this tweet to those already replied to
                    tweet_history.append(tweet.id)
                    
                    # Construct the reply that will go into the tweet
                    reply_status = '@%s %s' % (tweet.user.screen_name, reply_text)
                    # Tweet a reply to the user
                    api.update_status(status=reply_status, in_reply_to_status_id=tweet.id)

        time.sleep(INTERVAL)                

if __name__ == '__main__':
    tweet_test()
