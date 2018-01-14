"""
Script to generate groupme history

Access token from: https://dev.groupme.com/
"""

import os
import time

import requests
import requests_cache
from json import load

TOKEN = 'b9rW31lfwxhnxLHWt0M86sAqjfVTtdu2KFQEXffO'
LIST_CERF_ID = '28057504'
BAKER_ID = '20810670'

MESSAGE_LIMIT = 100

requests_cache.install_cache('groupme_cache')


def check_token(token):
    """Check the validity of the access token."""
    try:
        get_self_id(token)
        valid = True
    except:
        valid = False
        
    return valid


def get_url(token, chat_type, chat_ID):
    """Retrieve url for chat"""
    if chat_type == 'group':
        url = 'https://api.groupme.com/v3/groups/{}/messages'.format(chat_ID)
        url += "?token={}".format(token)
    elif chat_type == 'direct':
        url = 'https://api.groupme.com/v3/direct_messages'
        url += '?other_user_id={}'.format(chat_ID)
        url += "&token={}".format(token)
    
    url += "&limit={}".format(MESSAGE_LIMIT)

    return url

def get_json(url):
    """Retrieve json from url"""
    res = requests.get(url=url)
    json = res.json()

    return json

def get_chat_id(token):
    print(get_json('https://api.groupme.com/v3/groups?token={}'.format(token)))
    

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

def create_history(id, json, url, chat_type, chat_ID, msg_count, msg_limit):
    """ Create a full chat history for a specific 
    
    @name - name of person 
    @json - GroupMe API response in JSON format
    @url - URL being worked with
    @chat_type - the type of chat ('group' or 'direct')
    @chat_id - the chat's id
    @msg_count - total number of messages in the chat
    """

    msg = ''
    if chat_type == 'group':
        msg = 'messages'
    elif chat_type == 'direct':
        msg = 'direct_messages'
    history = []
    #Get date of most recent message
    initial_time = json['response'][msg][0]['created_at']
    old_date = time.strftime('%A, %d %B %Y', time.localtime(initial_time))

    while msg_count > 0:
        if msg_count < msg_limit:
            msg_limit = msg_count % msg_limit
        
        for i in range(msg_limit):

            u_id = json['response'][msg][i]['user_id']
            if u_id == id:
                temp = {}
                temp['user_id'] = u_id
                temp['name'] = json['response'][msg][i]['name']
                text = json['response'][msg][i]['text']
                if text:
                    temp['text'] = text
                history.append(temp)
            msg_count -= 1
            if msg_count != 0 and i == msg_limit - 1:
                try:
                    before_id = json['response'][msg][i]['id']
                    new_url = "{}&before_id={}".format(url, before_id)
                    json = get_json(new_url)
                except requests.HTTPError:
                    msg_count = 0

    return history


    
def write_single_history(name, full_history):
    """Records all text from an individual in a readable format"""
    filename = 'resources/{}chathistory.txt'.format(name)
    filename = filename.replace(' ', '_')
    f = open(filename, 'w')

    for message in full_history:
        if 'text' in message:
            text = message['text']
            text = clean_message(text)
            f.write(text)
    
    f.close()

def clean_message(text):
    text = text.replace('@', '') # remove @ symbols
    text = text.replace('*', '') # remove * symbols
    text = text.strip(' ')          # strip whitespace
    if text[-1] != '.':   # add period to end
        text += '.'
    text = ' ' + text     # add space to beginning
    print(text)
    return text

def test_baker():
    url = get_url(TOKEN, 'group', LIST_CERF_ID)
    i_json = get_json(url)
    history = create_history(BAKER_ID, i_json, url, 'group', LIST_CERF_ID, 10000, MESSAGE_LIMIT)
    write_single_history('baker', history)

test_baker() 