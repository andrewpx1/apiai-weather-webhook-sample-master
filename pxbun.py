#!/usr/bin/env python

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
