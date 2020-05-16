import os
from twarc import Twarc
import sys
import json

CONSUMER_KEY = "9At2u3Y2DraTHLSg3D9w6LhE9"
CONSUMER_KEY_SECRET = "DRFCbI2t0gMhfV2KnEub6cljowW9zRwmkeMJ0GT9MlMkrkzspM"
ACCESS_TOKEN = "1259913765614751745-LwtSI48si3sYekzvxW86syIFsRgirl"
ACCESS_TOKEN_SECRET = "e0gpJdT0IXOSxFrhplKMl8FlP0dVnuLg1vwBHzt5Fc9J9"

def readIdFile(input_file_name, output_file_name):
    try:
        t = Twarc(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
        output_file = open(output_file_name, "w")
        inputF = open(input_file_name, "r")
        line = inputF.readline()
        i = 1
        while line != "":
            tweet = t.tweet(line.strip())
            if tweet["lang"] == "en":
                output_file.write(json.dumps(tweet))
                print(i)
                i += 1
            line = inputF.readline()
    except Exception as e:
        print(e)
        return 1


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python dataobtainer.py [input_file_name] [output_file_name]")
        exit()
    input_file_name = sys.argv[1]
    output_file_name = sys.argv[2]
    readIdFile(input_file_name, output_file_name)
    exit()