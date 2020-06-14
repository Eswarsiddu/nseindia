from DataRequest import DataRequest
from ExcelData import ExcelDataFormatter as ExcelFormatter
from Constants import Constants as Const
from PostInExcel import Excel
from time import sleep
import os

Excelfilepath = os.getcwd() + "\\nsetest.xlsx"

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
timeframe = 0.1

Const.Testing_index = -1

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
    print("started")
    prevtime = ['', '']
    preprice = [0, 0]
    sleep(2)
    print("len = ",len(Const.testdata))
    # TODO:CHANGE to infinite loop
    for i in range(3):
        if i != 0:
            sleep(refresh_time)
        Data = request.request_data
        print("data retrived from internet")
        Data = exceldata.update_data(Data)
        print("Data analysed in excel form")
        isupdated = excel.postinexcel(data=Data, prevprice=preprice, prevtime=prevtime)
        print("updated data")
        if isupdated:
            prevtime[Const.NIFTY] = Data[Const.NIFTY][Const.TIME]
            preprice[Const.NIFTY] = Data[Const.NIFTY][Const.PRICE]
            prevtime[Const.BANK_NIFTY] = Data[Const.BANK_NIFTY][Const.TIME]
            preprice[Const.BANK_NIFTY] = Data[Const.BANK_NIFTY][Const.PRICE]
        else:
            request.reset_data()

        print("waiting for next")
