from typing import Tuple, Dict
import os, platform

# if platform.system() != 'Windows':
#     print("This program cannot be rune other than windows")
#     exit(0)

#rgbToInt = lambda r, g, b: (r + (g * 256) + (b * 256 * 256))

def rgbToInt(r,g,b):
    return '#%02x%02x%02x' % (r,g,b)

class Constants:
    URLS: Tuple[str, str] = ('https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY',
                             'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY')
    try:
        import xlwings
    except:
        os.system("python -m pip install xlwings")

    try:
        import requests
    except:
        os.system("python -m pip install requests")

    @staticmethod
    def getTrends(i,index):
        return str(Constants.REFRESH_TIME[index] * i) + " min"

    @staticmethod
    def initialise(calls_oi, calls_changeinoi, calls_ltp, calls_trend1, calls_trend2, calls_trend3,
                   puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3, up, down, refreshtime,testing):
        l = [calls_oi, calls_changeinoi, calls_ltp, calls_trend1, calls_trend2, calls_trend3]
        if len(l) != len(list(set(l))):
            print("Calls columns are crashing")
            exit(0)
        for i in l:
            if i in 'ABCDEFF':
                Constants.CALLS_LTP = calls_ltp
                Constants.CALLS_OI = calls_oi
                Constants.CALLS_CHANGE_IN_OI = calls_changeinoi
                Constants.CALLS_TREND1 = calls_trend1
                Constants.CALLS_TREND2 = calls_trend2
                Constants.CALLS_TREND3 = calls_trend3
            else:
                print("calls crossed it bounds")
        l = [puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3]
        if len(l) != len(list(set(l))):
            print("Puts columns are crashing")
            exit(0)

        for i in l:
            if i in 'HIJKLM':
                Constants.PUTS_LTP = puts_ltp
                Constants.PUTS_OI = puts_oi
                Constants.PUTS_CHANGE_IN_OI = puts_changeinoi
                Constants.PUTS_TREND1 = puts_trend1
                Constants.PUTS_TREND2 = puts_trend2
                Constants.PUTS_TREND3 = puts_trend3
            else:
                print("puts crossed it bounds")
                exit(0)

        Constants.UP = up
        Constants.DOWN = down
        if refreshtime*60 <= 180 and not testing:
            print("average refresh time cannot be less than 3 minutes")
            exit(0)
        Constants.REFRESH_TIME = refreshtime


    strikesdiff = [50, 100]
    INTIALIZING = False
    WELCOME_TEXT = ""

    UP = [8,8]
    DOWN = [8,8]

    CALLS_POS = [0,0]
    STRIKEPRICE_POS = [1,1]
    PUTS_POS = [2,2]

    CALLS_OI = [0,0]
    CALLS_CHANGE_IN_OI = [2,2]
    CALLS_LTP = [1,1]
    CALLS_TREND1 = [3,3]
    CALLS_TREND2 = [4,4]
    CALLS_TREND3 = [5,5]

    PUTS_OI = [0,0]
    PUTS_CHANGE_IN_OI = [2,2]
    PUTS_LTP = [1,1]
    PUTS_TREND1 = [3,3]
    PUTS_TREND2 = [4,4]
    PUTS_TREND3 = [5,5]

    REFRESH_TIME = [5,5]

    NIFTY_NAME = 'NIFTY'
    BANK_NIFTY_NAME = 'BANK NIFTY'

    STRIKES_LIST: str = "strikeprices"
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
    CELL_FILL_COLOR = 'fillcolor'
    FONT_STYLE = 'fontstyle'
    FONT_COLOR = 'fontcolor'
    FONT_SIZE = 'fontsize'
    ERROR = 'error'

    #ERRORS
    NO_INTERNET = 'nointernet'
    NO_DATA_FROM_SITE ='nodatainjson'
    CLOSED_EXCEL ='excelclosed'

    RED = rgbToInt(230, 0, 0)
    GREEN = rgbToInt(0, 230, 0)
    YELLOW = rgbToInt(204, 204, 0)
    BLACK = rgbToInt(0, 0, 0)
    GREY = rgbToInt(105, 105, 105)
    BLUE = rgbToInt(0, 0, 255)
    WHITE = rgbToInt(255, 255, 255)
    @staticmethod
    def FONTSIZE(i):
        return 11+i

    BOLD = 'bold'
    ITALIC = 'italic'
    BOLD_ITALIC = 'bold italic'
    REGULAR = 'normal'
    HEADING_SIZE = 15

    EXCEL_POSTING_AVG_TIME = 0
    REQUESTING_AVG_TIME = 0

    VISIBLE_UPDATING = True

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

    TESTING = True
