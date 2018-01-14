"""Main file to tie markov chaining and groupme scraping together"""
import os
import lib.markov.model as mod
import lib.markov.generate as gen
import lib.scrape.groupme as gm
from settings import TOKEN, GROUP_ID, USER_ID

'''
Parameters to perform task:

@token: dev groupme token
@group_id: groupme group id
@user_id: groupme user_id
@msg_count: desired number of messages to go through
@msg_limit: set at 100
@name: (no spaces) used for filenaming
'''

# url = get_url(TOKEN, 'group', LIST_CERF_ID)
# i_json = get_json(url)
# history = create_history(BAKER_ID, i_json, url, 'group', LIST_CERF_ID, 10000, MESSAGE_LIMIT)
# write_single_history('baker', history)
