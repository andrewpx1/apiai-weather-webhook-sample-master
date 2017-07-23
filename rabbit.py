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
import urllib

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
	baseurl = "http://www.rabbit.org/fun/net-bunnies.html"
	result = urllib.urlopen(baseurl).read()
	plitext = result.split("http://www.rabbit.org/graphics/fun/netbunnies/", 1);
	plitext = plitext[1].split('">')
	rmn = plitext[0]
	dlink = "http://www.rabbit.org/graphics/fun/netbunnies/" + rmn
	payload = {
		"file": dlink
	}
	jsondata = json.dumps(payload)
	jsnb = jsondata.encode('utf-8')
	data = json.loads(jsnb)
	res = makeWebhookResult(lol)
	return res
	
	
def makeWebhookResult(lol):
    joke = data.get('file')

    # print(json.dumps(item, indent=4))
	
    speech = joke

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": {"kik": kik_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
