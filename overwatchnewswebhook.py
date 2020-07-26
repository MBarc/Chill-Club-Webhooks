import datetime
from discord_webhook import DiscordWebhook
from requests_html import HTMLSession

overwatchURL = 'https://playoverwatch.com/en-us/news/patch-notes/'

#Grabbing the last update post on Overwatch's website
session = HTMLSession()
r = session.get(overwatchURL)
lastPostDate = str(r.html.xpath('/html/body/section[1]/section/div[2]/div[1]/div[1]/div[1]/div/text()'))[2:-2]

#Gettings todays info to compare to lastPostDate
today = datetime.datetime.today()
currentDate = f'{today.month}/{today.day}/{today.year}'

if currentDate in lastPostDate:
    webhook = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    webhookContent = f'New patch came out! View it here: <{overwatchURL}>'
    webhook = DiscordWebhook(url=webhook, content=webhookContent)
    response = webhook.execute()
