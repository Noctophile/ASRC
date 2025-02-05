# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21857983"))
API_HASH = getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
BOT_TOKEN = getenv("BOT_TOKEN", "7267580651:AAGHCvFRaBWBHpOy49JKeGYzYrnbZp8eylY")
OWNER_ID = list(map(int, getenv("OWNER_ID", "833465134").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://saverestricted:rizzstore@cluster0.jfjt3.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002164681451")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002319834974"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "10"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "500"))
WEBSITE_URL = getenv("WEBSITE_URL", "get2short.com")
AD_API = getenv("AD_API", "0ca9d7c312e534b02d74e95bef7eb06a11dd0314")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", None)
INSTA_COOKIES = getenv("INSTA_COOKIES", None)
