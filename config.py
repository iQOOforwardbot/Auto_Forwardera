import datetime
from os import environ  

class Config:
    API_ID = environ.get("API_ID", "11756133")
    API_HASH = environ.get("API_HASH", "6d2d5c9ca4fa62699f50feec4edd7b39")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7712226843:AAEba1gp9zfg34lrO6WIwA3HNkUbUy8Erv0")
    BOT_SESSION = environ.get("BOT_SESSION", "Auto_Forward") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://forwardbot17:rvforward1@cluster0.ubuxz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '7716635383').split()]
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002239391173'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/Magic_Botz") 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")
    PORT = environ.get('PORT', '8080')
    PICS = environ.get('PICS', 'https://mangandi-2-0.onrender.com/oY0q.JPG')
   
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
