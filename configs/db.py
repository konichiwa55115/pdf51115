# fileName: configs/db.py
# copyright ©️ 2021 nabilanavab

import os

DATA = {}                                                                    # save user api, fname, capt
                                                                             # if UPDATE_CHANNEL
myID = []                                                                    # saves bot info
  
GROUPS = []                                                                  # save groups id and checks each times
 
invite_link = []                                                             # just saves invitation link

BANNED_USR_DB, BANNED_GRP_DB = [], []                                        # Load Banned Users Id

CUSTOM_THUMBNAIL_U, CUSTOM_THUMBNAIL_C = [], []                              # Load UsersId with custom thumbnail

class dataBASE(object):
    
    MONGODB_URI = "mongodb+srv://Bala7a19871:Ibntaymya1.@cluster0.5mtsc.mongodb.net/?retryWrites=true&w=majority"                      # mongoDB Url (Optional)

                                                                             # Telegram: @nabilanavab
