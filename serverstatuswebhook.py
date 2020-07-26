from requests_html import HTMLSession
from discord_webhook import DiscordWebhook

services = {
    'Call of Duty': {
        'webhook': 'https://discordapp.com/api/webhooks/727289363175702680/_wcOyVKx3lO8lpEKYK-E_B3KZiV02opZL8H6Ylk1pzYlX91WPDlERjWvpH4TdgQFSV36',
        'url': 'https://downdetector.com/status/call-of-duty/',
        'roleID': '727221234429067295',
        'status': 'online'
    },
    'Destiny': {
        'webhook': 'https://discordapp.com/api/webhooks/727744001347813406/XtD6rbzrxosf22rWK6CmZK3k1y2_IGZ0pI9QgBA-sk5_XD2UTgjEafZBfFqOLOUzxai6',
        'url': 'https://downdetector.com/status/destiny/',
        'roleID': '727221199037399061',
        'status': 'online'
    },
    'Fortnite': {
        'webhook': 'https://discordapp.com/api/webhooks/727737910744449085/oGbwBndH-Nf6fBXYgJjbAM5UNBGriZk7ReZ6Es7x-blmhSsJvl8NU-JzbxmHg95Av8iM',
        'url': 'https://downdetector.com/status/fortnite/',
        'roleID': '727505873613881426',
        'status': 'online'
    },
    'Nintendo Switch Online': { # used by the following categories [Animal Crossing]
        'webhook': 'https://discordapp.com/api/webhooks/727737354147856418/ktJOo-qbScfxFlxNda4cMM9hgFTCu6igkvnXpq2S30dC_PINFgHkWmsZCbcnPk1sCwG8',
        'url': 'https://downdetector.com/status/nintendo-switch-online/',
        'roleID': '727221111531503686', #animal crossing role ID
        'status': 'online'
    },
    'Overwatch': {
        'webhook': 'https://discordapp.com/api/webhooks/727740100183851069/tHfDu958gaXonN2sRVvhrqTjE3QOW26P1H35SqJjUxFJdHjB6jr_A9FMewP-gXeC-z8y',
        'url': 'https://downdetector.com/status/overwatch/',
        'roleID': '727505803711479879',
        'status': 'online'
        },
    'Rainbow 6': {
        'webhook': 'https://discordapp.com/api/webhooks/727741184734396417/FM1p4VUMhG_OcQjA0YbV04wsfzgIVPClKq4KtC-fkwYtejncS0jy_2Fc3UceZaHLudv4',
        'url': 'https://downdetector.com/status/rainbow-six/',
        'roleID': '727505837953646632',
        'status': 'online'
    },
    'Rocket League': {
        'webhook': 'https://discordapp.com/api/webhooks/727811332367450123/2sSNwF1YFzRGWplRon8-MUpgf-HH8iuklSJALWgZC9wAQj0dZXQZiXFkoPhTiu6E3zvA',
        'url': 'https://downdetector.com/status/rocket-league/',
        'roleID': '727221384539013121',
        'status': 'online'
    },
    'The Sims': {
        'webhook': 'https://discordapp.com/api/webhooks/727743037652074517/TdXx6HML1-b3E3_eEhhOJOq0ci-kfZQeO_7cHrP4znwoatjg8DCf3hX5dPPB8NpUyprd',
        'url': 'https://downdetector.com/status/the-sims-4/',
        'roleID': '727221741071368203',
        'status': 'online'
    }
}

service_names = [service for service in services]

while True:
    for name in service_names:

        session = HTMLSession()

        r = session.get(services[name]['url'])

        service_status = str(r.html.xpath('/html/body/div[3]/div[2]/div[1]/div[1]/div/div[1]'))

        #Problem to work on: service_status HTML path does no exist for 'Problems at {service}' as oppose to 'Possible problems at {service}'

        if "danger" in service_status or "warning" in service_status: # if service offline

            if services[name]['status'] == 'offline': # if it was already determined to be offline
                continue
            else: # if service wasn't offline before, notify the discord webhook
                services[name]['status'] = 'offline'

                webhookContent = f"<@&{services[name]['roleID']}> {name} is experiencing issues. You may experience trouble connecting to their servers."
                webhook = DiscordWebhook(url=services[name]['webhook'], content=webhookContent)
                response = webhook.execute()
        else: # if service online

            if services[name]['status'] == 'online':  # if it was already determined to be online
                continue
            else: # if the service wasn't online before, notify the discord webhook
                services[name]['status'] = 'online'

                webhookContent = f"<@&{services[name]['roleID']}> {name} is no longer experiencing issues. Everything should be fine."
                webhook = DiscordWebhook(url=services[name]['webhook'], content=webhookContent)
                response = webhook.execute()