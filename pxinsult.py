#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext
from datetime import datetime

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)

dt = datetime.now()
seconds = dt.second


def RandomMale():
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
	elif (seconds < 36):
		return "ape "
	elif (seconds < 41):
		return "weiner "
	elif (seconds < 46):
		return "pecker "
	elif (seconds < 51):
		return "prick "
	elif (seconds < 56):
		return "jerk-off "
	elif (seconds < 61):
		return "schmuck "
	else:
		return " "

		
def RandomFemale():
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

		
def RandomNeutral():
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

		
def RandomStupid():
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
		
		
def RandomFat():
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

		
def RandomSkinny():
	if (seconds < 12):
		return "pencil-necked "
	elif (seconds < 22):
		return "emaciated "
	elif (seconds < 30):
		return "anorexic "
	elif (seconds < 43):
		return "puny "
	elif (seconds < 52):
		return "bony "
	elif (seconds < 61):
		return "scrawny-assed "
	else:
		return " "

		
def RandomDog():
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

		
def RandomIntenseEnd():
	if (seconds < 15):
		return "smelly-crotched "
	elif (seconds < 23):
		return "hog-humping "
	elif (seconds < 29):
		return "rectum-sniffing "
	elif (seconds < 41):
		return "smegging "
	elif (seconds < 52):
		return "butt-licking "
	elif (seconds < 61):
		return "bum-licking "
	else:
		return " "

	
def RandomEnd():
	if (seconds < 15):
		return "turd-like "
	elif (seconds < 23):
		return "crud-infested "
	elif (seconds < 29):
		return "lame "
	elif (seconds < 41):
		return "vermin-ridden "
	elif (seconds < 52):
		return "pus-sucking "
	elif (seconds < 61):
		return "fart-sniffing "	
	else:
		return " "


def processRequest(req):
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("any")
    trt = parameters.get("px")
    poke = "You " + RandomNeutral() + RandomEnd() + RandomFemale() + RandomStupid() + RandomSkinny() +  RandomDog() + RandomIntenseEnd() + RandomFat() + RandomMale()
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


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
