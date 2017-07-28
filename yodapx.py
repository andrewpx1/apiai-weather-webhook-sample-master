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
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("any")	
    baseurl = "https://yoda.p.mashape.com/yoda?"
    mydict = {'sentence': prt}
    put = urlencode(mydict)
    url = baseurl + put
    headers = {
	    "X-Mashape-Key": "axWE0J6Hj5mshIyeWhO19vjpSYyxp1k53ohjsnr3rxp4xsIj8I",
	    "Accept": "text/plain"
    }	
    rui = requests.get(url, headers=headers)
    hj = rui.content
    joke = hj.decode()
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
