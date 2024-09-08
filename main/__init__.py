#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config(66102, default=None, cast=int)
API_HASH = config("b6da542ebc418c1f282d372152d40664", default=None)
BOT_TOKEN = config("7179303938:AAGwNkCqj8pBVpM-H8rkTLWYULxjVAxgmco", default=None)
SESSION = config("BAABAjYAPnsAXsDAh-lN6sVQyBJTwOTetlPLu7P690tlBRFnSpt1nKslS_IE-3S73-qyXvxTKEFAagOIL4JTk2OexraUvQGkcrIGjiSta5Y2QIixBH-QYSVoZAvP1_xQ9rVoiGVZXQ8D2urz41big4ZH9FStVD6cqG1FgkiEWm3cEOu84-GIlt40KnkqqOXEUQPMUslHIew59_03_x3zXM612ImZ5rCWArbzR3OdTbrbrBzFzaaPBNjlPeLw-j4fb44vZm-on4kHvoznhVRKiRGuzmbGBFXSJtX1TiStEl_ZCALGBjv-vIF0qpS-EwIpHl2KqywjZWiMVdGfrhiKCYI_bijtdAAAAAGr63wCAQ", default=None)
FORCESUB = config("caronline_original", default=None)
AUTH = config(579247196, default=None, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
