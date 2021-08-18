from random import choice

from django.shortcuts import render

# Create your views here.
people = [
    "Luke",
    "Nena",
    "Jane",
    "Marc",
    "Ruth",
    "Nils",
    "Eric",
    "Lana",
]
likes = [
    "Fortnight",
    "Valorant",
    "Minecraft",
    "Agario",
    "CSGO",
    "Slitherio",
    "boogers",
    "tooting",
    "bathing",
    "donkeys",
    "small chickens",
    "zebras",
    "Demon Slayer",
    "donuts",
    "dairy queen",
]

actions = [
    "smelling",
    "walking",
    "talking",
    "sitting",
    "typing sentences",
    "listening",
    "doing a dance",
    "hitting self",
    "breaking",
    "slapping",
    "eating",
    "looking",
    "moving"
]
joiners = [
    "like a",
    "to",
    "with",
    "with some",
    "on",
    "under",
    "about",
    "at",
    "a"
]
headers = [
    "Gaming in Austin",
    "Movies in San Antonio",
    "Ping Pong in Tokyo",
    "Cooking in Paris",
    "Music in Italy",
    "Soccer in Mexico",
    "Sport in Indonesia",
]

contents = [
    "Blah blah blah this is soo boring",
    "Oh wait this is awesome and we have new news for you!!!",
    "E-e-e-e--eeverything is Awesome, when you're part of a team!",
    "E-e-e-e-e-e-everything is Aweome, when you're livin' your dream!",
    "Nightmares all around! Save me-e-e-e-e--e-e-e-ee-eeeeee!",
]

prefers = [
    "likes",
    "hates",
]

names = [
    "Josh",
    "Drake",
    "mike",
    "Luke",
    "Marc",
    "Tom",
    "Zach",
    "Nils",
    "Nick",
    "Connor",
]

greetings = [
    "Welcome to Rant",
    "Thank you for coming",
    "Hey welcome!!",
    "Hello this is are headquarters",
    "Hey welcome this is are secret hideout",
    "Welcome noobie",
    "Oh didn't see you there welcome to are place",
    "hey there Welcome",
    "Welcome to Donut Palace",
    "Welcome to king's burger's fries and shake's",

]

def index(request):
    context = {
        "title": f"{choice(people)} {choice(prefers)} {choice(actions)} {choice(joiners)} {choice(likes)}",
        "header": choice(headers),
        "content": "hello I am content wooo hoo",
    }
    return render(request, 'index.html', context=context)


def page(request):
    context = {
        "greeting": choice(greetings),
        "name": choice(names),
        "what": choice(likes)
    }

    return render(request, "page.html", context=context)


# Hello {{ name }}
# {{ Greeting }}
    # Here love to rant about {{ what }}!
