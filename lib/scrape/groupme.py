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

def get_json(url):
    """Retrieve json from url"""
    res = urllib2.urlopen(url)
    json = load(res)

    return json

def get_self_id(token):
    """Obtain a user's ID given token"""
    url = "https://api.groupme.com/v3/users/me?token={}".format(token)
    json = get_json(url)
    user_id = json['response']['user_id']

    return user_id

def get_groups(token):
    """Return a list of group chats' IDs and names."""
    url = 'https://api.groupme.com/v3/groups?token={}'.format(token)
    json = get_json(url)
    response = json['response']
    
    groups = []
    for i in response:
        ID = i['id']
        name = i['name']
        groups.append([ID, name])

    return groups

def get_directs(token):
    """Return a list of direct message chats' IDs and names."""
    url = 'https://api.groupme.com/v3/chats?token={}'.format(token)
    json = get_json(url)
    response = json['response']
    
    directs = []
    for i in response:
        ID = i['other_user']['id']
        name = i['other_user']['name']
        directs.append([ID, name])

    return directs

def create_history(json, url, self_id, chat_type, chat_ID, msg_count, msg_limit):
    """ Create a full chat history

    @json - GroupMe API response in JSON format
    @url - URL being worked with
    @self_id - user's GroupMe ID
    @chat_type - the type of chat ('group' or 'direct')
    @chat_id - the chat's id
    @msg_count - total number of messages in the chat
    @msg_limit - number of messages received in a set
    """

    


    


