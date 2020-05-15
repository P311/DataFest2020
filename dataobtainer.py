import os
from twarc import Twarc
import sys

CONSUMER_KEY = "9At2u3Y2DraTHLSg3D9w6LhE9"
CONSUMER_KEY_SECRET = "DRFCbI2t0gMhfV2KnEub6cljowW9zRwmkeMJ0GT9MlMkrkzspM"
ACCESS_TOKEN = "DRFCbI2t0gMhfV2KnEub6cljowW9zRwmkeMJ0GT9MlMkrkzspM"
ACCESS_TOKEN_SECRET = "1259913765614751745-LwtSI48si3sYekzvxW86syIFsRgirl"

if __name__ == "__main__":
    # t = Twarc(CONSUMER_KEY, CONSUMER_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # sysargv = ["dataobtainer.py", input_file_name]  
    file_name = sys.argv[1]
    os.system("twarc hydrate " + file_name + " > result.jsonl")