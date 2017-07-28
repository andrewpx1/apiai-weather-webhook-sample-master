#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from random import randint

import json
import os
import re

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("any")
    baseurl = "http://www.memes.com/search/"
    mydict = {'': prt}
    put = urlencode(mydict)
    num1 = 1
    num2 = randint(0, 4)
    url = baseurl + put + '/' + str(num1)
    hj = urlopen(url)
    gh = hj.read()
    cbt = gh.decode()
    dbt = 'id="image_(.+?)"'
    ebt = re.findall(dbt,cbt)
    fbt = ebt[num2]
    xurl = "http://images.memes.com/meme/"
    poke = xurl + fbt
    toke = '{"file":"' + poke + '"}'
    data = json.loads(toke)
    res = makeWebhookResult(data)
    return res
	
	
def makeWebhookResult(data):
    joke = data.get('file')

    # print(json.dumps(item, indent=4))
	
    speech = joke

    print("Response:")
    print(speech)


    kik_message = [
            {
                "type": "picture",
                "picUrl": speech
            }
    ]

    #kik_message2 = [
            #{
                #"type": "video",
                #"videoUrl": speech
            #}
    #]

    print(json.dumps(kik_message))
    #print(json.dumps(kik_message2))

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
