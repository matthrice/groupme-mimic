# settings.py
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# OR, the same with increased verbosity:
load_dotenv(dotenv_path, verbose=True)

TOKEN = os.environ.get("TOKEN")
GROUP_ID = os.environ.get("GROUP_ID")
USER_ID = os.environ.get("USER_ID")