#!/usr/bin/env python

from os.path import splitext
import urllib
import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
	url = "http://www.rabbit.org/fun/net-bunnies.html"
	result = urllib.urlopen(url).read()
	reg = 'http://www.rabbit.org/graphics/fun/netbunnies/(.+?)">'
	pat = re.compile(reg)
	pri = re.findall(pat,result)
	joke = "http://www.rabbit.org/graphics/fun/netbunnies/" + pri[0]
		
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
