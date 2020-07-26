import requests, json
from discord_webhook import DiscordWebhook, DiscordEmbed
import pprint
#Getting data from Nasa's A.P.O.D.
api_key = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
r = requests.get(f'https://api.nasa.gov/planetary/apod?api_key={api_key}').text
data = json.loads(r)

pprint.pprint(data)

#Initializing webhook message and embedding content into it
webhookURL = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
webhook = DiscordWebhook(url=webhookURL)
embed = DiscordEmbed(title=data['title'], description=data['explanation'], color=1000)
embed.set_image(url=data['url'])

if 'copyright' in data.keys(): # seeing if the picture is public domain
    embed.set_footer(text=f"Copyright© {data['copyright']}")
else:
    embed.set_footer(text='Public Domain')


webhook.add_embed(embed)
response = webhook.execute()
