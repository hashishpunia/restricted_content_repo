# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "23370661"))
API_HASH = getenv("API_HASH", "18136a71a26e067dd7ee4749fefd6af0")
BOT_TOKEN = getenv("BOT_TOKEN", "7212422700:AAFlEMD_TVcWCAAxlSlurbZIuCKAo4XPGuw")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7204450080").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002419891609"))
