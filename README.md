# Coronavirus Workers Support Group

In the wake of the coronavirus/COVID19, many workers are facing hardship due to a lack of comprehensive sick pay policies, the prevalance of zero hour contracts, exposure to the virus without adequate protection, and a lack of adequate policies to cover colleagues requiring sick leave. Workers rights are always important, and this global issue has thrown the lack of workers rights into stark contrast.

This support group, located [here](https://www.facebook.com/groups/329192668038673/) on facebook, aims to provide support and advice for workers in the UK facing issues at work.

## Twitter Reply App

This app has been created to tell more people about the existence of the support group. It responds to those using the hashtag #COVID19walkout on twitter to point them in the direction of the group.

### How it works

The app is written in python 3.5 and is deployed through the cloud service [Heroku](https://www.heroku.com). This allows the app to run constantly in the background and monitor the use of the hashtag.

Rather than monitoring a constant stream of tweets, the app searches for the hashtag on twitter and responds to tweets that it finds. It keeps note of any tweets that it has already replied to, so that twitter users are not bombarded with replies.

The app runs once an hour - this allows it to be run using Heroku's free service, which allows the app to 'sleep' when not in use and thus will not push us over the 550 hour/month limit on the free plan.

### Nuts and bolts

The backend of Heroku is controlled based on the guide [here](https://medium.com/datadriveninvestor/making-a-quote-tweeting-twitter-bot-with-python-tweepy-and-heroku-69a11cd3f47e). Similar to the guide, the tweepy library is used to allow python to talk to the twitter API.

The authorisation keys are held internally as environment variables in Heroku, and accessed securely from the script, so anyone running this for themselves would need to create their own twitter app to get the necessary access tokens.