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
    trt = zodsign(prt)
    baseurl = "https://new.theastrologer.com/"
    url = baseurl + prt + '/'
    hj = urlopen(url)
    gh = hj.read()
    cbt = gh.decode()
    dbt = '<p>(.+?)</p>'
    ebt = re.findall(dbt,cbt)
    xbt = ebt[5]
    aat = '<div class="daily-horoscope-date">(.+?)</div>'
    bbt = re.findall(aat,cbt)
    u1 = str(bbt[1])
    u2 = u1.replace("<sup>", "")
    u3 = u2.replace("</sup>", "")
    joke = 'Zodiac Sign : ' + prt + ' ' + trt  '\nDate : ' + u3 + '\nResult :' + '\n' + xbt
    # print(json.dumps(item, indent=4))
    speech = joke

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        #"data": {"kik": kik_message},
        # "contextOut": [],
        "source": "apiai-weather-webhook-sample"
    }


def zodsign(prt):
    if (prt == "Aries"):
        return "♈ "
    elif (prt == "Taurus"):
        return "♉ "
    elif (prt == "Gemini"):
        return "♊ "
    elif (prt == "Cancer"):
        return "♋ "
    elif (prt == "Leo"):
        return "♌ "
    elif (prt == "Virgo"):
        return "♍ "
    elif (prt == "Libra"):
        return "♎ "
    elif (prt == "Sagittarius"):
        return "♐ "
    elif (prt == "Capricorn"):
        return "♑ "
    elif (prt == "Aquarius"):
        return "♒ "
    elif (prt == "Pisces"):
        return "♓ "
    if (prt == "aries"):
        return "♈ "
    elif (prt == "taurus"):
        return "♉ "
    elif (prt == "gemini"):
        return "♊ "
    elif (prt == "cancer"):
        return "♋ "
    elif (prt == "leo"):
        return "♌ "
    elif (prt == "virgo"):
        return "♍ "
    elif (prt == "libra"):
        return "♎ "
    elif (prt == "sagittarius"):
        return "♐ "
    elif (prt == "capricorn"):
        return "♑ "
    elif (prt == "aquarius"):
        return "♒ "
    elif (prt == "pisces"):
        return "♓ " 
    else:
        return {}

 
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
