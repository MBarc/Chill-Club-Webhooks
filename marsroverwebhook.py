import requests, datetime
from discord_webhook import DiscordWebhook, DiscordEmbed

yesterday = f'{datetime.datetime.now().year}-{datetime.datetime.now().month}-{datetime.datetime.now().day - 3}' # -1 to get yesterday's date
api_key = 'fezcl1LeViOKgNbcpWHSetE75fPvz7BdiFHaaVXd'
r = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?earth_date={yesterday}&camera=fhaz&api_key={api_key}')

try:
    webhookURL = 'https://discordapp.com/api/webhooks/729050571700568065/NaR8XFpShKy1EZPPlCKQMMT9xSqjq2cftlK67YEsnC1sYSMmAvHELUWKRbSAnN5FlwGG'
    webhook = DiscordWebhook(url=webhookURL)

    embed = DiscordEmbed(title=f"Taken on {r.json()['photos'][0]['earth_date']}", color=15170833)#color == hex value converted to decimal
    embed.set_image(url=r.json()['photos'][0]['img_src']) #Exception would be here -> list index out of range
    webhook.add_embed(embed)

    response = webhook.execute()

except:
    pass