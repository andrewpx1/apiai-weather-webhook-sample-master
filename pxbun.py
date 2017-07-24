#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

import json
import os
import urllib

from re import findall
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__) 
   

baseurl = "http://www.rabbit.org/fun/net-bunnies.html"
site = urllib.urlopen(baseurl)
htmltxt = site.read()
lnb = htmltxt.decode()
txt = 'http://www.rabbit.org/graphics/fun/netbunnies/(.+?)">'
title1 = findall(txt,lnb)
dcd = title1[0]
link = "http://www.rabbit.org/graphics/fun/netbunnies/" + dcd


def processRequest(req):
   joke = link
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
