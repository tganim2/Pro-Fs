# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

import os
from os import environ,getenv
import logging
from logging.handlers import RotatingFileHandler

#rohit_1888 on Tg
#--------------------------------------------
#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8012157634:AAH6NL_qG2ylhQtnwhT8jfPCSr3H8s6gcl8")
APP_ID = int(os.environ.get("APP_ID", "16160395")) #Your API ID from my.telegram.org
API_HASH = os.environ.get("API_HASH", "892a16bf3b1569612b18c9d790967cbb") #Your API Hash from my.telegram.org
#--------------------------------------------

CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002521947691")) #Your db channel Id
OWNER = os.environ.get("OWNER", "NeoFrd") # Owner username without @
OWNER_ID = int(os.environ.get("OWNER_ID", "7822720438")) # Owner id
#--------------------------------------------
PORT = os.environ.get("PORT", "8001")
#--------------------------------------------
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://showrovislam535:SAdiKUL6043@cluster0.uktaexw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluooo")
#--------------------------------------------
FSUB_LINK_EXPIRY = int(os.getenv("FSUB_LINK_EXPIRY", "0"))  # 0 means no expiry
BAN_SUPPORT = os.environ.get("BAN_SUPPORT", "RM_Supports")
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "200"))
#--------------------------------------------
START_PIC = os.environ.get("START_PIC", "https://imgur.com/a/NYndShA")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://i.imgur.com/UiRj3CN.jpeg")

#--------------------------------------------
SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "")
TUT_VID = os.environ.get("TUT_VID","https://t.me/hwdownload/3")
SHORT_MSG = "<b>⌯ Here is Your Download Link, Must Watch Tutorial Before Clicking On Download...</b>"

SHORTENER_PIC = os.environ.get("SHORTENER_PIC", "https://telegra.ph/file/ec17880d61180d3312d6a.jpg")
#--------------------------------------------

#--------------------------------------------
HELP_TXT = "<b><blockquote> ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href=https://t.me/RahatMx>Rahat</a></blockquote></b>"
ABOUT_TXT = "<b><blockquote>◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/RahatMx>Rahat</a>"
#--------------------------------------------
#--------------------------------------------
START_MSG = os.environ.get(
    "START_MESSAGE",
    """𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙍𝙖𝙧𝙚 𝘼𝙣𝙞𝙢𝙚 𝙃𝙪𝙗 𝙊𝙛𝙛𝙞𝙘𝙞𝙖𝙡 𝘽𝙊𝙏! 🎉

𝙃𝙚𝙡𝙡𝙤 {mention}!
𝙒𝙚𝙡𝙘𝙤𝙢𝙚 𝙩𝙤 𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡! 𝙔𝙤𝙪’𝙡𝙡 𝙛𝙞𝙣𝙙 𝙮𝙤𝙪𝙧 𝙛𝙖𝙫𝙤𝙧𝙞𝙩𝙚 𝙖𝙣𝙞𝙢𝙚 𝙝𝙚𝙧𝙚. 𝙃𝙤𝙥𝙚 𝙮𝙤𝙪 𝙝𝙖𝙫𝙚 𝙖 𝙜𝙧𝙚𝙖𝙩 𝙩𝙞𝙢𝙚! 😊

*𝘿𝙤𝙣'𝙩 𝙛𝙤𝙧𝙜𝙚𝙩 𝙩𝙤 𝙟𝙤𝙞𝙣 𝙤𝙪𝙧 𝙘𝙝𝙖𝙣𝙣𝙚𝙡*
"""
)
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", """𝗛𝗲𝘆 {mention}

𝗣𝗹𝗲𝗮𝘀𝗲 𝗝𝗼𝗶𝗻 𝗔𝗹𝗹 𝗠𝘆 𝗨𝗽𝗱𝗮𝘁𝗲 𝗖𝗵𝗮𝗻𝗻𝗲𝗹𝘀 𝗧𝗼 𝗨𝘀𝗲 𝗠𝗲!
━━━━━━━━━━━━━━━━━━━━━━
➥ᴊᴏ ʟᴏɢ ᴅᴏᴡɴʟᴏᴀᴅ ᴋᴀʀᴀɴᴀ ʜᴀʜɪɴ ᴊᴀᴀɴᴀᴛᴇ, ᴏ ʟᴏɢ ʏᴀʜ ᴠɪᴅᴇᴏ ᴅᴇᴋʜᴇɴ ⟱⟱
https://t.me/Anime_Downlod_Tutorial/4""")

CMD_TXT = """<blockquote><b>» ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:</b></blockquote>

<b>›› /dlt_time :</b> sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /check_dlt_time :</b> ᴄʜᴇᴄᴋ ᴄᴜʀʀᴇɴᴛ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇ
<b>›› /dbroadcast :</b> ʙʀᴏᴀᴅᴄᴀsᴛ ᴅᴏᴄᴜᴍᴇɴᴛ / ᴠɪᴅᴇᴏ
<b>›› /ban :</b> ʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /unban :</b> ᴜɴʙᴀɴ ᴀ ᴜꜱᴇʀ
<b>›› /banlist :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ʙᴀɴɴᴇᴅ ᴜꜱᴇʀs
<b>›› /addchnl :</b> ᴀᴅᴅ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /delchnl :</b> ʀᴇᴍᴏᴠᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ
<b>›› /listchnl :</b> ᴠɪᴇᴡ ᴀᴅᴅᴇᴅ ᴄʜᴀɴɴᴇʟs
<b>›› /fsub_mode :</b> ᴛᴏɢɢʟᴇ ꜰᴏʀᴄᴇ sᴜʙ ᴍᴏᴅᴇ
<b>›› /pbroadcast :</b> sᴇɴᴅ ᴘʜᴏᴛᴏ ᴛᴏ ᴀʟʟ ᴜꜱᴇʀs
<b>›› /add_admin :</b> ᴀᴅᴅ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /deladmin :</b> ʀᴇᴍᴏᴠᴇ ᴀɴ ᴀᴅᴍɪɴ
<b>›› /admins :</b> ɢᴇᴛ ʟɪsᴛ ᴏꜰ ᴀᴅᴍɪɴs
<b>›› /addpremium :</b> ᴀᴅᴅ ᴀ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀ
<b>›› /premium_users :</b> ʟɪsᴛ ᴀʟʟ ᴘʀᴇᴍɪᴜᴍ ᴜꜱᴇʀs
<b>›› /remove_premium :</b> ʀᴇᴍᴏᴠᴇ ᴘʀᴇᴍɪᴜᴍ ꜰʀᴏᴍ ᴀ ᴜꜱᴇʀ
<b>›› /myplan :</b> ᴄʜᴇᴄᴋ ʏᴏᴜʀ ᴘʀᴇᴍɪᴜᴍ sᴛᴀᴛᴜs
<b>›› /count :</b> ᴄᴏᴜɴᴛ verifications
"""
#--------------------------------------------
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>• </b>") #set your Custom Caption here, Keep None for Disable Custom Caption
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False #set True if you want to prevent users from forwarding files from bot
#--------------------------------------------
#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'
#--------------------------------------------
BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

#==========================(BUY PREMIUM)====================#

OWNER_TAG = os.environ.get("OWNER_TAG", "RahatMx")
UPI_ID = os.environ.get("UPI_ID", "")
QR_PIC = os.environ.get("QR_PIC", "")
SCREENSHOT_URL = os.environ.get("SCREENSHOT_URL", f"t.me/RahatMx")
#--------------------------------------------
#Time and its price
#7 Days
PRICE1 = os.environ.get("PRICE1", "0 rs")
#1 Month
PRICE2 = os.environ.get("PRICE2", "60 rs")
#3 Month
PRICE3 = os.environ.get("PRICE3", "150 rs")
#6 Month
PRICE4 = os.environ.get("PRICE4", "280 rs")
#1 Year
PRICE5 = os.environ.get("PRICE5", "550 rs")

#===================(END)========================#

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
