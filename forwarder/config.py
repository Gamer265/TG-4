from forwarder.sample_config import Config


class Development(Config):
    API_KEY = "5231885300:AAGvyhETmGvS0cJHbuXkVsKcMC2eu0bkySw"  # Your bot API key
    OWNER_ID = 862271564  # Your user id

    # Make sure to include the '-' sign in group and channel ids.
    
    FROM_CHATS = [-1001519007225,-1001209629928,-1001217338584,-1001368524326,-1001471322747,-1001519628670,-1001505402139]# List of chat id's to forward messages from.
    TO_CHATS = [-1001606168094]# List of chat id's to forward messages to.

    REMOVE_TAG = False
    WORKERS = 32
   
    
