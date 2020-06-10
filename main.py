from DataFromSite import DataRequest
from time import time,sleep
from Constants import Constants as Const

import os
try:
    from selenium.common.exceptions import WebDriverException
except:
    os.system('python -m pip install selenium')
    from selenium.common.exceptions import WebDriverException


trends = []

if __name__ == "__main__":
    refresh_time = 10
    request = DataRequest()
    for i in range(6):
        if i!=0: sleep(refresh_time)
        Data = request.request_data()
        print("main",Data)