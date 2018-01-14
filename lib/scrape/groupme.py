"""
Script to generate groupme history

Access token from: https://dev.groupme.com/
"""

import os
import time

import requests
from json import load

TOKEN = 'b9rW31lfwxhnxLHWt0M86sAqjfVTtdu2KFQEXffO'
LIST_CERF_ID = '28057504'
BAKER_ID = '212697597'

MESSAGE_LIMIT = 100


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
        print(msg_count)

        if msg_count < msg_limit:
            msg_limit = msg_count % msg_limit
        
        for i in range(msg_limit):
            try: 
                epoch_time = json['response'][msg][i]['created_at']
            except IndexError:
                msg_count = 0
                break
        date = time.strftime('%A, %d %B %Y', time.localtime(epoch_time))

        u_id = json['response'][msg][i]['id']
        if u_id == id:
            history.append({
                user_id: u_id,
                name: json['response'][msg][i]['name'],
                hour: time.strftime('%H:%M:%S', time.localtime(epoch_time)),
                text: json['response'][msg][i]['text'].encode('unicode-escape')
            })
        msg_count -= 1

    return history


    
def write_single_history(name, full_history):
    """Records all text from an individual in a readable format"""
    filename = 'resources/{}_chat_history.txt'.format(name)
    filename = filename.replace(' ', '_')
    f = open(filename, 'w')

    for message in full_history:
        print(message)
        text = message[text]
        if text[-1] != '.':
            text += '.'
        f.write(text)
    
    f.close()

def test_baker():
    url = get_url(TOKEN, 'group', LIST_CERF_ID)
    i_json = get_json(url)
    history = create_history(BAKER_ID, i_json, url, 'group', LIST_CERF_ID, 100, MESSAGE_LIMIT)
    write_single_history('baker', history)

test_baker() 