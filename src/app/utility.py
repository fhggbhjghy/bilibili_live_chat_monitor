from bilibili_api import Credential
from dotenv import load_dotenv, set_key
from json import loads, dumps
from pathlib import Path
import os
import logging

# Start logger
logger = logging.getLogger(__name__)

# Define .env path
env_path = Path('.') / 'src/.env'

# Parse and stores login cookies to obtain user credentials
def is_logged_in(instruction = 1):

    # Load from env
    load_dotenv(dotenv_path=env_path)

    # Attempt to grab existing cookies stored in .env
    cookies = os.getenv('cookies')
    if cookies and instruction:
        try:
            parsed_cookies = loads(cookies)
            return parsed_cookies
        except Exception as e:
            logger.info(e)
            print(e)

    instruction = 1
    # Prompt user to enter cookies
    print('Login Failed\n')
    raw_cookies = input('import cookies')
    cookies = {}

    # Parses cookies for key-value pairs
    for raw_cookie in raw_cookies.split('; '):
        content = raw_cookie.split('=')
        key = content[0].lower()
        value = content[-1]
        cookies[key] = value
    
    # Store cookies in env and returns
    set_key(env_path, 'cookies', dumps(cookies))
    return cookies

# Generate credentials to unlock full api functionality
def get_credentials():
    
    # Grab cookies
    cookies = is_logged_in()

    # Generate credential
    try:
        return Credential(
            sessdata=cookies['sessdata'],
            bili_jct=cookies['bili_jct'],
            buvid3=cookies['buvid3'],
            buvid4=cookies['buvid4'],
            dedeuserid=cookies['dedeuserid'])
    except:
        is_logged_in(0)
        return get_credentials()

# Retrieve room_display_id from env
def get_room_display_id():

    # Load from env
    load_dotenv(dotenv_path=env_path)

    # Attempt to grab room_display_id
    room_display_id = os.getenv('room_display_id')

    # On fail request user to input room_display_id
    if not room_display_id:
        return change_room_display_id()
    return int(room_display_id)

# Change room_display_id
def change_room_display_id():

    # Request valid room_display_id inputs 
    try:
        room_display_id = int(input('enter target room_display_id\n'))
        set_key(env_path, 'room_display_id', f'{room_display_id}')
        return room_display_id
    
    # Recursive call until valid id is acquired
    except Exception as e:
        logger.info(e)
        print(e)
        return change_room_display_id()


    