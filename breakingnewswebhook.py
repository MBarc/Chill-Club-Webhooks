import tweepy
from discord_webhook import DiscordWebhook
from datetime import datetime
import datetime as dt
import time

consumerKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumerSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessTokenSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Account name that we want to grap the tweets of
username = "cnnbrk"

waitTime = 60 #Same at tweet age
while True:

    time.sleep(waitTime)

    #Grabbing both times at the end of the time frame
    startTime = dt.datetime.utcnow() - dt.timedelta(seconds=waitTime)
    endTime = dt.datetime.utcnow()

    mostRecentTweet = api.user_timeline(username)[0]
    if mostRecentTweet.created_at < endTime and mostRecentTweet.created_at > startTime:

        webhook = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
        webhookContent = f'https://twitter.com/cnnbrk/status/{mostRecentTweet.id}' #Exception would be here
        webhook = DiscordWebhook(url=webhook, content=webhookContent)
        response = webhook.execute()
