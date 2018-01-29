"""
bot.py

GroupMe API request module for registering and writing to bots
"""

import requests
import json
from lib.scrape.groupme import get_groupme_info


def register_bot(token, group_name, user_name, bot_name):
	"""
	Register the bot through Groupme API. Returns a token for the bot

	Params:
		@token - GroupMe token
		@group_name - current name of the GroupMe group
		@user_name - current name of user in group above
		@bot_name - desired name for bot

	Returns:
		{ chat_id, user_id, bot_id } - ids for use rather than names

	"""
	URL = "https://api.groupme.com/v3/bots?token={}".format(token)
	chat_id, user_id = get_groupme_info(token, group_name, user_name)

	bot_data = {
		"bot": {
			"name" : bot_name,
			"group_id" : chat_id
		}
	}
	try:
		res = requests.post(URL, data=json.dumps(bot_data));
	except requests.exceptions.HTTPError as e:
		print("Error: " + str(e))
		exit(1)

	json_obj = res.json()
	return {
		'chat_id': chat_id,
		'user_id': user_id,
		'bot_id': json_obj['response']['bot']['bot_id']
	}

def write_message(bot_id, message):
	"""
	Send a message into the defined group using Groupme API

	Params:
		@bot_id - ID of the registered bot
		@message - message to be sent by the bot
	"""

	URL = "https://api.groupme.com/v3/bots/post"
	bot_data = {
		"bot_id": bot_id,
		"text": message
	}
	try:
		res = requests.post(URL, data=json.dumps(bot_data))
	except requests.exceptions.HTTPError as e:
		print("Error: " + str(e))
		exit(1)

