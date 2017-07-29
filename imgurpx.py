#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext
from re import findall
from random import randint

import json
import os
import requests


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def scheck(easi):
    if (easi > 60):
        return 60
    else:
        return easi


def processRequest(req):
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("any")
    baseurl = "http://imgur.com/search/score?"
    mydict = {'q': prt}
    put = urlencode(mydict)
    url = baseurl + put
    headers = {}
    a = requests.get(url, headers=headers)
    b = a.content
    c = b.decode()
    d = '<span class="sorting-text-align">Found <i>(.+?)<'
    e = findall(d,c)
    eas = e[0].replace("," , "")
    easi = int(eas)
    h1 = scheck(easi)
    h2i = int(h1) + 1
    h3 = randint(0, h2i)
    h41 = 'href="/gallery/(.+?)"'
    h51 = findall(h41,c)
    h61 = h51[h3]
    nurl = 'http://imgur.com/gallery/' + h61
    a10 = requests.get(nurl, headers=headers)
    h7 = a10.content
    hdec1 = h7.decode()
    h711 = 'src="//i.imgur.com/(.+?)"'
    h721 = findall(h711,hdec1)
    h73 = h721[0]
    h74 = 'http://i.imgur.com/' + h73
    h75 = '{"file":"' + h74 + '"}'
    data = json.loads(h75)
    res = makeWebhookResult(data)
    return res
	
	
def makeWebhookResult(data):
    joke = data.get('file')

    # print(json.dumps(item, indent=4))
	
    speech = joke

    print("Response:")
    print(speech)

    if getext(joke) == ".gif":
        kik_message = [
            {
                "type": "video",
                "videoUrl": speech
            }
        ]
    elif getext(joke) == ".mp4":
        kik_message = [
            {
                "type": "video",
                "videoUrl": speech
            }
        ]
    else:
        kik_message = [
            {
                "type": "picture",
                "picUrl": speech
            }
        ]

    print(json.dumps(kik_message))

    return {
        "speech": speech,
        "displayText": speech,
        "data": {"kik": kik_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


def getext(joke):
    parsed = urlparse(joke)
    root, ext = splitext(parsed.path)
    return ext


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
