import tweepy
from discord_webhook import DiscordWebhook
from datetime import datetime
import datetime as dt
import time

consumerKey = "xzKmPYUndQyF3sW8Yzs7A6Ia4"
consumerSecret = "bC9DMdqbonyvphhoX0vbNKfKXtyXhyIAZQagugtqUW5R6p0bcz"
accessToken = "925489542-bK3Kbf62l9ludW3fahrY3sIjHoPKCeA5h0UJR9my"
accessTokenSecret = "sPDY4prKtPwgg4c63VzXr1d2cRGQFyH2aGxLQLwwM5tBe"

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

        webhook = 'https://discordapp.com/api/webhooks/692080532250558594/xEMzGLFnmRFtT2cBgUQT-S_Yj2qdXZT0nlPaNVVmffEVgAAXRznjpR-1h6uv_DyUpBCn'
        webhookContent = f'https://twitter.com/cnnbrk/status/{mostRecentTweet.id}' #Exception would be here
        webhook = DiscordWebhook(url=webhook, content=webhookContent)
        response = webhook.execute()
