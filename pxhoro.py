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
import requests

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


def processRequest(req):
    result = req.get("result")
    parameters = result.get("parameters")
    prt = parameters.get("Zodiac")
    baseurl = "https://new.theastrologer.com/"
    url = baseurl + prt + '/'
    headers = {}
    hj = requests.get(url, headers=headers)
    gh = hj.content
    cbt = gh.decode()
    dbt = '<p>(.+?)</p>'
    ebt = re.findall(dbt,cbt)
    xbt = ebt[0]
    aat = '<div class="daily-horoscope-date">(.+?)</div>'
    bbt = re.findall(aat,cbt)
    u1 = str(bbt[2])
    u2 = u1.replace("<sup>", "")
    u3 = u2.replace("</sup>", "")
    joke = 'Zodiac Sign : ' + prt + '\nDate : ' + u3 + '\nResult : ' + xbt 

    # print(json.dumps(item, indent=4))
	
    speech = joke

    print("Response:")
    print(speech)


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
