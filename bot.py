import tweepy, time, sys
from os import environ
from datetime import datetime, timedelta

CONSUMER_KEY = environ['CONSUMER_KEY']
CONSUMER_SECRET = environ['CONSUMER_SECRET']
ACCESS_KEY = environ['ACCESS_KEY']
ACCESS_SECRET = environ['ACCESS_SECRET']

def tweet_test():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)
    
    reply_text = 'For support/advice as a worker affected by coronavirus, follow us and join the FB group at www.facebook.com/groups/329192668038673/'

    api.update_status(status=reply_text)

def tweet_reply():
    interval = 60 * 25 # run the app every hour

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)

    api = tweepy.API(auth)

    hashtags = ['%23covid19walkout', '%23keyworkers', '%23universalbasicincome', '%23universalbasicincomenow']
    joiner = '+OR+'
    
    reply_text = 'For support/advice as a worker affected by coronavirus, follow us and join the FB group at www.facebook.com/groups/329192668038673/'

    tweet_history = []

    print ( 'Starting main loop' )
    sys.stdout.flush()

    while True: # the main loop to run the app
        tweet_count = 0        
        for tweet in tweepy.Cursor(api.search, q=joiner.join(hashtags), lang='en', geocode='54.259447,-4.191876,500km', result_type = 'recent', count=20).items(): # cycle through the tweets found with the hashtag
            if tweet is None:
                print ( 'No results in Search' )
                sys.stdout.flush()
                break
            # Ignore tweets already replied to, and only look at those in the last hour and in English
            if ( tweet.user.id_str not in tweet_history ) and ( tweet.created_at > (datetime.now() - timedelta(minutes = 25)) ):
                
                # Add this tweet to those already replied to
                tweet_history.append(tweet.user.id_str)
                
                # Construct the reply that will go into the tweet
                reply_status = '@%s %s' % (tweet.user.screen_name, reply_text)
                try:
                    # Tweet a reply to the user
                    api.update_status(status=reply_status, in_reply_to_status_id=tweet.id_str, auto_populate_reply_metadata=True)
                except tweepy.TweepError:
                    print ( 'Caught Tweepy error' )
                    sys.stdout.flush()
                    continue
            tweet_count += 1
            if tweet_count == 20:
                print ( 'Replied to 20 tweets' )
                sys.stdout.flush()
                break
            time.sleep(10)
        print ( '%s Tweets in Search' % tweet_count )
        sys.stdout.flush()
        print ( 'Sleeping' )
        sys.stdout.flush()
        time.sleep(interval)
        print ( 'Waking Up' )
        sys.stdout.flush()

if __name__ == '__main__':
    tweet_reply()
