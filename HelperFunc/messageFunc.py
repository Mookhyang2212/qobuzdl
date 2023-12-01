import time
from pyrogram.errors.exceptions.bad_request_400 import MessageNotModified
from pyrogram.errors import FloodWait
from pyrogram.types import Message
import logging

from HelperFunc.mediaInfo import get_media_info
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

def sendMessage(toReplyMessage, replyText, replyButtons = None, disablePreview = True):
    try:
        return toReplyMessage.reply_text(replyText,
            disable_web_page_preview=disablePreview,
            quote=True,
            reply_markup = replyButtons)
    except FloodWait as e:
        time.sleep(e.value)
        LOGGER.info(str(e))
        sendMessage(toReplyMessage)
    except Exception as e:
        LOGGER.info(str(e))

def editMessage(toEditMessage, editText, replyButtons = None):
    try:
        return toEditMessage.edit(text=editText,
            disable_web_page_preview=True,
            reply_markup = replyButtons)
    except FloodWait as e:
        time.sleep(e.value)
        LOGGER.info(str(e))
        editMessage(toEditMessage)
    except MessageNotModified as e:
        LOGGER.info(str(e))
    except Exception as e:
        LOGGER.info(str(e))

def copyMessage(toReplyDocument, toCopyChatId = None, sendAsReply = False):
    if toCopyChatId is None: toCopyChatId = toReplyDocument.chat.id
    try:
        if sendAsReply:
            return toReplyDocument.copy(chat_id=toCopyChatId,
                reply_to_message_id=toReplyDocument.message_id)
        else:
            return toReplyDocument.copy(chat_id=toCopyChatId)
    except FloodWait as e:
        time.sleep(e.value)
        LOGGER.info(str(e))
        copyMessage(toReplyDocument)
    except Exception as e:
        LOGGER.info(str(e))

def sendFiles(toReplyFiles:Message, filePath):
    try:
        return toReplyFiles.reply_Files(filePath)
    except FloodWait as e:
        time.sleep(e.value)
        LOGGER.info(str(e))
        sendFiles(toReplyFiles)
    except Exception as e:
        LOGGER.info(str(e))

def sendFiles(toReplyDocument:Message, filePath:str):
    try:
        cap = filePath.replace("/app/qobuzdown/", "", 1)
        cap = cap.replace("usr/src/app", "", 1)
        cap = cap.replace("usr/src", "", 1)
        cap = cap.replace("/", "\n") + "\n@downloaderqobuzcok"
        duration , artist, title = get_media_info(filePath)
        return toReplyDocument.reply_audio(filePath,caption=cap,duration=duration,performer=artist,title=title)
    except FloodWait as e:
        time.sleep(e.value)
        LOGGER.info(str(e))
        sendFiles(toReplyDocument, filePath)
    except Exception as e:
        LOGGER.info(str(e))
