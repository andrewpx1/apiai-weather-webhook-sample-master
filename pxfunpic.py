#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

import json
import os
import urllib
import re

from re import findall
from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__) 
 

def processRequest(req):
   baseurl = "http://www.funcage.com/"
   site = urlopen(baseurl)
   htmltxt = site.read()
   lnb = htmltxt.decode()
   txt = '<img src="/photos/(.+?)"'
   title1 = findall(txt,lnb)
   dcd = title1[0]
   body = '"http://www.funcage.com/photos/' + dcd + '"'
   obje = '{"file":' + body +'}'
   data = json.loads(obje)
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
