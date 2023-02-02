import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):

    BOT_TOKEN = os.environ.get("BOT_TOKEN", "1823808722:AAFlWM_qHhQbClnWzWHPD3mSCQlCDVVOFd8")

    API_ID = int(os.environ.get("API_ID", "663122"))

    API_HASH = os.environ.get("API_HASH", "23dac54b523173b5f83014ae566584bd")

    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "662933911").split())

    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())

    DOWNLOAD_LOCATION = "./DOWNLOADS"

    UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "NewBotz")

    MAX_FILE_SIZE = 4194304000

    TG_MAX_FILE_SIZE = 4194304000

    FREE_USER_MAX_FILE_SIZE = 4194304000

    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))

    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")

    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")

    OUO_IO_API_KEY = ""

    MAX_MESSAGE_LENGTH = 4096

    PROCESS_MAX_TIMEOUT = 0

    DEF_WATER_MARK_FILE = "Use this bot @UploadLinkToFileBot"

    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://aswanthvk:aswanthvk@cluster0.ul7sp2m.mongodb.net/?retryWrites=true&w=majority")

    SESSION_NAME = os.environ.get("SESSION_NAME", "SuperDLBot")

    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001438032160"))

    LOGGER = logging

    OWNER_ID = int(os.environ.get("OWNER_ID", "662933911"))

    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "NewBotz")
    
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "SuperDLBot")
