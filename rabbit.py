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
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    res = makeWebhookResult(data)
    return res
	
	
def makeWebhookResult(data):
	url = "http://www.rabbit.org/fun/net-bunnies.html"
	regex = 'http://www.rabbit.org/graphics/fun/netbunnies/(.+?)">'
	txt = re.compile(regex)
	site = urlopen(url)
	site1 = site.read()
	title1 = re.findall(txt,site1)
	title = str(title1)
	splitted_text = title.split("'", 1);
	splitted_text = splitted_text[1].split("'")
	rmn = splitted_text[0]
	link = "http://www.rabbit.org/graphics/fun/netbunnies/" + rmn
	joke = link

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
