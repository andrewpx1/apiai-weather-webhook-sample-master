#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urlparse import urlparse
from os.path import splitext

import json
import os
import urllib


from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def get_ext(url):
    """Return the filename extension from url, or ''."""
    parsed = urlparse(url)
    root, ext = splitext(parsed.path)
    return ext


def processRequest(req):
    baseurl = "http://random.cat/meow"
    result = urllib.urlopen(baseurl).read()
    data = json.loads(result)
    res = makeWebhookResult(data)
    return res
	
	
def makeWebhookResult(data):
    joke = data.get('file')
    if get_ext(joke) == ".gif":
		txt = "video"
		bdy = "videoUrl"
    else:
	txt = "picture"
	bdy = "picUrl"
		
# print(json.dumps(item, indent=4))
	
    speech = joke
    text = '"' + str(txt) + '"'
    body = '"' + str(bdy) + '"'

    print("Response:")
    print(speech)

    kik_message = [
        {
            "type": text,
            body: speech
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

	
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
