import os
from twarc import Twarc
import sys
import json
import csv
import datetime

CONSUMER_KEY = "9At2u3Y2DraTHLSg3D9w6LhE9"
CONSUMER_KEY_SECRET = "DRFCbI2t0gMhfV2KnEub6cljowW9zRwmkeMJ0GT9MlMkrkzspM"
ACCESS_TOKEN = "1259913765614751745-LwtSI48si3sYekzvxW86syIFsRgirl"
ACCESS_TOKEN_SECRET = "e0gpJdT0IXOSxFrhplKMl8FlP0dVnuLg1vwBHzt5Fc9J9"
# every request read READ_RATE num of tweets 
READ_RATE = 50000
#example: tweet_sample.json
#More info: https://developer.twitter.com/en/docs/tweets/data-dictionary/overview/tweet-object


def readIdFile(input_file_name, tweets_num = 0):
    t = Twarc(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    inputF = open(input_file_name, "r")
    i = 1
    subIdFileName = "tweets_id_" + str(i // 50000 + 1) + ".txt"
    subIdFile = open(subIdFileName, "a+")
    print("start read")
    line = inputF.readline()
    while line != "" and (tweets_num > 0 and i < tweets_num + 1) or tweets_num <= 0:
        subIdFile.write(line)
        line = inputF.readline()
        if i % 50000 == 0 or tweets_num == i or line == "":
            print("Read: " + subIdFileName)
            subIdFile.close()
            # send request
            tweets = t.hydrate(open(subIdFileName))
            tweetsClean(tweets)
            print("Finish read:" + subIdFileName)
            subIdFileName = "./tweets_id_" + str(i // 50000 + 1) + ".txt"
            subIdFile = open("./tweets_id_" + str(i // 50000 + 1) + ".txt", "w")
        i += 1   

def filter(tweet):
    # change when needed
    return tweet["lang"] == "en" and not tweet["is_quote_status"] and tweet["in_reply_to_status_id_str"] is None

#Temporary
KEYWORD = {"China": ["china", "chinese", "cn"], "Trump": ["trump"], "StayHome": ["WFH", "work from home", "stay at home", "stay home"]}
def tweetsClean(tweets):
    #output csv
    print("extract data")
    index = 1
    fileDict = {i: csv.writer(open(i+".csv", "w", encoding="utf-8")) for i in KEYWORD}
    for tweet in tweets:
        if filter(tweet):
            t = datetime.datetime.strptime(tweet["created_at"], "%a %b %d %X %z %Y")
            data = [tweet["id"], t.strftime("%Y-%m-%d"), tweet["full_text"], tweet["retweet_count"], tweet["user"]["name"]]
            text = tweet["full_text"]
            writeData(data, text, fileDict)
        index += 1
        if index % 1000 == 0:
            print(index)


def writeData(data, text, fileDict):
    text = text.lower()
    for i in KEYWORD:
        if any([j in text for j in KEYWORD[i]]):
            fileDict[i].writerow(data)
    return 
            
        




if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python dataobtainer.py [input_file_name] [tweets_num(OPTIONAL)]")
        exit()
    input_file_name = sys.argv[1]
    if len(sys.argv) == 3:
        tweets_num = int(sys.argv[2])
        readIdFile(input_file_name, tweets_num = tweets_num)
    else:
        readIdFile(input_file_name)
    exit()