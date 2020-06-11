from DataRequest import DataRequest
from ExcelData import ExcelDataFormatter as ExcelFormatter
from Constants import Constants as Const
from time import time, sleep

import os

try:
    from selenium.common.exceptions import WebDriverException
except:
    os.system('python -m pip install selenium')
    from selenium.common.exceptions import WebDriverException

trends = []

if __name__ == "__main__":
    refresh_time = 3*60
    request = DataRequest()
    exceldata = ExcelFormatter(up=13,down=13)
    # TODO:change to while
    for i in range(3):
        # TODO: change refresh time from seconds to minutes
        if i != 0:
            sleep(refresh_time)
        Data = request.request_data()
        print(Data)
        #Postingdata=exceldata.update_data(data=Data)
        # for index in range(2):
        #     for strikeprice in Postingdata[index]:
        #         print('Strike price',strikeprice)
        #         for option in Postingdata[index][strikeprice]:
        #             print('option',option)
        #             for attribute in Postingdata[index][strikeprice][option]:
        #                 print(attribute,Postingdata[index][strikeprice][option][attribute])
        print("waiting for next")
