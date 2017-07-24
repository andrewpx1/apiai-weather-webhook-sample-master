#!/usr/bin/env python

from __future__ import print_function
from future.standard_library import install_aliases
install_aliases()

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from os.path import splitext

import urllib
import json
import os
import re


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
