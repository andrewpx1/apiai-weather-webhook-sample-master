#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext

import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    baseurl = "http://www.rabbit.org/fun/net-bunnies.html"
    site = urlopen(baseurl)
    sitee = site.read()
    res = makeWebhookResult(data)
    return res
	
	
def makeWebhookResult(data):
    splitted_text = sitee.split("http://www.rabbit.org/graphics/fun/netbunnies/", 1);
    splitted_text = splitted_text[1].split('">')
    rmn = splitted_text[0]
    dlink = "http://www.rabbit.org/graphics/fun/netbunnies/" + rmn
    joke = dlink

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
