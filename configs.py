from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1923471"))
    API_HASH = getenv("API_HASH", "fcdc178451cd234e63faefd38895c991")
    BOT_TOKEN = getenv("BOT_TOKEN", "5796564520:AAGU5KcNB1xowytuOOGuSx4TWz8jpibzXdo")
    FSUB = getenv("FSUB", "AsuranMoviefinder1")
    CHID = int(getenv("CHID", "-1001702935595")
    #SUDO = "880087645"
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Erichdaniken:Erichdaniken@cluster0.vhu3d.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
