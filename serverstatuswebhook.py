from requests_html import HTMLSession
from discord_webhook import DiscordWebhook

services = {
    'Call of Duty': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/call-of-duty/',
        'roleID': '727221234429067295',
        'status': 'online'
    },
    'Destiny': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/destiny/',
        'roleID': '727221199037399061',
        'status': 'online'
    },
    'Fortnite': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/fortnite/',
        'roleID': '727505873613881426',
        'status': 'online'
    },
    'Nintendo Switch Online': { # used by the following categories [Animal Crossing]
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/nintendo-switch-online/',
        'roleID': '727221111531503686', #animal crossing role ID
        'status': 'online'
    },
    'Overwatch': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/overwatch/',
        'roleID': '727505803711479879',
        'status': 'online'
        },
    'Rainbow 6': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/rainbow-six/',
        'roleID': '727505837953646632',
        'status': 'online'
    },
    'Rocket League': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
        'url': 'https://downdetector.com/status/rocket-league/',
        'roleID': '727221384539013121',
        'status': 'online'
    },
    'The Sims': {
        'webhook': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
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
