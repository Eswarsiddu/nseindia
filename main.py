from DataRequest import DataRequest
from ExcelData import ExcelDataFormatter as ExcelFormatter
from time import time, sleep

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
    exceldata = ExcelFormatter(up=13,down=13)
    # TODO:change to while
    for i in range(1):
        # TODO: change refresh time from seconds to minutes
        if i != 0:
            sleep(refresh_time)
        Data = request.request_data()
        exceldata.update_data(data=Data)

