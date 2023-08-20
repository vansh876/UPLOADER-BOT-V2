import os

class Config(object):
    
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6317033018:AAELYma_0EKAOwC7YfUhca-scjFre7yFSiQ")
    
    API_ID = int(os.environ.get("API_ID", "25194985")
    
    API_HASH = os.environ.get("API_HASH", "dc6efd66926906b2a354b6020ba5dfad")
    
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    
    MAX_FILE_SIZE = 50000000

    TG_MAX_FILE_SIZE = 2097152000

    FREE_USER_MAX_FILE_SIZE = 50000000
    
    CHUNK_SIZE = int(128)

    HTTP_PROXY = ""
    
    MAX_MESSAGE_LENGTH = 4096
    
    PROCESS_MAX_TIMEOUT = 3600
    
    OWNER_ID = int(os.environ.get("OWNER_ID", "2122960237")

    SESSION_NAME = "UploadLinkToFileBot"
    
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Vansh:Vansh@cluster0.qeuxme9.mongodb.net/?retryWrites=true&w=majority")

    MAX_RESULTS = "100"
