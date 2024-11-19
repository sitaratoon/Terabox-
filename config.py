import os

#Database 
#Database [https://youtu.be/qFB0cFqiyOM?si=fVicsCcRSmpuja1A]
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://Renamest:Renamest@cluster0.prfhc.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#Shortner (token system) 
# check my discription to help by using my refer link of shareus.io


SHORTLINK_URL = os.environ.get("SHORTLINK_URL", "instantlinks.co")
SHORTLINK_API = os.environ.get("SHORTLINK_API", "bb19246271be2273550dd1c3817ebda087e6c01b")
VERIFY_EXPIRE = int(os.environ.get('VERIFY_EXPIRE', 43200)) # Add time in seconds
IS_VERIFY = os.environ.get("IS_VERIFY", "True")
TUT_VID = os.environ.get("TUT_VID", "https://t.me/ultroid_official/18") # shareus ka tut_vid he 
