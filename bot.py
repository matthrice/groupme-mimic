import requests
from lib.scrape.groupme import get_groupme_info
from settings import GLOBALS, BOT


def register_bot(token, group_name, user_name, bot_name, avatar_url):
	"""Register the bot through Groupme API. Returns a token for the bot"""
	URL = "https://api.groupme.com/v3/bots?token={}".format(token)
	chat_id, user_id = get_groupme_info(token, group_name, user_name)
	bot_data = {
		"bot" : {
			"name" : bot_name,
			"group_id" : chat_id
		}
	}

	res = requests.post(URL, data=bot_data);
	json = res.json()
	print(json)
	return json['response']['bot_id'];

def write_message(bot_id, message):
	"""Send a message into the defined group using Groupme API"""

	URL = "https://api.groupme.com/v3/bots/post"
	bot_data = {
		"bot_id": bot_id,
		"text": message
	}

	requests.post(URL, bot_data)