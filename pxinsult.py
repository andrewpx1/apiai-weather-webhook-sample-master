#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext
from random import randint

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    seconds = randint(0, 60)
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("any")
    trt = parameters.get("px")
    poke = "You " + RandomNeutral(seconds) + RandomEnd(seconds) + RandomFemale(seconds) + RandomStupid(seconds) + RandomSkinny(seconds) +  RandomDog(seconds) + RandomIntenseEnd(seconds) + RandomFat(seconds) + RandomMale(seconds)
    joke = trt + prt + ' , ' + poke + " 😂😂😂"
    speech = joke

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


def RandomMale(seconds):
	if (seconds < 6):
		return "dick "
	elif (seconds < 11):
		return "bastard "
	elif (seconds < 16):
		return "sperm-bank "
	elif (seconds < 21):
		return "dickwad "
	elif (seconds < 26):
		return "dickhead "
	elif (seconds < 31):
		return "penis "
	elif (seconds < 35):
		return "ape "
	elif (seconds < 40):
		return "weiner "
	elif (seconds < 44):
		return "pecker "
	elif (seconds < 48):
		return "prick "
	elif (seconds < 52):
		return "jerk-off "
	elif (seconds < 56):
		return "schmuck "
	elif (seconds < 61):
		return "arsehole collector "
	else:
		return " "

		
def RandomFemale(seconds):
	if (seconds < 6):
		return "hag "
	elif (seconds < 11):
		return "wench "
	elif (seconds < 16):
		return "bitchwad "
	elif (seconds < 21):
		return "shrew "
	elif (seconds < 26):
		return "tramp "
	elif (seconds < 31):
		return "slut "
	elif (seconds < 36):
		return "bitch "
	elif (seconds < 41):
		return "bimbo "
	elif (seconds < 46):
		return "tart "
	elif (seconds < 51):
		return "scuz-bag "
	elif (seconds < 56):
		return "floozy "
	elif (seconds < 61):
		return "douche bag "
	else:
		return " "

		
def RandomNeutral(seconds):
	if (seconds < 6):
		return "pukebreath "
	elif (seconds < 11):
		return "frotterist "
	elif (seconds < 16):
		return "bumwipe "
	elif (seconds < 21):
		return "rectum-head "
	elif (seconds < 26):
		return "asshole "
	elif (seconds < 31):
		return "assface "
	elif (seconds < 36):
		return "vomit-face "
	elif (seconds < 41):
		return "coprophagiac "
	elif (seconds < 46):
		return "pukestick "
	elif (seconds < 51):
		return "twit "
	elif (seconds < 56):
		return "loser "
	elif (seconds < 61):
		return "smeghead "
	else:
		return " "

		
def RandomStupid(seconds):
	if (seconds < 4):
		return "dumbshit "
	elif (seconds < 8):
		return "cerebrally-challenged "
	elif (seconds < 12):
		return "brain-dead "
	elif (seconds < 16):
		return "vacuous "
	elif (seconds < 20):
		return "witless "
	elif (seconds < 24):
		return "airheaded "
	elif (seconds < 28):
		return "moronic "
	elif (seconds < 32):
		return "pea-brained "
	elif (seconds < 36):
		return "nit-witted "
	elif (seconds < 41):
		return "chicken-brained "
	elif (seconds < 47):
		return "obtuse "
	elif (seconds < 53):
		return "idiotic "
	elif (seconds < 61):
		return "dense "
	else:
		return " "
		
		
def RandomFat(seconds):
	if (seconds < 5):
		return "fat-ass "
	elif (seconds < 11):
		return "chubby "
	elif (seconds < 17):
		return "pork-bellied "
	elif (seconds < 23):
		return "portly "
	elif (seconds < 29):
		return "corpulent "
	elif (seconds < 35):
		return "obese "
	elif (seconds < 42):
		return "bovine "
	elif (seconds < 48):
		return "cow-like "
	elif (seconds < 53):
		return "fat "
	elif (seconds < 58):
		return "rotund "
	elif (seconds < 61):
		return "pudgy "
	else:
		return " "

		
def RandomSkinny(seconds):
	if (seconds < 4):
		return "pencil-necked "
	elif (seconds < 8):
		return "emaciated "
	elif (seconds < 12):
		return "anorexic "
	elif (seconds < 16):
		return "puny "
	elif (seconds < 20):
		return "bony "
	elif (seconds < 24):
		return "scrawny-assed "
	elif (seconds < 28):
		return "cum graduated "
	elif (seconds < 32):
		return "frigging gaylord extracting "
	elif (seconds < 36):
		return "cross-eyed asswad twat experimented "
	elif (seconds < 40):
		return "lonely sack graduated "
	elif (seconds < 44):
		return "dumb shitfaced "
	elif (seconds < 48):
		return "shitting clusterfuck "
	elif (seconds < 52):
		return "flip-flopping skinny dick  "
	elif (seconds < 56):
		return "dried out tea-bag licking "
	elif (seconds < 61):
		return "vomit bollock bony "
	else:
		return " "

		
def RandomDog(seconds):
	if (seconds < 8):
		return "butt-ugly "
	elif (seconds < 15):
		return "puke-inducing "
	elif (seconds < 23):
		return "barforific "
	elif (seconds < 31):
		return "ugolicious "
	elif (seconds < 41):
		return "vomitrocious "
	elif (seconds < 49):
		return "up-chuck-inspiring "
	elif (seconds < 55):
		return "zit-faced "
	elif (seconds < 61):
		return "pus-lipped "	
	else:
		return " "

		
def RandomIntenseEnd(seconds):
	if (seconds < 4):
		return "smelly-crotched "
	elif (seconds < 8):
		return "hog-humping "
	elif (seconds < 12):
		return "rectum-sniffing "
	elif (seconds < 16):
		return "smegging "
	elif (seconds < 20):
		return "butt-licking "
	elif (seconds < 24):
		return "badly drawn nut fondling "
	elif (seconds < 28):
		return "glorious cockstorm foot packing "
	elif (seconds < 32):
		return "mental erection sniffing "
	elif (seconds < 36):
		return "hard-rubbing clotpole wanking "
	elif (seconds < 40):
		return "bukake licking "
	elif (seconds < 44):
		return "twittering puke handler "
	elif (seconds < 48):
		return "overrated scrotum bucket detecting "
	elif (seconds < 52):
		return "stale bunghole sniffing "
	elif (seconds < 56):
		return "scurvy looking "
	elif (seconds < 58):
		return "nipple spunk-bubble "
	elif (seconds < 61):
		return "hairy chesticle licking "
	else:
		return " "

	
def RandomEnd(seconds):
	if (seconds < 3):
		return "turd-like "
	elif (seconds < 6):
		return "crud-infested "
	elif (seconds < 9):
		return "lame "
	elif (seconds < 12):
		return "vermin-ridden "
	elif (seconds < 15):
		return "pus-sucking "
	elif (seconds < 16):
		return "fart-sniffing "
	elif (seconds < 19):
		return "indeterminable semen goatse jacker "
	elif (seconds < 22):
		return "offspring of a motherless goat "
	elif (seconds < 25):
		return "Harambe fucked "
	elif (seconds < 28):
		return "anus raped "
	elif (seconds < 32):
		return "undead fuck piped "
	elif (seconds < 40):
		return "annoying arse shiner, "
	elif (seconds < 44):
		return "failed slut wagon dictator, "
	elif (seconds < 48):
		return "colon bender, "
	elif (seconds < 52):
		return "poop balls, "
	elif (seconds < 56):
		return "instant tit testicle basher, "
	elif (seconds < 61):
		return "maiming cock jockey, "
	else:
		return " "


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
