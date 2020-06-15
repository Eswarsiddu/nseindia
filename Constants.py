from typing import Tuple, Dict

rgbToInt = lambda r, g, b: (r + (g * 256) + (b * 256 * 256))


class Constants:
    URLS: Tuple[str, str] = ('https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY',
                             'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY')

    @staticmethod
    def getTrends(i):
        return str(Constants.REFRESH_TIME * i) + " min"

    @staticmethod
    def initialise(calls_oi, calls_changeinoi, calls_ltp, calls_trend1, calls_trend2, calls_trend3,
                   puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3, up, down, refreshtime):
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
        if refreshtime*60 <= 180:
            print("average refresh time cannot be less than 3 minutes")
            exit(0)
        Constants.REFRESH_TIME = refreshtime

    strikesdiff = [50, 100]
    UP: int = 8
    DOWN: int = 8
    INTIALIZING = False
    WELCOME_TEXT = ""
    CALLS_OI = 'A'
    CALLS_CHANGE_IN_OI = 'B'
    CALLS_LTP = 'F'
    CALLS_TREND1 = 'C'
    CALLS_TREND2 = 'D'
    CALLS_TREND3 = 'E'

    REFRESH_TIME = 3

    EXCEL_STRIKE_PRICE_COLUMN = 'G'

    PUTS_OI = 'H'
    PUTS_CHANGE_IN_OI = 'I'
    PUTS_LTP = 'M'
    PUTS_TREND1 = 'J'
    PUTS_TREND2 = 'K'
    PUTS_TREND3 = 'L'

    NIFTY_NAME = 'NIFTY'
    BANK_NIFTY_NAME = 'BANK NIFTY'

    EXCEL_STRIKES: str = "strikePRICEs"
    NIFTY: int = 0
    BANK_NIFTY: int = 1
    STRIKE_PRICE: str = 'strikePRICE'
    CALLS: str = 'CE'
    PUTS: str = 'PE'
    INDEX: str = "index"
    OI: str = "OI"
    CHANGE_IN_OI: str = "CHANGEINOI"
    LTP: str = "LTP"
    TIME: str = "TIME"
    DATE: str = "DATE"
    PRICE: str = "PRICE"
    TURNOVER_PRICE: str = "turnoverPRICE"
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
    ERROR = 'ERROR'

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
        if i==0:
            return 11
        if i==1:
            return 12
        if i==2:
            return 13
        if i==3:
            return 14
        if i==4:
            return 15
        if i==5:
            return 16

    BOLD = 'bold'
    ITALIC = 'italic'
    BOLD_ITALIC = 'bold italic'
    REGULAR = 'regular'
    HEADING_SIZE = 15

    EXCEL_POSTING_AVG_TIME = 0
    REQUESTING_AVG_TIME = 0
    DIALOGUE_BOX_ROW = 6 + UP + DOWN

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

