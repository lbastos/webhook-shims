#!/usr/bin/env python

"""
Create an incoming webhook for Google Chat

http://XXXXXX:5001/v1/spaces/XXXXXX/messages/XXXXXXXX/XXXXXXXX
"""

from loginsightwebhookdemo import app, parse, callapi
from flask import request, json


@app.route("/v1/spaces/<SPACEID>/messages/<APPKEY>/<TOKEN>", methods=['POST'])
def gchat(APPKEY=None, TOKEN=None, SPACEID=None):
    """
    Posts a message to a Google Chat channel. Set CHATURL to the incoming
    webhook URL provided by gChat. To create a Chat webhook see:
    """
    if not TOKEN:
        return ("TOKEN must be set in the URL (e.g. /v1/spaces/<SPACEID>/messages/<TOKEN>/<APPKEY>", 500, None)
    if not APPKEY:
        return ("APPKEY must be set in the URL (e.g. /v1/spaces/<SPACEID>/messages/<TOKEN>/<APPKEY>", 500, None)

    GCHATURL = 'https://chat.googleapis.com/v1/spaces/%s/messages?key=%s&token=%s' % (SPACEID, APPKEY, TOKEN)

    a = parse(request)

    payload = {
    "text": a['moreinfo']
    }

    # Defaults to Content-type: application/json
    # If changed you must specify the content-type manually
    headers = {'Content-type': 'application/json', 'Accept': 'application/json'}
    if not headers:
        headers = None
    return callapi(GCHATURL, 'post', json.dumps(payload), headers)
