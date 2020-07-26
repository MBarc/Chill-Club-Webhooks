import tweepy
from discord_webhook import DiscordWebhook
import datetime as dt

consumerKey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumerSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessToken = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
accessTokenSecret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Account name that we want to grap the tweets of
username = "charlieINTEL"

#Getting information/news tweets by filtering out any replies
newsTweets = []
for tweet in api.user_timeline(username):
    if tweet.in_reply_to_status_id: #if tweet is a reply
        continue # do nothing
    else:
        newsTweets.append(tweet)

#Grabbing both times at the end of the time frame
startTime = dt.datetime.utcnow() - dt.timedelta(seconds=60*60) # 1 hour
endTime = dt.datetime.utcnow()

mostRecentTweet = newsTweets[0]
if mostRecentTweet.created_at < endTime and mostRecentTweet.created_at > startTime:
    webhook = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    webhookContent = f'https://twitter.com/charlieINTEL/status/{mostRecentTweet.id}'  # Exception would be here
    webhook = DiscordWebhook(url=webhook, content=webhookContent)
    response = webhook.execute()
