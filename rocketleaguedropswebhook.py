import requests, json
from discord_webhook import DiscordWebhook

#Pulling all JSON information
url = 'https://tmi.twitch.tv/group/user/rocketleague/chatters'
r = requests.get(url)
jsonData = json.loads(r.text)

#Grabbing the amount of viewers
amountOfViews = jsonData['chatter_count']

if amountOfViews >= 5000: # 5000 people to know that the Rocket League channel is stream (as opposed to hosting another channel).

    webhook = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
    webhookContent = f'Rocket League is live on Twitch Right now! View the stream here <https://www.twitch.tv/rocketleague>'
    webhook = DiscordWebhook(url=webhook, content=webhookContent)

    response = webhook.execute()
