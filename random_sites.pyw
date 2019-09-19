import random
import webbrowser
import time

random_sites = ['https://www.youtube.com/pewdiepie', 'https://www.twitch.tv', 'https://mail.google.com/mail/u/0/#inbox', 'https://facebook.com']

while True:
    time.sleep(random.randint(10,30))
    webbrowser.open(random.choice(random_sites))
