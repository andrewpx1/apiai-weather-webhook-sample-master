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
	result = req.get("result")
	parameters = result.get("parameters")
	prt = parameters.get("any")
	yurt = parameters.get("any1")	
    baseurl = "https://love-calculator.p.mashape.com/getPercentage?"
    mydict1 = {'fname': prt}
	mydict2 = {'sname': yurt}
	put1 = urlencode(mydict1)
	put2 = urlencode(mydict2)
	url = baseurl + put1 + '&' + put2
	headers = {
	    "X-Mashape-Key": "axWE0J6Hj5mshIyeWhO19vjpSYyxp1k53ohjsnr3rxp4xsIj8I",
	    'Accept': 'application/json'
	}
	r = requests.get(url, headers=headers)
	gh = r.content
	poke = gh.decode()
	toke = json.loads(poke)
	perc = toke.get('percentage')
	resl = toke.get("result")
	joke = prt + ' & ' + yurt + '\nYour Love Percentage is = ' + perc + ' % \nSo, You ' + resl
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
