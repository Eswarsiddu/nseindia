from typing import Tuple, Dict
import os,platform,json


# if platform.system() != 'Windows':
#     print("This program cannot be rune other than windows")
#     exit(0)

# rgbToInt = lambda r, g, b: (r + (g * 256) + (b * 256 * 256))
columnsvaluefilepath=""
if(platform=="Windows"):
    columnsvaluefilepath = os.getcwd()+"\\dependencies\\columnvalues.json"
else:
    columnsvaluefilepath = os.getcwd()+"/dependencies/columnvalues.json"

def rgbToInt(r, g, b):
    return '#%02x%02x%02x' % (r, g, b)


class Constants:
    URLS: Tuple[str, str] = ('https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY',
                             'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY')
    try:
        import requests
    except:
        os.system("python -m pip install requests")

    @staticmethod
    def getTrends(i, index):
        return str(Constants.REFRESH_TIME[index] * i) + " min"

    @staticmethod
    def checkvalues(calls_oi, calls_changeinoi, calls_ltp, calls_trend1, calls_trend2, calls_trend3,
                    puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3, up, down,
                    refreshtime, calls, strikeprice, puts, index,mode):
        t = ([calls, puts, strikeprice],
             [calls_oi, calls_ltp, calls_changeinoi, calls_trend1, calls_trend2, calls_trend3],
             [puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3])

        er = (("Calls, Puts, Strike Price columns overlapped", "Minimum column value is 1", "Maximum column value is 3", 3),
              ("Columns in calls side overlapped", "Minimum column value is 1", "Maximum column value is 6", 6),
              ("Columns in puts side overlapped", "Minimum column value is 1", "Maximum column value is 6", 6))

        for i in range(3):
            l = list(map(int, t[i]))
            if len(set(l)) != len(l): return er[i][0]
            if min(l) < 1: return er[i][1]
            if max(l) > er[i][3]: return er[i][2]

        # TODO: CHECK UP AND DOWN VALUES restrict to 8
        if int(up) > 8:
            return "up value should be less than 10"
        if int(up) <= 0:
            return "up value should be greather then 0"
        if int(down) > 8:
            return "down value should be less than 10"
        if int(down) <= 0:
            return "down value should be greather then 0"

        if int(refreshtime) <= 3:
            return "Time frame must be greater than 3 minutes"

        if mode=="loading":
            Constants.loadvalues(index=index, refreshtime=refreshtime, strikeprice=strikeprice, calls=calls,
                                 calls_oi=calls_oi, calls_ltp=calls_ltp, calls_changeinoi=calls_changeinoi,
                                 calls_trend1=calls_trend1, calls_trend2=calls_trend2, calls_trend3=calls_trend3,
                                 puts=puts, puts_oi=puts_oi, puts_changeinoi=puts_changeinoi, puts_ltp=puts_ltp,
                                 puts_trend1=puts_trend1, puts_trend2=puts_trend2, puts_trend3=puts_trend3, up=up,
                                 down=down)
        else:
            Constants.savevalues(index=index, refreshtime=refreshtime, strikeprice=strikeprice, calls=calls,
                                 calls_oi=calls_oi, calls_ltp=calls_ltp, calls_changeinoi=calls_changeinoi,
                                 calls_trend1=calls_trend1, calls_trend2=calls_trend2, calls_trend3=calls_trend3,
                                 puts=puts, puts_oi=puts_oi, puts_changeinoi=puts_changeinoi, puts_ltp=puts_ltp,
                                 puts_trend1=puts_trend1, puts_trend2=puts_trend2, puts_trend3=puts_trend3, up=up,
                                 down=down)
        return ""

    @staticmethod
    def loadvalues(index,refreshtime,strikeprice,calls,calls_oi,calls_ltp,calls_changeinoi,calls_trend1,calls_trend2,calls_trend3,puts,puts_oi,puts_ltp,puts_changeinoi,puts_trend1,puts_trend2,puts_trend3,up,down):
        Constants.REFRESH_TIME[index] = int(refreshtime)
        Constants.STRIKEPRICE_POS[index] = int(strikeprice)
        Constants.CALLS_POS[index] = int(calls)
        Constants.CALLS_OI[index] = int(calls_oi)
        Constants.CALLS_LTP[index] = int(calls_ltp)
        Constants.CALLS_CHANGE_IN_OI[index] = int(calls_changeinoi)
        Constants.CALLS_TREND1[index] = int(calls_trend1)
        Constants.CALLS_TREND2[index] = int(calls_trend2)
        Constants.CALLS_TREND3[index] = int(calls_trend3)
        Constants.PUTS_POS[index] = int(puts)
        Constants.PUTS_OI[index] = int(puts_oi)
        Constants.PUTS_LTP[index] = int(puts_ltp)
        Constants.PUTS_CHANGE_IN_OI[index] = int(puts_changeinoi)
        Constants.PUTS_TREND1[index] = int(puts_trend1)
        Constants.PUTS_TREND2[index] = int(puts_trend2)
        Constants.PUTS_TREND3[index] = int(puts_trend3)
        Constants.UP_VALUE[index] = int(up)
        Constants.DOWN_VALUE[index] = int(down)

    @staticmethod
    def setvalues(index,data):
        Constants.REFRESH_TIME[index] = data[Constants.REFRESTIME][str(index)]
        Constants.UP_VALUE[index] = data[Constants.UP][str(index)]
        Constants.DOWN_VALUE[index] = data[Constants.DOWN][str(index)]
        Constants.STRIKEPRICE_POS[index]=data[Constants.STRIKE_PRICE][str(index)]
        calls = data[Constants.CALLS]
        Constants.CALLS_POS[index] = calls[Constants.CALLS][str(index)]
        Constants.CALLS_OI[index] = calls[Constants.OI][str(index)]
        Constants.CALLS_LTP[index] = calls[Constants.LTP][str(index)]
        Constants.CALLS_CHANGE_IN_OI[index] = calls[Constants.CHANGE_IN_OI][str(index)]
        Constants.CALLS_TREND1[index] = calls[Constants.TRENDS1][str(index)]
        Constants.CALLS_TREND2[index] = calls[Constants.TRENDS2][str(index)]
        Constants.CALLS_TREND3[index] = calls[Constants.TRENDS3][str(index)]

        puts = data[Constants.PUTS]
        Constants.PUTS_POS[index] = puts[Constants.PUTS][str(index)]
        Constants.PUTS_OI[index] = puts[Constants.OI][str(index)]
        Constants.PUTS_LTP[index] = puts[Constants.LTP][str(index)]
        Constants.PUTS_CHANGE_IN_OI[index] = puts[Constants.CHANGE_IN_OI][str(index)]
        Constants.PUTS_TREND1[index] = puts[Constants.TRENDS1][str(index)]
        Constants.PUTS_TREND2[index] = puts[Constants.TRENDS2][str(index)]
        Constants.PUTS_TREND3[index] = puts[Constants.TRENDS3][str(index)]



    @staticmethod
    def resetvalues(index,mode):
        f = open(columnsvaluefilepath,"r")
        data = json.load(f)
        if mode=="reset":
            Constants.setvalues(index=index, data=data[Constants.DEFAULT])
        else:
            Constants.setvalues(index=index, data=data[Constants.SAVED_VALUES])
        f.close()


    @staticmethod
    def savevalues(index, refreshtime, strikeprice, calls, calls_oi, calls_ltp, calls_changeinoi, calls_trend1, calls_trend2, calls_trend3, puts, puts_oi, puts_ltp, puts_changeinoi, puts_trend1, puts_trend2, puts_trend3, up, down):
        f = open(columnsvaluefilepath,"r+")
        da = json.load(f)
        data = da[Constants.SAVED_VALUES]
        data[Constants.REFRESTIME][str(index)] = int(refreshtime)
        data[Constants.STRIKE_PRICE][str(index)] = int(strikeprice)
        data[Constants.UP][str(index)] = int(up)
        data[Constants.DOWN][str(index)] = int(down)

        data[Constants.CALLS][Constants.CALLS][str(index)] = int(calls)
        data[Constants.CALLS][Constants.OI][str(index)] = int(calls_oi)
        data[Constants.CALLS][Constants.LTP][str(index)] = int(calls_ltp)
        data[Constants.CALLS][Constants.CHANGE_IN_OI][str(index)] = int(calls_changeinoi)
        data[Constants.CALLS][Constants.TRENDS1][str(index)] = int(calls_trend1)
        data[Constants.CALLS][Constants.TRENDS2][str(index)] = int(calls_trend2)
        data[Constants.CALLS][Constants.TRENDS3][str(index)] = int(calls_trend3)

        data[Constants.PUTS][Constants.PUTS][str(index)] = int(puts)
        data[Constants.PUTS][Constants.OI][str(index)] = int(puts_oi)
        data[Constants.PUTS][Constants.LTP][str(index)] = int(puts_ltp)
        data[Constants.PUTS][Constants.CHANGE_IN_OI][str(index)] = int(puts_changeinoi)
        data[Constants.PUTS][Constants.TRENDS1][str(index)] = int(puts_trend1)
        data[Constants.PUTS][Constants.TRENDS2][str(index)] = int(puts_trend2)
        data[Constants.PUTS][Constants.TRENDS3][str(index)] = int(puts_trend3)
        da[Constants.SAVED_VALUES] = data
        f.seek(0)
        json.dump(da,f)
        f.truncate()
        f.close()



    strikesdiff = [50, 100]
    INTIALIZING = False
    WELCOME_TEXT = ""

    UP_VALUE = [8, 8]
    DOWN_VALUE = [8, 8]

    CALLS_POS = [1, 1]
    STRIKEPRICE_POS = [2, 2]
    PUTS_POS = [3, 3]

    CALLS_OI = [1, 1]
    CALLS_CHANGE_IN_OI = [2, 2]
    CALLS_LTP = [6, 6]
    CALLS_TREND1 = [3, 3]
    CALLS_TREND2 = [4, 4]
    CALLS_TREND3 = [5, 5]

    PUTS_OI = [2, 2]
    PUTS_CHANGE_IN_OI = [3, 3]
    PUTS_LTP = [1, 1]
    PUTS_TREND1 = [4, 4]
    PUTS_TREND2 = [5, 5]
    PUTS_TREND3 = [6, 6]

    REFRESH_TIME = [5, 5]

    REFRESTIME = "refreshtime"
    UP = "up"
    DOWN = "down"

    NIFTY_NAME = 'NIFTY'
    BANK_NIFTY_NAME = 'BANK NIFTY'

    STRIKES_LIST: str = "strikeprices"
    DEFAULT: str ="default"
    SAVED_VALUES: str = "savedvalues"
    NIFTY: int = 0
    BANK_NIFTY: int = 1
    STRIKE_PRICE: str = 'STRIKE PRICE'
    CALLS: str = 'CE'
    PUTS: str = 'PE'
    INDEX: str = "index"
    OI: str = "OI"
    CHANGE_IN_OI: str = "CHANGEINOI"
    LTP: str = "LTP"
    TIME: str = "TIME"
    DATE: str = "DATE"
    PRICE: str = "PRICE"
    TURNOVER_PRICE: str = "turnoverprice"
    MARKET_STATUS: str = "marketstatus"
    TRENDS: str = "trends"
    TRENDS1 = 'trends1'
    TRENDS2 = 'trends2'
    TRENDS3 = 'trends3'
    TREND_CHANGE_OF_OI: str = "trendschangeOI"
    TEXT = 'text'
    VALUE = 'value'
    CELL_FILL_COLOR = 'fillcolor'
    FONT_STYLE = 'fontstyle'
    FONT_COLOR = 'fontcolor'
    FONT_SIZE = 'fontsize'
    ERROR = 'error'

    # ERRORS
    NO_INTERNET = 'nointernet'
    NO_DATA_FROM_SITE = 'nodatainjson'
    CLOSED_EXCEL = 'excelclosed'

    BODY = "body"
    HEADING = "heading"

    RED = rgbToInt(230, 0, 0)
    GREEN = rgbToInt(0, 230, 0)
    YELLOW = rgbToInt(204, 204, 0)
    BLACK = rgbToInt(0, 0, 0)
    GREY = rgbToInt(105, 105, 105)
    BLUE = rgbToInt(0, 0, 255)
    WHITE = rgbToInt(255, 255, 255)

    @staticmethod
    def FONTSIZE(i):
        return 11 + i

    BOLD = 'bold'
    ITALIC = 'italic'
    BOLD_ITALIC = 'bold italic'
    REGULAR = 'normal'
    HEADING_SIZE = 15

    EXCEL_POSTING_AVG_TIME = 0
    REQUESTING_AVG_TIME = 0

    HEADERS: Dict[str, str] = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'www.nseindia.com',
        'If-None-Match': 'W/"1047db-ffsRpZgBL7KYhzea10O6o9p87Bk"',
        'TE': 'Trailers',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    }

    TESTING = False
