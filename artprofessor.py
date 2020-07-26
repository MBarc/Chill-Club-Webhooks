from discord_webhook import DiscordWebhook
import random
import datetime

def numberToDayofWeek(today):
    if today == 0:
        return "Monday"
    if today == 1:
        return "Tuesday"
    if today == 2:
        return "Wednesday"
    if today == 3:
        return "Thursday"
    if today == 4:
        return "Friday"
    if today == 5:
        return "Saturday"
    if today == 6:
        return "Sunday"

prompts = [
    "Make yourself, as an animal",
    "Make a cat who’s dressed for an interview",
    "Make an agitated dog with aggressive body language",
    "Make an internet troll",
    "Make powerful spirits disguised as kittens",
    "Make your dream pet in his pajamas",
    "Make a fruity ninja",
    "Make a camel surfing the waves",
    "Combine two animals to create a new one",
    "Make a shark eating a cupcake",
    "Make a dinosaur at a birthday party",
    "Make a horse throwing a horseshoe",
    "Make a koala bear sitting on a trash can",
    "Make a squirrel roasting a marshmallow around a campfire",
    "Make a butterfly eating a steak",
    "Make a cat chasing a dog",
    "Make a dog playing ping pong",
    "Make one of the admins eating pizza while dancing",
    "Make one of the admins as a zombie",
    "Make yourself with a super power",
    "Make yourself as a fairy",
    "Make a Pop Tart lifting weights",
    "Make a food eating another food",
    "Make a dancing taco wearing a sombrero",
    "Make an annoying orange",
    "Make a turkey leg eating a turkey sandwich",
    "Make a banana in pajamas",
    "Make a garden of lollipops",
    "Make an ice cream cone eating a Popsicle",
    "Make yourself as a spoiled brat",
    "Make a super scary Valentine’s Day card",
    "Make a design for a $3 bill",
    "Make a pencil sharpener eating something other than a pencil",
    "Make a starfish eating a bowl of cereal under the sea",
    "Make a pair of scissors running",
    "Make your own version of Mount Rushmore",
    "Make one of the admins as a pirate captain",
    "Make a battle elf",
    "Make a troll riding a unicorn",
    "Make what your imaginary friend would look like if we could see them",
    "Make a dragon breathing rainbows",
    "Combine two holidays to make a new one",
    "Make the moon fighting the sun over a turkey sandwich",
    "Make a crime scene where a donut lost its donut hole",
    "Make something really gross",
    "Make the moon howling at a wolf",
    "Make your name as an animal",
    "Make a modest unicorn taking a shower",
    "Make another member in a fight with a small animal",
    "Make something from your pet’s point of view",
    "Make a dog taking its human for a walk",
    "Make the most adorable animal you can imagine",
    "Make the most terrifying animal you can imagine",
    "Make a spider as an adorable, cuddly animal",
    "Make the oldest thing in your refrigerator",
    "Make you, getting the last laugh",
    "Make another member as one of Snow White’s dwarves",
    "Make a mysterious man in a sharp business suit",
    "Make a ballet dancer in a striking pose",
    "Make a pigeon fighting for an ice cream cone",
    "Make a shy mouse doing her grocery shopping",
    "Make a vampire astronaut",
    "Make an unenthusiastic fast food employee",
    "Make a peanut butter pussy",
    "Make a frantic tiger who sees that he’s losing his stripes",
    "Make yourself as a Lego figure",
    "Make a goldfish driving a racecar",
    "Make a snail on a skateboard getting away from a puppy",
    "Make a Dracula Parrot on someone's shoulder",
    "Make a llama surfing",
    "Make a fish swimming in something other than water",
    "Make a shark eating a cupcake",
    "Make a crab at a birthday party",
    "Make a seahorse in a blizzard",
    "Make a dinosaur crying",
    "Make an animal with arms for legs and legs for arms",
    "Make a pug on a treadmill",
    "Make a shark waterskiing",
    "Make a walrus in a beach chair",
    "Make a circus elephant standing on a ball",
    "Make a koala bear sitting on a trash can",
    "Make a lizard putting on lipstick",
    "Make a squirrel roasting a marshmallow",
    "Make an octopus with spoons for legs",
    "Make a mouse riding a motorcycle",
    "Make a flamingo doing ballet",
    "Make a butterfly eating a steak",
    "Make a cat chasing a dog",
    "Make a lobster dancing",
    "Make a cat playing a sport",
    "Make a chicken skydiving",
    "Make a piece of fruit in outer space",
    "Make a loaf of bread at a disco",
    "Make a rainstorm of sprinkles",
    "Make french fries on a rollercoaster",
    "Make a walking taco",
    "Make chicken wings flying",
    "Make a banana slipping on banana peels",
    "Make a cookie with googly eyes instead of chocolate chips",
    "Make a pineapple rollerblading",
    "Make a piece of asparagus snowboarding",
    "Make a donut riding a skateboard",
    "Make a cheeseburger wearing a dress",
    "Make a banana in pajamas",
    "Make a peanut butter and jelly sandwich on vacation",
    "Make a hot dog flying",
    "Make a lemon making orange juice",
    "Make something other than a pot of gold at the end of the rainbow",
    "Make an alien driving a car",
    "Make an elf jumping on a trampoline",
]

sentencesUpper = [
    "I don’t usually buy amateur pieces, but I suppose I’ll give you a shot. %s.",
    "My granddaughter Makes as if she's lost both of her eyes. Can you do better? %s.",
    "{prompt} and make it snappy!",
    "I'm looking for a painting that will give my husband a heart attack. Please %s. I think that should do the trick.",
    "I am ready to drop millions of fictional dollars on this piece! %s.",
    "Thanks for the last painting. However, I am already bored. %s.",
    "If you nail this one, it’s going up in my personal gallery. Don’t mess it up! %s.",
    "My grandfather was quite literally Michelangelo. No pressure. %s.",
    "My dentures just fell out so make this quick. %s.",
    "All my friends are dead. %s.",
    "I could make a better piece of art by banging my cane against the wall. Prove me wrong. %s.",
    "Last time I really felt something was in 1982. Make something that’ll rattle my bones a bit, will you? %s.",
    "The ladies in my walking club requested this one. No need to put too much thought, those women have no taste. %s.",
    "Make me tingle like John Travolta did in Saturday Night Fever. %s.",
    "The country club is having a crazy painting contest. Help me out? %s.",
    "My pool boy said that painting is “in” right now. %s."
]

sentencesLower = [
"Hello again. After some consideration, I decided to burn the last art piece I bought from this server. I'm in need of another piece. Please %s.",
"If I don't get this Makeing, I feel as if I'm going to die. Please %s.",
"My son just got into Yale! I was thinking of getting him some sort of art piece. Please %s.",
"Please %s. I'll have my people pick it up in a couple of weeks.",
"No price is too high! Please %s.",
"I can tell that you are all are amateur artists from the moment I walked in. No matter, you all come highly recommended. Please %s.",
"I'm looking for a painting that will go in my Chihuahua, Snickers, dog house. Please %s.",
"If I wasn’t too busy knitting, I would reach out to a real artist. But, since you’re here, %s",
"Hello can you %s. Just please don’t reuse whatever technique you tried last time. . .thanks.",
"I'm missing my morning crumpets and tea session to be here. Please %s.",
"My husbands out hunting in the safari again. I thought I was spend my time shopping. Please %s before I die in the presence of amateurs.",
"I'm looking for a gift to give my least favorite grandchild. Please %s.",
"I’ll make you a deal, if you %s, and I won’t tell people about the monstrosity you made last time.",
"I studied art in the 50s, way more class in those days. Nevertheless, %s.",
]

reminders = [
    "I'll be by next week in order to pick up my painting.",
    "I can see that my purchasing options so far are absolutely horrendus. I'll give you until next week to make this right.",
    "I'll postpone my husband's funeral and I'll stop by next week.",
    "My people will be here next week to pick up the art piece on my behalf.",
    "This is all you people have been able to mustard up so far? I sure hope you'll have something better by next week.",
    "These art pieces better not be for me. I'll give you more time to turn this trash around.",
    "At this rate, you all are being out performed by Hellen Keller. I'll be here next week to pick up my painting.",
    "No, no, no... all wrong. Start over. I'll give you one more week.",
    "My chihuahua is displeased with these options. I hope these aren't the final piece. I'll be back next week for my painting.",
    "Did you understand what I asked of you? Get back to it. One more week.",
    "I said I wanted art, not all *this*! I'll be back in a week for it..."
]

webhook = 'https://discordapp.com/api/webhooks/725177156971528243/ulsunB6BNMHwapU5X0F47INHQW2wrIbeRRqn35GgY5v2naP82W9yccjjREyUAV2Z-Mnm'
dayOfWeek = numberToDayofWeek(datetime.datetime.today().weekday())
if dayOfWeek == "Saturday" and (int(datetime.datetime.today().strftime("%V")) % 2 == 0): #if its friday and the week is divisible by 2

    categories = ["upper", "lower"]
    picker = random.choice(categories)

    if picker is "upper":
        prompt = random.choice(prompts)
        choice = random.choice(sentencesUpper) % (prompt)
    else:
        prompt = random.choice(prompts).lower()
        choice = random.choice(sentencesLower) % (prompt)

    webhook = DiscordWebhook(url=webhook, content=choice)
    response = webhook.execute()

elif dayOfWeek == "Friday" and not (int(datetime.datetime.today().strftime("%V")) % 2 == 0): #if its friday and the week is NOT divisible by 2
    webhook = DiscordWebhook(url=webhook, content=random.choice(reminders))
    response = webhook.execute()