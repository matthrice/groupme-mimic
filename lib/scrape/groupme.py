"""
Script to generate groupme history

Access token from: https://dev.groupme.com/
"""

import os
import time

import urllib2
from json import load

message_limit = 100

def get_url(token, chat_type, chat_ID):
    """Retrieve url for chat"""
    if chat_type == 'group':
        url = 'https://api.groupme.com/v3/groups/{}/messages'.format(chat_ID)
        url += "?token={}".format(token)
    elif chat_type == 'direct':
        url = 'https://api.groupme.com/v3/direct_messages'
        url += '?other_user_id={}'.format(chat_ID)
        url += "&token={}".format(token)
    
    url += "&limit={}".format(message_limit)

    return url


