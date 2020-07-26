import tweepy
from discord_webhook import DiscordWebhook
import datetime as dt

consumerKey = "xzKmPYUndQyF3sW8Yzs7A6Ia4"
consumerSecret = "bC9DMdqbonyvphhoX0vbNKfKXtyXhyIAZQagugtqUW5R6p0bcz"
accessToken = "925489542-bK3Kbf62l9ludW3fahrY3sIjHoPKCeA5h0UJR9my"
accessTokenSecret = "sPDY4prKtPwgg4c63VzXr1d2cRGQFyH2aGxLQLwwM5tBe"

auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
auth.set_access_token(accessToken, accessTokenSecret)
api = tweepy.API(auth)

#Account name that we want to grap the tweets of
username = "fortnitebr"

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
    webhook = 'https://discordapp.com/api/webhooks/729545743211429970/Q5kmsgw0Nm6DXUXGCyL-VIPXigIs8wUoAlTICiPHEe-9ADhvtio11wB7qfPrWNdyhmYU'
    webhookContent = f'https://twitter.com/fortnitebr/status/{mostRecentTweet.id}'  # Exception would be here
    webhook = DiscordWebhook(url=webhook, content=webhookContent)
    response = webhook.execute()
