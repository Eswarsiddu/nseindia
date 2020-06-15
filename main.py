from DataRequest import DataRequest
from ExcelData import ExcelDataFormatter as ExcelFormatter
from Constants import Constants as Const
from PostInExcel import Excel
from time import sleep
import os

try:
    import xlwings
except:
    os.system("python -m pip install xlwings")

try:
    import requests
except:
    os.system("python -m pip install requests")


Excelfilepath = os.getcwd() + "\\optionchaindata.xlsx"

# Welcome text
Const.WELCOME_TEXT = "PLEASE WAIT FOR FEW SECONDS, RELOADING AWM 😁😁"

# How many values you need to see up/down from current price
up = 8
down = 8

# The structure of the columns
# calls, should be between A-F
calls_oi = 'A'
calls_changeinoi = 'C'
calls_trend1 = 'D'
calls_trend2 = 'E'
calls_trend3 = 'F'
calls_ltp = 'B'
# puts should be between H-M
puts_oi = 'H'
puts_changeinoi = 'I'
puts_trend1 = 'J'
puts_trend2 = 'K'
puts_trend3 = 'L'
puts_ltp = 'M'

# TimeFrame
timeframe = 5

Const.VISIBLE_UPDATING = False

if __name__ == "__main__":
    Const.initialise(calls_changeinoi=calls_changeinoi,
                     calls_ltp=calls_ltp,
                     calls_oi=calls_oi,
                     calls_trend1=calls_trend1,
                     calls_trend2=calls_trend2,
                     calls_trend3=calls_trend3,
                     puts_oi=puts_oi,
                     puts_ltp=puts_ltp,
                     puts_trend1=puts_trend1,
                     puts_trend2=puts_trend2,
                     puts_changeinoi=puts_changeinoi,
                     puts_trend3=puts_trend3,
                     up=up,
                     down=down,
                     refreshtime=timeframe)

    refresh_time = Const.REFRESH_TIME * 60
    request = DataRequest()
    exceldata = ExcelFormatter(up=Const.UP, down=Const.DOWN)
    excel = Excel(filepath=Excelfilepath)
    starting = True
    sleep(2)
    while True:
        if starting == False:
            sleep(refresh_time)
        starting = False
        Data = request.request_data
        Data = exceldata.update_data(Data)
        try:
            excel.postinexcel(data=Data)
        except:
            excel.setupexcel()
            excel.postinexcel(data=Data)
        if Data[Const.NIFTY][Const.ERROR] != None:
            request.reset_data()

        elif Data[Const.NIFTY][Const.MARKET_STATUS] == False:
            exit(0)
