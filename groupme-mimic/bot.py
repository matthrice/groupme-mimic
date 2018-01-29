import requests
import json
from lib.scrape.groupme import get_groupme_info


def register_bot(token, group_name, user_name, bot_name, avatar_url):
	"""Register the bot through Groupme API. Returns a token for the bot"""
	URL = "https://api.groupme.com/v3/bots?token={}".format(token)
	chat_id, user_id = get_groupme_info(token, group_name, user_name)
	bot_data = {
		"bot": {
			"name" : bot_name,
			"group_id" : chat_id
		}
	}
	res = requests.post(URL, data=json.dumps(bot_data));
	json_obj = res.json()
	return {
		'chat_id': chat_id,
		'user_id': user_id,
		'bot_id': json_obj['response']['bot']['bot_id']
	}

def write_message(bot_id, message):
	"""Send a message into the defined group using Groupme API"""

	URL = "https://api.groupme.com/v3/bots/post"
	bot_data = {
		"bot_id": bot_id,
		"text": message
	}

	res = requests.post(URL, data=json.dumps(bot_data))

def destroy_bot(bot_id):
	URL = "https://api.groupme.com/v3/bots/destroy"
	bot_data = {
		"bot_id" : bot_id
	}

	res = requests.post(URL, data=json.dumps(bot_data))
