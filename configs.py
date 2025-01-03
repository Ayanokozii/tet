# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21189715"))
    API_HASH = getenv("API_HASH", "988a9111105fd2f0c5e21c2c2449edfd")
    BOT_TOKEN = getenv("BOT_TOKEN", "7242102837:AAGAv-USsh3v570_2RahxYsAIDcw1FPwUgg")
    # Your Force Subscribe Channel Id Below 
    CHID = int(getenv("CHID", "-1002231147120")) # Make Bot Admin In This Channel
    # Admin Or Owner Id Below
    SUDO = list(map(int, getenv("SUDO", "7181106700").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/mydatabase")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
