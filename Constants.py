from typing import Tuple, Dict, List

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
        if len(l) == len(list(set(l))):
            print("no calls reduncy")
        for i in l:
            if i in 'ABCDEFF':
                Constants.CALLS_LTP = calls_ltp
                Constants.CALLS_OI = calls_oi
                Constants.CALLS_CHANGE_IN_OI = calls_changeinoi
                Constants.CALLS_TREND1 = calls_trend1
                Constants.CALLS_TREND2 = calls_trend2
                Constants.CALLS_TREND3 = calls_trend3
            else:
                print("crossed bounds")
        l = [puts_oi, puts_changeinoi, puts_ltp, puts_trend1, puts_trend2, puts_trend3]
        if len(l) == len(list(set(l))):
            print("no puts reduncancy")

        for i in l:
            if i in 'HIJKLM':
                Constants.PUTS_LTP = puts_ltp
                Constants.PUTS_OI = puts_oi
                Constants.PUTS_CHANGE_IN_OI = puts_changeinoi
                Constants.PUTS_TREND1 = puts_trend1
                Constants.PUTS_TREND2 = puts_trend2
                Constants.PUTS_TREND3 = puts_trend3
            else:
                print("crossed bounds")

        Constants.UP = up
        Constants.DOWN = down
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

    BOLD = 'bold'
    ITALIC = 'italic'
    BOLD_ITALIC = 'bold italic'
    REGULAR = 'regular'
    HEADING_SIZE = 15

    EXCEL_POSTING_AVG_TIME = 0
    REQUESTING_AVG_TIME = 0
    DIALOGUE_BOX_ROW = 6 + UP + DOWN

    VISIBLE_UPDATING = True

    DUMMYDATA = [{'TIME': '12:58:56',
                  "DATE": '12-Jun-2020',
                  'PRICE': 9766.25,
                  'marketstatus': True,
                  'strikePRICEs': [1, 2, 3, 4, 5, 6, 7, 8, 9, 9, 10, 11, 12, 13, 14, 15, 16], 9350: {
            'CE': {'OI': {'text': '5', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '5', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '420.3', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '1681', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1401', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '54.7', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 9350, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9400: {'CE': {
                      'OI': {'text': '475', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                      'CHANGEINOI': {'text': '321', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': 52428},
                      'LTP': {'text': '403.05', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': 52428},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428}}, 'PE': {
                      'OI': {'text': '19230', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': None},
                      'CHANGEINOI': {'text': '12041', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': None},
                      'LTP': {'text': '63.25', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': None},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None}},
                         'strikePRICE': {'text': 9400, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                         'fillcolor': 15073280}}, 9450: {
            'CE': {'OI': {'text': '38', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '37', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '356.1', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '1728', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1137', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '72.45', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 9450, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9500: {'CE': {'OI': {'text': '3095', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                       'fillcolor': 52428},
                                'CHANGEINOI': {'text': '1764', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                'LTP': {'text': '327.7', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': 52428},
                                'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428}}, 'PE': {
                      'OI': {'text': '27223', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': None},
                      'CHANGEINOI': {'text': '10920', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': None},
                      'LTP': {'text': '83.95', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': None},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None}},
                         'strikePRICE': {'text': 9500, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                         'fillcolor': 15073280}}, 9550: {
            'CE': {'OI': {'text': '158', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '155', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '290.8', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '2061', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1622', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '96.3', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 9550, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9600: {'CE': {'OI': {'text': '4954', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                       'fillcolor': 52428},
                                'CHANGEINOI': {'text': '4638', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                'LTP': {'text': '254', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': 52428},
                                'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428}}, 'PE': {
                      'OI': {'text': '19943', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': None},
                      'CHANGEINOI': {'text': '10739', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': None},
                      'LTP': {'text': '111.3', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': None},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None}},
                         'strikePRICE': {'text': 9600, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                         'fillcolor': 15073280}}, 9650: {
            'CE': {'OI': {'text': '1031', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '1026', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '220.45', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '2716', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1985', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '128', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 9650, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9700: {'CE': {'OI': {'text': '12192', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                       'fillcolor': 52428},
                                'CHANGEINOI': {'text': '11421', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                'LTP': {'text': '189', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': 52428},
                                'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428},
                                'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': 52428}}, 'PE': {
                      'OI': {'text': '19048', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': None},
                      'CHANGEINOI': {'text': '9555', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': None},
                      'LTP': {'text': '146.55', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': None},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None}},
                         'strikePRICE': {'text': 9700, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                         'fillcolor': None}}, 9750: {
            'CE': {'OI': {'text': '2112', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '2108', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '161', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '2127', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '847', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '167', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 9750, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9800: {'CE': {'OI': {'text': '17692', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                       'fillcolor': None},
                                'CHANGEINOI': {'text': '14332', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                'LTP': {'text': '135.6', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': None},
                                'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None},
                                'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None},
                                'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None}}, 'PE': {
                      'OI': {'text': '9227', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': 52428},
                      'CHANGEINOI': {'text': '0580', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': 52428},
                      'LTP': {'text': '191.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': 52428},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428}},
                         'strikePRICE': {'text': 9800, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                         'fillcolor': 15073280}}, 9850: {
            'CE': {'OI': {'text': '1329', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1225', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '112.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '935', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '29', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '220.55', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 9850, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  9900: {'CE': {'OI': {'text': '22471', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                       'fillcolor': None},
                                'CHANGEINOI': {'text': '14108', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                'LTP': {'text': '91.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': None},
                                'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None},
                                'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None},
                                'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                            'fillcolor': None}}, 'PE': {
                      'OI': {'text': '6347', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': 52428},
                      'CHANGEINOI': {'text': '-3808', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': 52428},
                      'LTP': {'text': '247.15', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': 52428},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428}},
                         'strikePRICE': {'text': 9900, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                         'fillcolor': 15073280}}, 9950: {
            'CE': {'OI': {'text': '2331', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1476', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '74.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '479', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '-268', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '279.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 9950, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  10000: {'CE': {'OI': {'text': '27372', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': None},
                                 'CHANGEINOI': {'text': '14047', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                'fillcolor': None},
                                 'LTP': {'text': '59.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                         'fillcolor': None},
                                 'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None},
                                 'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None},
                                 'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None}}, 'PE': {
                      'OI': {'text': '7289', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': 52428},
                      'CHANGEINOI': {'text': '-652', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': 52428},
                      'LTP': {'text': '316', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': 52428},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428}},
                          'strikePRICE': {'text': 10000, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0,
                                          'fillcolor': 15073280}}, 10050: {
            'CE': {'OI': {'text': '3253', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1442', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '46.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '664', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '-59', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '351.2', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 10050, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  10100: {'CE': {'OI': {'text': '16883', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                        'fillcolor': None},
                                 'CHANGEINOI': {'text': '2777', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                'fillcolor': None},
                                 'LTP': {'text': '36.45', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                         'fillcolor': None},
                                 'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None},
                                 'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None},
                                 'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                             'fillcolor': None}}, 'PE': {
                      'OI': {'text': '4031', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                             'fillcolor': 52428},
                      'CHANGEINOI': {'text': '-379', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                     'fillcolor': 52428},
                      'LTP': {'text': '391.55', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                              'fillcolor': 52428},
                      'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                      'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428}},
                          'strikePRICE': {'text': 10100, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                          'fillcolor': None}}, 10150: {
            'CE': {'OI': {'text': '4716', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '2969', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '28.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '181', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '-38', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '427.1', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 10150, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                  'ERROR': None}, {'TIME': '12:58:56', 'DATE': '12-Jun-2020', 'PRICE': 20058.5, 'marketstatus': True,
                                   'strikePRICEs': [19200, 19300, 19400, 19500, 19600, 19700, 19800, 19900, 20000,
                                                    20100, 20200, 20300, 20400, 20500, 20600, 20700, 20800], 19200: {
            'CE': {'OI': {'text': '34', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '34', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '1140.8', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '4686', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '4520', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '313.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 19200, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0, 'fillcolor': 15073280}},
                                   19300: {'CE': {
                                       'OI': {'text': '38', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '38', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '1070', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}}, 'PE': {
                                       'OI': {'text': '3599', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '3231', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '341.65', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}},
                                           'strikePRICE': {'text': 19300, 'fontsize': 11, 'fontstyle': 'regular',
                                                           'fontcolor': 0, 'fillcolor': None}}, 19400: {
            'CE': {'OI': {'text': '56', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '56', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '1025.2', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '1976', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1468', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '373.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 19400, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   19500: {'CE': {
                                       'OI': {'text': '3457', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '3245', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '937', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}}, 'PE': {
                                       'OI': {'text': '16628', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '2830', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '403.85', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}},
                                           'strikePRICE': {'text': 19500, 'fontsize': 14, 'fontstyle': 'bold',
                                                           'fontcolor': 0, 'fillcolor': 15073280}}, 19600: {
            'CE': {'OI': {'text': '464', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '463', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '864.2', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '2291', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '2103', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '442.95', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 19600, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   19700: {'CE': {
                                       'OI': {'text': '1320', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '1320', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '819', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}}, 'PE': {
                                       'OI': {'text': '4197', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '3603', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '477.95', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}},
                                           'strikePRICE': {'text': 19700, 'fontsize': 14, 'fontstyle': 'bold',
                                                           'fontcolor': 0, 'fillcolor': 15073280}}, 19800: {
            'CE': {'OI': {'text': '2251', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '2250', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '744.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '4091', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '3618', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '519.25', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 19800, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0, 'fillcolor': 15073280}},
                                   19900: {'CE': {
                                       'OI': {'text': '1732', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '1730', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '690.4', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}}, 'PE': {
                                       'OI': {'text': '3513', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '3188', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '563.1', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}},
                                           'strikePRICE': {'text': 19900, 'fontsize': 11, 'fontstyle': 'regular',
                                                           'fontcolor': 0, 'fillcolor': None}}, 20000: {
            'CE': {'OI': {'text': '10783', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '9218', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '636.8', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'PE': {'OI': {'text': '11773', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1652', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '605', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'strikePRICE': {'text': 20000, 'fontsize': 14, 'fontstyle': 'bold', 'fontcolor': 0, 'fillcolor': 15073280}},
                                   20100: {'CE': {
                                       'OI': {'text': '1596', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '1596', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '587.05', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}}, 'PE': {
                                       'OI': {'text': '1058', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '637', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '654.65', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}},
                                           'strikePRICE': {'text': 20100, 'fontsize': 11, 'fontstyle': 'regular',
                                                           'fontcolor': 0, 'fillcolor': None}}, 20200: {
            'CE': {'OI': {'text': '2575', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '2543', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '537.8', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '904', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '-8', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '710.45', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 20200, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   20300: {'CE': {
                                       'OI': {'text': '1659', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '1584', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '492.2', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}}, 'PE': {
                                       'OI': {'text': '595', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '-379', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '760', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}},
                                           'strikePRICE': {'text': 20300, 'fontsize': 11, 'fontstyle': 'regular',
                                                           'fontcolor': 0, 'fillcolor': None}}, 20400: {
            'CE': {'OI': {'text': '2170', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '2044', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '447.9', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '727', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '02', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '805.85', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 20400, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   20500: {'CE': {
                                       'OI': {'text': '10743', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '6640', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '408.35', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}}, 'PE': {
                                       'OI': {'text': '4316', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '0548', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '883', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}},
                                           'strikePRICE': {'text': 20500, 'fontsize': 14, 'fontstyle': 'bold',
                                                           'fontcolor': 0, 'fillcolor': 15073280}}, 20600: {
            'CE': {'OI': {'text': '2225', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '1281', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '371.05', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '351', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '062', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '930', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 20600, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   20700: {'CE': {
                                       'OI': {'text': '2187', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': None},
                                       'CHANGEINOI': {'text': '1334', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': None},
                                       'LTP': {'text': '334.3', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': None},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': None}}, 'PE': {
                                       'OI': {'text': '370', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                              'fillcolor': 52428},
                                       'CHANGEINOI': {'text': '-40', 'fontsize': 11, 'fontstyle': 'regular',
                                                      'fontcolor': 0, 'fillcolor': 52428},
                                       'LTP': {'text': '985.5', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                               'fillcolor': 52428},
                                       'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428},
                                       'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                                   'fillcolor': 52428}},
                                           'strikePRICE': {'text': 20700, 'fontsize': 11, 'fontstyle': 'regular',
                                                           'fontcolor': 0, 'fillcolor': None}}, 20800: {
            'CE': {'OI': {'text': '3606', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'CHANGEINOI': {'text': '2308', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': None},
                   'LTP': {'text': '302', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
            'PE': {'OI': {'text': '371', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'CHANGEINOI': {'text': '009', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                                  'fillcolor': 52428},
                   'LTP': {'text': '1075.15', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                           'fillcolor': 52428},
                   'trends1': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends2': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': 52428},
                   'trends3': {'text': '0', 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0,
                               'fillcolor': 52428}},
            'strikePRICE': {'text': 20800, 'fontsize': 11, 'fontstyle': 'regular', 'fontcolor': 0, 'fillcolor': None}},
                                   'ERROR': None}]

    # testing
    EROOR_MSG = None
    TESTING: bool = True
    Testing_index: int = 0
    testdata = [[{'index': 'NIFTY', 'marketstatus': True, 'TIME': '12:58:56', 'DATE': '12-Jun-2020', 'PRICE': 9766.25,
                  'turnoverPRICE': 9750, 7300: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 78, 'CHANGEINOI': 52, 'LTP': 0.8, 'trendschangeOI': [52], 'trends': [0, 0, 0, 0, 0]}},
                  7350: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1.7, 'trendschangeOI': [1],
                             'trends': [0, 0, 0, 0, 0]}}, 7400: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1.15, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  7450: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0.75, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 7500: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 835, 'CHANGEINOI': 830, 'LTP': 1.15, 'trendschangeOI': [830], 'trends': [0, 0, 0, 0, 0]}},
                  7550: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 7600: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 7650: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 7700: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 7750: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 7800: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2.9, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  7850: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 7900: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 8, 'CHANGEINOI': 8, 'LTP': 1.95, 'trendschangeOI': [8], 'trends': [0, 0, 0, 0, 0]}},
                  7950: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 8000: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 3674, 'CHANGEINOI': 1781, 'LTP': 1.9, 'trendschangeOI': [1781],
                   'trends': [0, 0, 0, 0, 0]}}, 8050: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8100: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8150: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8200: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8250: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8300: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 306, 'CHANGEINOI': 306, 'LTP': 3, 'trendschangeOI': [306], 'trends': [0, 0, 0, 0, 0]}},
                  8350: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 8400: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 736, 'CHANGEINOI': 734, 'LTP': 3.95, 'trendschangeOI': [734], 'trends': [0, 0, 0, 0, 0]}},
                  8450: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 8500: {
            'CE': {'OI': 6, 'CHANGEINOI': 0, 'LTP': 1210, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 7681, 'CHANGEINOI': 3755, 'LTP': 4.95, 'trendschangeOI': [3755],
                   'trends': [0, 0, 0, 0, 0]}}, 8550: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8600: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 3186, 'CHANGEINOI': 3121, 'LTP': 6.35, 'trendschangeOI': [3121],
                   'trends': [0, 0, 0, 0, 0]}}, 8650: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8700: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1000, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 4263, 'CHANGEINOI': 3881, 'LTP': 8.35, 'trendschangeOI': [3881],
                   'trends': [0, 0, 0, 0, 0]}}, 8750: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 8800: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 4958, 'CHANGEINOI': 3585, 'LTP': 10.9, 'trendschangeOI': [3585],
                   'trends': [0, 0, 0, 0, 0]}}, 8850: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 26, 'CHANGEINOI': 23, 'LTP': 13.35, 'trendschangeOI': [23], 'trends': [0, 0, 0, 0, 0]}},
                  8900: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 3879, 'CHANGEINOI': 2560, 'LTP': 14.8, 'trendschangeOI': [2560],
                             'trends': [0, 0, 0, 0, 0]}}, 8950: {
            'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 406, 'CHANGEINOI': 398, 'LTP': 16.8, 'trendschangeOI': [398], 'trends': [0, 0, 0, 0, 0]}},
                  9000: {'CE': {'OI': 208, 'CHANGEINOI': 183, 'LTP': 762, 'trendschangeOI': [183],
                                'trends': [0, 0, 0, 0, 0]},
                         'PE': {'OI': 24957, 'CHANGEINOI': 11132, 'LTP': 19.7, 'trendschangeOI': [11132],
                                'trends': [0, 0, 0, 0, 0]}}, 9050: {
            'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 645.4, 'trendschangeOI': [1], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 827, 'CHANGEINOI': 794, 'LTP': 22.75, 'trendschangeOI': [794],
                   'trends': [0, 0, 0, 0, 0]}}, 9100: {
            'CE': {'OI': 88, 'CHANGEINOI': 1, 'LTP': 693.9, 'trendschangeOI': [1], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 8066, 'CHANGEINOI': 4383, 'LTP': 26.4, 'trendschangeOI': [4383],
                   'trends': [0, 0, 0, 0, 0]}}, 9150: {
            'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 648.8, 'trendschangeOI': [1], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 987, 'CHANGEINOI': 927, 'LTP': 30.45, 'trendschangeOI': [927],
                   'trends': [0, 0, 0, 0, 0]}}, 9200: {
            'CE': {'OI': 68, 'CHANGEINOI': 45, 'LTP': 548.6, 'trendschangeOI': [45], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 13260, 'CHANGEINOI': 7697, 'LTP': 35.5, 'trendschangeOI': [7697],
                   'trends': [0, 0, 0, 0, 0]}}, 9250: {
            'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 540.7, 'trendschangeOI': [1], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1319, 'CHANGEINOI': 876, 'LTP': 40.9, 'trendschangeOI': [876],
                   'trends': [0, 0, 0, 0, 0]}}, 9300: {
            'CE': {'OI': 435, 'CHANGEINOI': -17, 'LTP': 498.45, 'trendschangeOI': [-17],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 19759, 'CHANGEINOI': 11672, 'LTP': 47.35, 'trendschangeOI': [11672],
                   'trends': [0, 0, 0, 0, 0]}}, 9350: {
            'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 420.3, 'trendschangeOI': [5], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1681, 'CHANGEINOI': 1401, 'LTP': 54.7, 'trendschangeOI': [1401],
                   'trends': [0, 0, 0, 0, 0]}}, 9400: {
            'CE': {'OI': 475, 'CHANGEINOI': 321, 'LTP': 403.05, 'trendschangeOI': [321],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 19230, 'CHANGEINOI': 12041, 'LTP': 63.25, 'trendschangeOI': [12041],
                   'trends': [0, 0, 0, 0, 0]}}, 9450: {
            'CE': {'OI': 38, 'CHANGEINOI': 37, 'LTP': 356.1, 'trendschangeOI': [37], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1728, 'CHANGEINOI': 1137, 'LTP': 72.45, 'trendschangeOI': [1137],
                   'trends': [0, 0, 0, 0, 0]}}, 9500: {
            'CE': {'OI': 3095, 'CHANGEINOI': 1764, 'LTP': 327.7, 'trendschangeOI': [1764],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 27223, 'CHANGEINOI': 10920, 'LTP': 83.95, 'trendschangeOI': [10920],
                   'trends': [0, 0, 0, 0, 0]}}, 9550: {
            'CE': {'OI': 158, 'CHANGEINOI': 155, 'LTP': 290.8, 'trendschangeOI': [155], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 2061, 'CHANGEINOI': 1622, 'LTP': 96.3, 'trendschangeOI': [1622],
                   'trends': [0, 0, 0, 0, 0]}}, 9600: {
            'CE': {'OI': 4954, 'CHANGEINOI': 4638, 'LTP': 254, 'trendschangeOI': [4638],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 19943, 'CHANGEINOI': 10739, 'LTP': 111.3, 'trendschangeOI': [10739],
                   'trends': [0, 0, 0, 0, 0]}}, 9650: {
            'CE': {'OI': 1031, 'CHANGEINOI': 1026, 'LTP': 220.45, 'trendschangeOI': [1026],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 2716, 'CHANGEINOI': 1985, 'LTP': 128, 'trendschangeOI': [1985],
                   'trends': [0, 0, 0, 0, 0]}}, 9700: {
            'CE': {'OI': 12192, 'CHANGEINOI': 11421, 'LTP': 189, 'trendschangeOI': [11421],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 19048, 'CHANGEINOI': 9555, 'LTP': 146.55, 'trendschangeOI': [9555],
                   'trends': [0, 0, 0, 0, 0]}}, 9750: {
            'CE': {'OI': 2112, 'CHANGEINOI': 2108, 'LTP': 161, 'trendschangeOI': [2108],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 2127, 'CHANGEINOI': 847, 'LTP': 167, 'trendschangeOI': [847], 'trends': [0, 0, 0, 0, 0]}},
                  9800: {'CE': {'OI': 17692, 'CHANGEINOI': 14332, 'LTP': 135.6, 'trendschangeOI': [14332],
                                'trends': [0, 0, 0, 0, 0]},
                         'PE': {'OI': 9227, 'CHANGEINOI': -1580, 'LTP': 191.9, 'trendschangeOI': [-1580],
                                'trends': [0, 0, 0, 0, 0]}}, 9850: {
            'CE': {'OI': 1329, 'CHANGEINOI': 1225, 'LTP': 112.4, 'trendschangeOI': [1225],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 935, 'CHANGEINOI': 29, 'LTP': 220.55, 'trendschangeOI': [29], 'trends': [0, 0, 0, 0, 0]}},
                  9900: {'CE': {'OI': 22471, 'CHANGEINOI': 14108, 'LTP': 91.4, 'trendschangeOI': [14108],
                                'trends': [0, 0, 0, 0, 0]},
                         'PE': {'OI': 6347, 'CHANGEINOI': -3808, 'LTP': 247.15, 'trendschangeOI': [-3808],
                                'trends': [0, 0, 0, 0, 0]}}, 9950: {
            'CE': {'OI': 2331, 'CHANGEINOI': 1476, 'LTP': 74.9, 'trendschangeOI': [1476],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 479, 'CHANGEINOI': -268, 'LTP': 279.4, 'trendschangeOI': [-268],
                   'trends': [0, 0, 0, 0, 0]}}, 10000: {
            'CE': {'OI': 27372, 'CHANGEINOI': 14047, 'LTP': 59.4, 'trendschangeOI': [14047],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 7289, 'CHANGEINOI': -652, 'LTP': 316, 'trendschangeOI': [-652],
                   'trends': [0, 0, 0, 0, 0]}}, 10050: {
            'CE': {'OI': 3253, 'CHANGEINOI': 1442, 'LTP': 46.9, 'trendschangeOI': [1442],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 664, 'CHANGEINOI': -59, 'LTP': 351.2, 'trendschangeOI': [-59],
                   'trends': [0, 0, 0, 0, 0]}}, 10100: {
            'CE': {'OI': 16883, 'CHANGEINOI': 2777, 'LTP': 36.45, 'trendschangeOI': [2777],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 4031, 'CHANGEINOI': -379, 'LTP': 391.55, 'trendschangeOI': [-379],
                   'trends': [0, 0, 0, 0, 0]}}, 10150: {
            'CE': {'OI': 4716, 'CHANGEINOI': 2969, 'LTP': 28.4, 'trendschangeOI': [2969],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 181, 'CHANGEINOI': -38, 'LTP': 427.1, 'trendschangeOI': [-38],
                   'trends': [0, 0, 0, 0, 0]}}, 10200: {
            'CE': {'OI': 16725, 'CHANGEINOI': 2780, 'LTP': 22.25, 'trendschangeOI': [2780],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1027, 'CHANGEINOI': -212, 'LTP': 475.55, 'trendschangeOI': [-212],
                   'trends': [0, 0, 0, 0, 0]}}, 10250: {
            'CE': {'OI': 2052, 'CHANGEINOI': 578, 'LTP': 17.4, 'trendschangeOI': [578], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 93, 'CHANGEINOI': -17, 'LTP': 505.85, 'trendschangeOI': [-17],
                   'trends': [0, 0, 0, 0, 0]}}, 10300: {
            'CE': {'OI': 18253, 'CHANGEINOI': 4187, 'LTP': 13.75, 'trendschangeOI': [4187],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 893, 'CHANGEINOI': -246, 'LTP': 556.95, 'trendschangeOI': [-246],
                   'trends': [0, 0, 0, 0, 0]}}, 10350: {
            'CE': {'OI': 1413, 'CHANGEINOI': 296, 'LTP': 11.1, 'trendschangeOI': [296], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 31, 'CHANGEINOI': 00, 'LTP': 614, 'trendschangeOI': [00], 'trends': [0, 0, 0, 0, 0]}},
                  10400: {'CE': {'OI': 13512, 'CHANGEINOI': 2002, 'LTP': 9.25, 'trendschangeOI': [2002],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 164, 'CHANGEINOI': -14, 'LTP': 656, 'trendschangeOI': [-14],
                                 'trends': [0, 0, 0, 0, 0]}}, 10450: {
            'CE': {'OI': 785, 'CHANGEINOI': 1, 'LTP': 7.7, 'trendschangeOI': [1], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 7, 'CHANGEINOI': 0, 'LTP': 732.7, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  10500: {'CE': {'OI': 26254, 'CHANGEINOI': 7328, 'LTP': 6.55, 'trendschangeOI': [7328],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 647, 'CHANGEINOI': -3, 'LTP': 749.5, 'trendschangeOI': [-3],
                                 'trends': [0, 0, 0, 0, 0]}}, 10550: {
            'CE': {'OI': 806, 'CHANGEINOI': 17, 'LTP': 5.35, 'trendschangeOI': [17], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 10600: {
            'CE': {'OI': 11536, 'CHANGEINOI': 2005, 'LTP': 4.65, 'trendschangeOI': [2005],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 49, 'CHANGEINOI': 0, 'LTP': 889.45, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  10650: {'CE': {'OI': 825, 'CHANGEINOI': 404, 'LTP': 4.2, 'trendschangeOI': [404],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 10700: {
            'CE': {'OI': 7842, 'CHANGEINOI': 97, 'LTP': 3.25, 'trendschangeOI': [97], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 934.65, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  10750: {'CE': {'OI': 432, 'CHANGEINOI': 16, 'LTP': 3, 'trendschangeOI': [16],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 10800: {
            'CE': {'OI': 5056, 'CHANGEINOI': -1010, 'LTP': 2.25, 'trendschangeOI': [-1010],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 1110.4, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  10850: {'CE': {'OI': 104, 'CHANGEINOI': 27, 'LTP': 2.05, 'trendschangeOI': [27],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 10900: {
            'CE': {'OI': 2261, 'CHANGEINOI': -419, 'LTP': 1.7, 'trendschangeOI': [-419],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 10950: {
            'CE': {'OI': 144, 'CHANGEINOI': 102, 'LTP': 1.6, 'trendschangeOI': [102], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11000: {
            'CE': {'OI': 12605, 'CHANGEINOI': -460, 'LTP': 1.4, 'trendschangeOI': [-460],
                   'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11050: {
            'CE': {'OI': 71, 'CHANGEINOI': 21, 'LTP': 1.5, 'trendschangeOI': [21], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11100: {
            'CE': {'OI': 656, 'CHANGEINOI': -244, 'LTP': 1.2, 'trendschangeOI': [-244], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11150: {
            'CE': {'OI': 49, 'CHANGEINOI': 7, 'LTP': 1.1, 'trendschangeOI': [7], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11200: {
            'CE': {'OI': 1734, 'CHANGEINOI': 111, 'LTP': 0.95, 'trendschangeOI': [111], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11250: {
            'CE': {'OI': 16, 'CHANGEINOI': 14, 'LTP': 1, 'trendschangeOI': [14], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11300: {
            'CE': {'OI': 179, 'CHANGEINOI': -8, 'LTP': 0.9, 'trendschangeOI': [-8], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 2, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11350: {
            'CE': {'OI': 7, 'CHANGEINOI': 5, 'LTP': 1.1, 'trendschangeOI': [5], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11400: {
            'CE': {'OI': 101, 'CHANGEINOI': 7, 'LTP': 0.8, 'trendschangeOI': [7], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11450: {
            'CE': {'OI': 34, 'CHANGEINOI': 4, 'LTP': 0.75, 'trendschangeOI': [4], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11500: {
            'CE': {'OI': 2597, 'CHANGEINOI': 367, 'LTP': 0.65, 'trendschangeOI': [367], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11550: {
            'CE': {'OI': 4, 'CHANGEINOI': 3, 'LTP': 0.5, 'trendschangeOI': [3], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11600: {
            'CE': {'OI': 39, 'CHANGEINOI': 15, 'LTP': 0.6, 'trendschangeOI': [15], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}, 11650: {
            'CE': {'OI': 162, 'CHANGEINOI': 108, 'LTP': 0.7, 'trendschangeOI': [108], 'trends': [0, 0, 0, 0, 0]},
            'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'TIME': '12:58:56', 'DATE': '12-Jun-2020',
                  'PRICE': 20058.5, 'turnoverPRICE': 20050, 14300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2565, 'CHANGEINOI': 2484, 'LTP': 6.3, 'trendschangeOI': [2484],
                            'trends': [0, 0, 0, 0, 0]}}, 14400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  14500: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 3.05, 'trendschangeOI': [1],
                             'trends': [0, 0, 0, 0, 0]}}, 14600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  14700: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 14800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  14900: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 15000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 430, 'CHANGEINOI': 430, 'LTP': 7.9, 'trendschangeOI': [430],
                            'trends': [0, 0, 0, 0, 0]}}, 15100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  15200: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 15300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  15400: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 9, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 15500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 946, 'CHANGEINOI': 946, 'LTP': 10.75, 'trendschangeOI': [946],
                            'trends': [0, 0, 0, 0, 0]}}, 15600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  15700: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 15800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  15900: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 16000: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 4197.3, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 7232, 'CHANGEINOI': 6079, 'LTP': 15.55, 'trendschangeOI': [6079],
                            'trends': [0, 0, 0, 0, 0]}}, 16100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  16200: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 13, 'CHANGEINOI': 13, 'LTP': 19, 'trendschangeOI': [13],
                             'trends': [0, 0, 0, 0, 0]}}, 16300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  16400: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                             'trends': [0, 0, 0, 0, 0]}}, 16500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3384.9, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4592, 'CHANGEINOI': 3890, 'LTP': 24.1, 'trendschangeOI': [3890],
                            'trends': [0, 0, 0, 0, 0]}}, 16600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  16700: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 25, 'CHANGEINOI': 25, 'LTP': 30, 'trendschangeOI': [25],
                             'trends': [0, 0, 0, 0, 0]}}, 16800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  16900: {
                      'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                      'PE': {'OI': 45, 'CHANGEINOI': 45, 'LTP': 37, 'trendschangeOI': [45],
                             'trends': [0, 0, 0, 0, 0]}}, 17000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3200, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 9657, 'CHANGEINOI': 7823, 'LTP': 39.25, 'trendschangeOI': [7823],
                            'trends': [0, 0, 0, 0, 0]}}, 17100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': 25, 'LTP': 42.7, 'trendschangeOI': [25],
                            'trends': [0, 0, 0, 0, 0]}}, 17200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 70, 'CHANGEINOI': 70, 'LTP': 46.95, 'trendschangeOI': [70],
                            'trends': [0, 0, 0, 0, 0]}}, 17300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 18, 'CHANGEINOI': 18, 'LTP': 49.05, 'trendschangeOI': [18],
                            'trends': [0, 0, 0, 0, 0]}}, 17400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 286, 'CHANGEINOI': 276, 'LTP': 57, 'trendschangeOI': [276],
                            'trends': [0, 0, 0, 0, 0]}}, 17500: {
                     'CE': {'OI': 5, 'CHANGEINOI': 2, 'LTP': 2350.35, 'trendschangeOI': [2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 10518, 'CHANGEINOI': 8928, 'LTP': 63.85, 'trendschangeOI': [8928],
                            'trends': [0, 0, 0, 0, 0]}}, 17600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 295, 'CHANGEINOI': 295, 'LTP': 69.3, 'trendschangeOI': [295],
                            'trends': [0, 0, 0, 0, 0]}}, 17700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2266.3, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 726, 'CHANGEINOI': 674, 'LTP': 76.4, 'trendschangeOI': [674],
                            'trends': [0, 0, 0, 0, 0]}}, 17800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1710, 'CHANGEINOI': 1607, 'LTP': 84.85, 'trendschangeOI': [1607],
                            'trends': [0, 0, 0, 0, 0]}}, 17900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 310, 'CHANGEINOI': 310, 'LTP': 92.9, 'trendschangeOI': [310],
                            'trends': [0, 0, 0, 0, 0]}}, 18000: {
                     'CE': {'OI': 78, 'CHANGEINOI': 21, 'LTP': 1950, 'trendschangeOI': [21],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 17243, 'CHANGEINOI': 11320, 'LTP': 102.75, 'trendschangeOI': [11320],
                            'trends': [0, 0, 0, 0, 0]}}, 18100: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 2217.05, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1329, 'CHANGEINOI': 1128, 'LTP': 114.4, 'trendschangeOI': [1128],
                            'trends': [0, 0, 0, 0, 0]}}, 18200: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1824, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1891, 'CHANGEINOI': 1794, 'LTP': 124.7, 'trendschangeOI': [1794],
                            'trends': [0, 0, 0, 0, 0]}}, 18300: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1620.9, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 896, 'CHANGEINOI': 882, 'LTP': 136.95, 'trendschangeOI': [882],
                            'trends': [0, 0, 0, 0, 0]}}, 18400: {
                     'CE': {'OI': 11, 'CHANGEINOI': 11, 'LTP': 1779.75, 'trendschangeOI': [11],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1692, 'CHANGEINOI': 1618, 'LTP': 149.8, 'trendschangeOI': [1618],
                            'trends': [0, 0, 0, 0, 0]}}, 18500: {
                     'CE': {'OI': 154, 'CHANGEINOI': 67, 'LTP': 1765.7, 'trendschangeOI': [67],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 15489, 'CHANGEINOI': 9688, 'LTP': 163.4, 'trendschangeOI': [9688],
                            'trends': [0, 0, 0, 0, 0]}}, 18600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1663.4, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1323, 'CHANGEINOI': 1233, 'LTP': 180.1, 'trendschangeOI': [1233],
                            'trends': [0, 0, 0, 0, 0]}}, 18700: {
                     'CE': {'OI': 2, 'CHANGEINOI': 2, 'LTP': 1534.45, 'trendschangeOI': [2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1346, 'CHANGEINOI': 1110, 'LTP': 197.8, 'trendschangeOI': [1110],
                            'trends': [0, 0, 0, 0, 0]}}, 18800: {
                     'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 1558.95, 'trendschangeOI': [5],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2325, 'CHANGEINOI': 1868, 'LTP': 217.45, 'trendschangeOI': [1868],
                            'trends': [0, 0, 0, 0, 0]}}, 18900: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1250, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1581, 'CHANGEINOI': 1301, 'LTP': 237, 'trendschangeOI': [1301],
                            'trends': [0, 0, 0, 0, 0]}}, 19000: {
                     'CE': {'OI': 989, 'CHANGEINOI': 747, 'LTP': 1280.5, 'trendschangeOI': [747],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 24119, 'CHANGEINOI': 12026, 'LTP': 260.7, 'trendschangeOI': [12026],
                            'trends': [0, 0, 0, 0, 0]}}, 19100: {
                     'CE': {'OI': 9, 'CHANGEINOI': 9, 'LTP': 1355.8, 'trendschangeOI': [9],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1724, 'CHANGEINOI': 1615, 'LTP': 286.2, 'trendschangeOI': [1615],
                            'trends': [0, 0, 0, 0, 0]}}, 19200: {
                     'CE': {'OI': 34, 'CHANGEINOI': 34, 'LTP': 1140.8, 'trendschangeOI': [34],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4686, 'CHANGEINOI': 4520, 'LTP': 313.9, 'trendschangeOI': [4520],
                            'trends': [0, 0, 0, 0, 0]}}, 19300: {
                     'CE': {'OI': 38, 'CHANGEINOI': 38, 'LTP': 1070, 'trendschangeOI': [38],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 3599, 'CHANGEINOI': 3231, 'LTP': 341.65, 'trendschangeOI': [3231],
                            'trends': [0, 0, 0, 0, 0]}}, 19400: {
                     'CE': {'OI': 56, 'CHANGEINOI': 56, 'LTP': 1025.2, 'trendschangeOI': [56],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1976, 'CHANGEINOI': 1468, 'LTP': 373.4, 'trendschangeOI': [1468],
                            'trends': [0, 0, 0, 0, 0]}}, 19500: {
                     'CE': {'OI': 3457, 'CHANGEINOI': 3245, 'LTP': 937, 'trendschangeOI': [3245],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 16628, 'CHANGEINOI': 2830, 'LTP': 403.85, 'trendschangeOI': [2830],
                            'trends': [0, 0, 0, 0, 0]}}, 19600: {
                     'CE': {'OI': 464, 'CHANGEINOI': 463, 'LTP': 864.2, 'trendschangeOI': [463],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2291, 'CHANGEINOI': 2103, 'LTP': 442.95, 'trendschangeOI': [2103],
                            'trends': [0, 0, 0, 0, 0]}}, 19700: {
                     'CE': {'OI': 1320, 'CHANGEINOI': 1320, 'LTP': 819, 'trendschangeOI': [1320],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4197, 'CHANGEINOI': 3603, 'LTP': 477.95, 'trendschangeOI': [3603],
                            'trends': [0, 0, 0, 0, 0]}}, 19800: {
                     'CE': {'OI': 2251, 'CHANGEINOI': 2250, 'LTP': 744.9, 'trendschangeOI': [2250],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4091, 'CHANGEINOI': 3618, 'LTP': 519.25, 'trendschangeOI': [3618],
                            'trends': [0, 0, 0, 0, 0]}}, 19900: {
                     'CE': {'OI': 1732, 'CHANGEINOI': 1730, 'LTP': 690.4, 'trendschangeOI': [1730],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 3513, 'CHANGEINOI': 3188, 'LTP': 563.1, 'trendschangeOI': [3188],
                            'trends': [0, 0, 0, 0, 0]}}, 20000: {
                     'CE': {'OI': 10783, 'CHANGEINOI': 9218, 'LTP': 636.8, 'trendschangeOI': [9218],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 11773, 'CHANGEINOI': 1652, 'LTP': 605, 'trendschangeOI': [1652],
                            'trends': [0, 0, 0, 0, 0]}}, 20100: {
                     'CE': {'OI': 1596, 'CHANGEINOI': 1596, 'LTP': 587.05, 'trendschangeOI': [1596],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1058, 'CHANGEINOI': 637, 'LTP': 654.65, 'trendschangeOI': [637],
                            'trends': [0, 0, 0, 0, 0]}}, 20200: {
                     'CE': {'OI': 2575, 'CHANGEINOI': 2543, 'LTP': 537.8, 'trendschangeOI': [2543],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 904, 'CHANGEINOI': -8, 'LTP': 710.45, 'trendschangeOI': [-8],
                            'trends': [0, 0, 0, 0, 0]}}, 20300: {
                     'CE': {'OI': 1659, 'CHANGEINOI': 1584, 'LTP': 492.2, 'trendschangeOI': [1584],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 595, 'CHANGEINOI': -379, 'LTP': 760, 'trendschangeOI': [-379],
                            'trends': [0, 0, 0, 0, 0]}}, 20400: {
                     'CE': {'OI': 2170, 'CHANGEINOI': 2044, 'LTP': 447.9, 'trendschangeOI': [2044],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 727, 'CHANGEINOI': -12, 'LTP': 805.85, 'trendschangeOI': [-12],
                            'trends': [0, 0, 0, 0, 0]}}, 20500: {
                     'CE': {'OI': 10743, 'CHANGEINOI': 6640, 'LTP': 408.35, 'trendschangeOI': [6640],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4316, 'CHANGEINOI': -1548, 'LTP': 883, 'trendschangeOI': [-1548],
                            'trends': [0, 0, 0, 0, 0]}}, 20600: {
                     'CE': {'OI': 2225, 'CHANGEINOI': 1281, 'LTP': 371.05, 'trendschangeOI': [1281],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 351, 'CHANGEINOI': -162, 'LTP': 930, 'trendschangeOI': [-162],
                            'trends': [0, 0, 0, 0, 0]}}, 20700: {
                     'CE': {'OI': 2187, 'CHANGEINOI': 1334, 'LTP': 334.3, 'trendschangeOI': [1334],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 370, 'CHANGEINOI': -40, 'LTP': 985.5, 'trendschangeOI': [-40],
                            'trends': [0, 0, 0, 0, 0]}}, 20800: {
                     'CE': {'OI': 3606, 'CHANGEINOI': 2308, 'LTP': 302, 'trendschangeOI': [2308],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 371, 'CHANGEINOI': -109, 'LTP': 1075.15, 'trendschangeOI': [-109],
                            'trends': [0, 0, 0, 0, 0]}}, 20900: {
                     'CE': {'OI': 1921, 'CHANGEINOI': 1409, 'LTP': 272.35, 'trendschangeOI': [1409],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 239, 'CHANGEINOI': -45, 'LTP': 1146.95, 'trendschangeOI': [-45],
                            'trends': [0, 0, 0, 0, 0]}}, 21000: {
                     'CE': {'OI': 21142, 'CHANGEINOI': 10221, 'LTP': 245.4, 'trendschangeOI': [10221],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 3829, 'CHANGEINOI': -354, 'LTP': 1217.35, 'trendschangeOI': [-354],
                            'trends': [0, 0, 0, 0, 0]}}, 21100: {
                     'CE': {'OI': 2324, 'CHANGEINOI': 1514, 'LTP': 219.25, 'trendschangeOI': [1514],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 353, 'CHANGEINOI': -20, 'LTP': 1291.2, 'trendschangeOI': [-20],
                            'trends': [0, 0, 0, 0, 0]}}, 21200: {
                     'CE': {'OI': 2950, 'CHANGEINOI': 1453, 'LTP': 197.35, 'trendschangeOI': [1453],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 155, 'CHANGEINOI': -19, 'LTP': 1510.2, 'trendschangeOI': [-19],
                            'trends': [0, 0, 0, 0, 0]}}, 21300: {
                     'CE': {'OI': 2560, 'CHANGEINOI': 1510, 'LTP': 175.95, 'trendschangeOI': [1510],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 87, 'CHANGEINOI': 0, 'LTP': 1498.5, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]}}, 21400: {
                     'CE': {'OI': 1557, 'CHANGEINOI': 677, 'LTP': 156.05, 'trendschangeOI': [677],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': -2, 'LTP': 1308.6, 'trendschangeOI': [-2],
                            'trends': [0, 0, 0, 0, 0]}}, 21500: {
                     'CE': {'OI': 16886, 'CHANGEINOI': 5571, 'LTP': 138.15, 'trendschangeOI': [5571],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 971, 'CHANGEINOI': -475, 'LTP': 1601.3, 'trendschangeOI': [-475],
                            'trends': [0, 0, 0, 0, 0]}}, 21600: {
                     'CE': {'OI': 2069, 'CHANGEINOI': 1375, 'LTP': 123.9, 'trendschangeOI': [1375],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 10, 'CHANGEINOI': 2, 'LTP': 1641.1, 'trendschangeOI': [2],
                            'trends': [0, 0, 0, 0, 0]}}, 21700: {
                     'CE': {'OI': 1905, 'CHANGEINOI': 1402, 'LTP': 109.3, 'trendschangeOI': [1402],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 13, 'CHANGEINOI': 0, 'LTP': 1959.1, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]}}, 21800: {
                     'CE': {'OI': 4357, 'CHANGEINOI': 3184, 'LTP': 95.95, 'trendschangeOI': [3184],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2, 'CHANGEINOI': 1, 'LTP': 2140.85, 'trendschangeOI': [1],
                            'trends': [0, 0, 0, 0, 0]}}, 21900: {
                     'CE': {'OI': 1370, 'CHANGEINOI': 957, 'LTP': 85.95, 'trendschangeOI': [957],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  22000: {'CE': {'OI': 19932, 'CHANGEINOI': 8904, 'LTP': 75.65, 'trendschangeOI': [8904],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 354, 'CHANGEINOI': -20, 'LTP': 2002.3, 'trendschangeOI': [-20],
                                 'trends': [0, 0, 0, 0, 0]}}, 22100: {
                     'CE': {'OI': 907, 'CHANGEINOI': 639, 'LTP': 67.75, 'trendschangeOI': [639],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  22200: {'CE': {'OI': 1210, 'CHANGEINOI': 710, 'LTP': 59.7, 'trendschangeOI': [710],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 22300: {
                     'CE': {'OI': 824, 'CHANGEINOI': 634, 'LTP': 52.65, 'trendschangeOI': [634],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  22400: {'CE': {'OI': 784, 'CHANGEINOI': 473, 'LTP': 47.65, 'trendschangeOI': [473],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 22500: {
                     'CE': {'OI': 12721, 'CHANGEINOI': 4640, 'LTP': 41.6, 'trendschangeOI': [4640],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  22600: {'CE': {'OI': 1088, 'CHANGEINOI': 445, 'LTP': 37.55, 'trendschangeOI': [445],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 22700: {
                     'CE': {'OI': 681, 'CHANGEINOI': 485, 'LTP': 32.15, 'trendschangeOI': [485],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  22800: {'CE': {'OI': 726, 'CHANGEINOI': 435, 'LTP': 29.6, 'trendschangeOI': [435],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 22900: {
                     'CE': {'OI': 690, 'CHANGEINOI': 376, 'LTP': 25.8, 'trendschangeOI': [376],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  23000: {'CE': {'OI': 13319, 'CHANGEINOI': 2525, 'LTP': 22.05, 'trendschangeOI': [2525],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 33, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 23100: {
                     'CE': {'OI': 350, 'CHANGEINOI': 240, 'LTP': 19.85, 'trendschangeOI': [240],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  23200: {'CE': {'OI': 754, 'CHANGEINOI': 157, 'LTP': 17, 'trendschangeOI': [157],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 23300: {
                     'CE': {'OI': 17, 'CHANGEINOI': 17, 'LTP': 14, 'trendschangeOI': [17],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  23400: {'CE': {'OI': 196, 'CHANGEINOI': 70, 'LTP': 12.8, 'trendschangeOI': [70],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 23500: {
                     'CE': {'OI': 8701, 'CHANGEINOI': 2758, 'LTP': 11.8, 'trendschangeOI': [2758],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  23600: {'CE': {'OI': 122, 'CHANGEINOI': 107, 'LTP': 9.8, 'trendschangeOI': [107],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 23700: {
                     'CE': {'OI': 124, 'CHANGEINOI': 124, 'LTP': 8.4, 'trendschangeOI': [124],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  23800: {'CE': {'OI': 302, 'CHANGEINOI': 171, 'LTP': 9.55, 'trendschangeOI': [171],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 23900: {
                     'CE': {'OI': 402, 'CHANGEINOI': 206, 'LTP': 8.9, 'trendschangeOI': [206],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  24000: {'CE': {'OI': 5634, 'CHANGEINOI': 1267, 'LTP': 7, 'trendschangeOI': [1267],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 24100: {
                     'CE': {'OI': 47, 'CHANGEINOI': 38, 'LTP': 6.3, 'trendschangeOI': [38],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  24200: {'CE': {'OI': 59, 'CHANGEINOI': 34, 'LTP': 6.75, 'trendschangeOI': [34],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 24300: {
                     'CE': {'OI': 56, 'CHANGEINOI': 16, 'LTP': 6.85, 'trendschangeOI': [16],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0], 'trends': [0, 0, 0, 0, 0]}},
                  24400: {'CE': {'OI': 172, 'CHANGEINOI': -61, 'LTP': 6.15, 'trendschangeOI': [-61],
                                 'trends': [0, 0, 0, 0, 0]},
                          'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                                 'trends': [0, 0, 0, 0, 0]}}, 24500: {
                     'CE': {'OI': 5359, 'CHANGEINOI': 945, 'LTP': 5.75, 'trendschangeOI': [945],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0],
                            'trends': [0, 0, 0, 0, 0]}}}],
                [{'index': 'NIFTY', 'marketstatus': True, 'TIME': '13:04:26', 'DATE': '12-Jun-2020', 'PRICE': 9766.8,
                  'turnoverPRICE': 9750, 7300: {'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                                                       'trends': [0, 0, 0, 0, 0]},
                                                'PE': {'OI': 79, 'CHANGEINOI': 53, 'LTP': 0.8,
                                                       'trendschangeOI': [53, 52], 'trends': [0, 0, 0, 0, 0]}},
                  7350: {'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                                'trends': [0, 0, 0, 0, 0]},
                         'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1.7, 'trendschangeOI': [1, 1],
                                'trends': [0, 0, 0, 0, 0]}}, 7400: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1.15, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7450: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0.75, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7500: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 835, 'CHANGEINOI': 830, 'LTP': 1.15, 'trendschangeOI': [830, 830],
                               'trends': [0, 0, 0, 0, 0]}}, 7550: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7600: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7650: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7700: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7750: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7800: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2.9, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7850: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7900: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 8, 'CHANGEINOI': 8, 'LTP': 1.95, 'trendschangeOI': [8, 8],
                               'trends': [0, 0, 0, 0, 0]}}, 7950: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8000: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3653, 'CHANGEINOI': 1760, 'LTP': 1.9, 'trendschangeOI': [1760, 1781],
                               'trends': [21, 0, 0, 0, 0]}}, 8050: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8100: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8150: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8200: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8250: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8300: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 303, 'CHANGEINOI': 303, 'LTP': 3, 'trendschangeOI': [303, 306],
                               'trends': [3, 0, 0, 0, 0]}}, 8350: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8400: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 737, 'CHANGEINOI': 735, 'LTP': 3.75, 'trendschangeOI': [735, 734],
                               'trends': [0, 0, 0, 0, 0]}}, 8450: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8500: {
                        'CE': {'OI': 6, 'CHANGEINOI': 0, 'LTP': 1210, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 7676, 'CHANGEINOI': 3750, 'LTP': 4.9, 'trendschangeOI': [3750, 3755],
                               'trends': [5, 0, 0, 0, 0]}}, 8550: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8600: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3172, 'CHANGEINOI': 3107, 'LTP': 6.4, 'trendschangeOI': [3107, 3121],
                               'trends': [14, 0, 0, 0, 0]}}, 8650: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8700: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1000, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 4408, 'CHANGEINOI': 4026, 'LTP': 8.3, 'trendschangeOI': [4026, 3881],
                               'trends': [-145, 0, 0, 0, 0]}}, 8750: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8800: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 4884, 'CHANGEINOI': 3511, 'LTP': 10.9, 'trendschangeOI': [3511, 3585],
                               'trends': [74, 0, 0, 0, 0]}}, 8850: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 25, 'CHANGEINOI': 22, 'LTP': 13.25, 'trendschangeOI': [22, 23],
                               'trends': [1, 0, 0, 0, 0]}}, 8900: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3874, 'CHANGEINOI': 2555, 'LTP': 14.6, 'trendschangeOI': [2555, 2560],
                               'trends': [5, 0, 0, 0, 0]}}, 8950: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 404, 'CHANGEINOI': 396, 'LTP': 17.3, 'trendschangeOI': [396, 398],
                               'trends': [2, 0, 0, 0, 0]}}, 9000: {
                        'CE': {'OI': 208, 'CHANGEINOI': 183, 'LTP': 765, 'trendschangeOI': [183, 183],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 24872, 'CHANGEINOI': 11047, 'LTP': 19.25, 'trendschangeOI': [11047, 11132],
                               'trends': [85, 0, 0, 0, 0]}}, 9050: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 645.4, 'trendschangeOI': [1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 828, 'CHANGEINOI': 795, 'LTP': 22.65, 'trendschangeOI': [795, 794],
                               'trends': [0, 0, 0, 0, 0]}}, 9100: {
                        'CE': {'OI': 88, 'CHANGEINOI': 1, 'LTP': 693.9, 'trendschangeOI': [1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 8068, 'CHANGEINOI': 4385, 'LTP': 25.9, 'trendschangeOI': [4385, 4383],
                               'trends': [-2, 0, 0, 0, 0]}}, 9150: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 648.8, 'trendschangeOI': [1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 988, 'CHANGEINOI': 928, 'LTP': 30.1, 'trendschangeOI': [928, 927],
                               'trends': [0, 0, 0, 0, 0]}}, 9200: {
                        'CE': {'OI': 68, 'CHANGEINOI': 45, 'LTP': 548.6, 'trendschangeOI': [45, 45],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 13331, 'CHANGEINOI': 7768, 'LTP': 34.45, 'trendschangeOI': [7768, 7697],
                               'trends': [-71, 0, 0, 0, 0]}}, 9250: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 540.7, 'trendschangeOI': [1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1331, 'CHANGEINOI': 888, 'LTP': 39.8, 'trendschangeOI': [888, 876],
                               'trends': [-12, 0, 0, 0, 0]}}, 9300: {
                        'CE': {'OI': 435, 'CHANGEINOI': -17, 'LTP': 498.45, 'trendschangeOI': [-17, -17],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 19457, 'CHANGEINOI': 11370, 'LTP': 46.65, 'trendschangeOI': [11370, 11672],
                               'trends': [302, 0, 0, 0, 0]}}, 9350: {
                        'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 420.3, 'trendschangeOI': [5, 5],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1703, 'CHANGEINOI': 1423, 'LTP': 53.45, 'trendschangeOI': [1423, 1401],
                               'trends': [-22, 0, 0, 0, 0]}}, 9400: {
                        'CE': {'OI': 474, 'CHANGEINOI': 320, 'LTP': 403.05, 'trendschangeOI': [320, 321],
                               'trends': [1, 0, 0, 0, 0]},
                        'PE': {'OI': 19384, 'CHANGEINOI': 12195, 'LTP': 62.05, 'trendschangeOI': [12195, 12041],
                               'trends': [-154, 0, 0, 0, 0]}}, 9450: {
                        'CE': {'OI': 38, 'CHANGEINOI': 37, 'LTP': 356.1, 'trendschangeOI': [37, 37],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1687, 'CHANGEINOI': 1096, 'LTP': 71, 'trendschangeOI': [1096, 1137],
                               'trends': [41, 0, 0, 0, 0]}}, 9500: {
                        'CE': {'OI': 3041, 'CHANGEINOI': 1710, 'LTP': 333.95, 'trendschangeOI': [1710, 1764],
                               'trends': [54, 0, 0, 0, 0]},
                        'PE': {'OI': 27460, 'CHANGEINOI': 11157, 'LTP': 82.3, 'trendschangeOI': [11157, 10920],
                               'trends': [-237, 0, 0, 0, 0]}}, 9550: {
                        'CE': {'OI': 134, 'CHANGEINOI': 131, 'LTP': 293, 'trendschangeOI': [131, 155],
                               'trends': [24, 0, 0, 0, 0]},
                        'PE': {'OI': 2004, 'CHANGEINOI': 1565, 'LTP': 95.45, 'trendschangeOI': [1565, 1622],
                               'trends': [57, 0, 0, 0, 0]}}, 9600: {
                        'CE': {'OI': 4909, 'CHANGEINOI': 4593, 'LTP': 260.9, 'trendschangeOI': [4593, 4638],
                               'trends': [45, 0, 0, 0, 0]},
                        'PE': {'OI': 19989, 'CHANGEINOI': 10785, 'LTP': 109.2, 'trendschangeOI': [10785, 10739],
                               'trends': [-46, 0, 0, 0, 0]}}, 9650: {
                        'CE': {'OI': 1005, 'CHANGEINOI': 1000, 'LTP': 224.55, 'trendschangeOI': [1000, 1026],
                               'trends': [26, 0, 0, 0, 0]},
                        'PE': {'OI': 2736, 'CHANGEINOI': 2005, 'LTP': 125, 'trendschangeOI': [2005, 1985],
                               'trends': [-20, 0, 0, 0, 0]}}, 9700: {
                        'CE': {'OI': 12076, 'CHANGEINOI': 11305, 'LTP': 195.6, 'trendschangeOI': [11305, 11421],
                               'trends': [116, 0, 0, 0, 0]},
                        'PE': {'OI': 18945, 'CHANGEINOI': 9452, 'LTP': 143.15, 'trendschangeOI': [9452, 9555],
                               'trends': [103, 0, 0, 0, 0]}}, 9750: {
                        'CE': {'OI': 2206, 'CHANGEINOI': 2202, 'LTP': 166.5, 'trendschangeOI': [2202, 2108],
                               'trends': [-94, 0, 0, 0, 0]},
                        'PE': {'OI': 2274, 'CHANGEINOI': 994, 'LTP': 164.75, 'trendschangeOI': [994, 847],
                               'trends': [-147, 0, 0, 0, 0]}}, 9800: {
                        'CE': {'OI': 17474, 'CHANGEINOI': 14114, 'LTP': 139.75, 'trendschangeOI': [14114, 14332],
                               'trends': [218, 0, 0, 0, 0]},
                        'PE': {'OI': 9197, 'CHANGEINOI': -1610, 'LTP': 188.7, 'trendschangeOI': [-1610, -1580],
                               'trends': [30, 0, 0, 0, 0]}}, 9850: {
                        'CE': {'OI': 1301, 'CHANGEINOI': 1197, 'LTP': 115.75, 'trendschangeOI': [1197, 1225],
                               'trends': [28, 0, 0, 0, 0]},
                        'PE': {'OI': 905, 'CHANGEINOI': 0, 'LTP': 214.1, 'trendschangeOI': [0, 29],
                               'trends': [30, 0, 0, 0, 0]}}, 9900: {
                        'CE': {'OI': 22392, 'CHANGEINOI': 14029, 'LTP': 95.6, 'trendschangeOI': [14029, 14108],
                               'trends': [79, 0, 0, 0, 0]},
                        'PE': {'OI': 6381, 'CHANGEINOI': -3774, 'LTP': 243, 'trendschangeOI': [-3774, -3808],
                               'trends': [-34, 0, 0, 0, 0]}}, 9950: {
                        'CE': {'OI': 2283, 'CHANGEINOI': 1428, 'LTP': 76.85, 'trendschangeOI': [1428, 1476],
                               'trends': [48, 0, 0, 0, 0]},
                        'PE': {'OI': 478, 'CHANGEINOI': -269, 'LTP': 288, 'trendschangeOI': [-269, -268],
                               'trends': [1, 0, 0, 0, 0]}}, 10000: {
                        'CE': {'OI': 27323, 'CHANGEINOI': 13998, 'LTP': 61.05, 'trendschangeOI': [13998, 14047],
                               'trends': [49, 0, 0, 0, 0]},
                        'PE': {'OI': 7255, 'CHANGEINOI': -686, 'LTP': 307.35, 'trendschangeOI': [-686, -652],
                               'trends': [34, 0, 0, 0, 0]}}, 10050: {
                        'CE': {'OI': 3205, 'CHANGEINOI': 1394, 'LTP': 48.15, 'trendschangeOI': [1394, 1442],
                               'trends': [48, 0, 0, 0, 0]},
                        'PE': {'OI': 663, 'CHANGEINOI': -60, 'LTP': 352, 'trendschangeOI': [-60, -59],
                               'trends': [1, 0, 0, 0, 0]}}, 10100: {
                        'CE': {'OI': 16910, 'CHANGEINOI': 2804, 'LTP': 37.6, 'trendschangeOI': [2804, 2777],
                               'trends': [-27, 0, 0, 0, 0]},
                        'PE': {'OI': 4041, 'CHANGEINOI': -369, 'LTP': 384.2, 'trendschangeOI': [-369, -379],
                               'trends': [00, 0, 0, 0, 0]}}, 10150: {
                        'CE': {'OI': 4695, 'CHANGEINOI': 2948, 'LTP': 29.25, 'trendschangeOI': [2948, 2969],
                               'trends': [21, 0, 0, 0, 0]},
                        'PE': {'OI': 181, 'CHANGEINOI': -38, 'LTP': 427.1, 'trendschangeOI': [-38, -38],
                               'trends': [0, 0, 0, 0, 0]}}, 10200: {
                        'CE': {'OI': 16665, 'CHANGEINOI': 2720, 'LTP': 22.85, 'trendschangeOI': [2720, 2780],
                               'trends': [60, 0, 0, 0, 0]},
                        'PE': {'OI': 1027, 'CHANGEINOI': -212, 'LTP': 471.45, 'trendschangeOI': [-212, -212],
                               'trends': [0, 0, 0, 0, 0]}}, 10250: {
                        'CE': {'OI': 2094, 'CHANGEINOI': 620, 'LTP': 17.85, 'trendschangeOI': [620, 578],
                               'trends': [-42, 0, 0, 0, 0]},
                        'PE': {'OI': 93, 'CHANGEINOI': -17, 'LTP': 505.85, 'trendschangeOI': [-17, -17],
                               'trends': [0, 0, 0, 0, 0]}}, 10300: {
                        'CE': {'OI': 18182, 'CHANGEINOI': 4116, 'LTP': 14.2, 'trendschangeOI': [4116, 4187],
                               'trends': [71, 0, 0, 0, 0]},
                        'PE': {'OI': 893, 'CHANGEINOI': -246, 'LTP': 559.1, 'trendschangeOI': [-246, -246],
                               'trends': [0, 0, 0, 0, 0]}}, 10350: {
                        'CE': {'OI': 1402, 'CHANGEINOI': 285, 'LTP': 11.25, 'trendschangeOI': [285, 296],
                               'trends': [11, 0, 0, 0, 0]},
                        'PE': {'OI': 31, 'CHANGEINOI': 00, 'LTP': 614, 'trendschangeOI': [00, 00],
                               'trends': [0, 0, 0, 0, 0]}}, 10400: {
                        'CE': {'OI': 13473, 'CHANGEINOI': 1963, 'LTP': 9.4, 'trendschangeOI': [1963, 2002],
                               'trends': [39, 0, 0, 0, 0]},
                        'PE': {'OI': 165, 'CHANGEINOI': -13, 'LTP': 670.75, 'trendschangeOI': [-13, -14],
                               'trends': [0, 0, 0, 0, 0]}}, 10450: {
                        'CE': {'OI': 809, 'CHANGEINOI': 25, 'LTP': 7.9, 'trendschangeOI': [25, 1],
                               'trends': [-24, 0, 0, 0, 0]},
                        'PE': {'OI': 7, 'CHANGEINOI': 0, 'LTP': 732.7, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10500: {
                        'CE': {'OI': 26352, 'CHANGEINOI': 7426, 'LTP': 6.7, 'trendschangeOI': [7426, 7328],
                               'trends': [-98, 0, 0, 0, 0]},
                        'PE': {'OI': 647, 'CHANGEINOI': -3, 'LTP': 749.5, 'trendschangeOI': [-3, -3],
                               'trends': [0, 0, 0, 0, 0]}}, 10550: {
                        'CE': {'OI': 818, 'CHANGEINOI': 29, 'LTP': 5.5, 'trendschangeOI': [29, 17],
                               'trends': [-12, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10600: {
                        'CE': {'OI': 11603, 'CHANGEINOI': 2072, 'LTP': 4.7, 'trendschangeOI': [2072, 2005],
                               'trends': [-67, 0, 0, 0, 0]},
                        'PE': {'OI': 49, 'CHANGEINOI': 0, 'LTP': 889.45, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10650: {
                        'CE': {'OI': 812, 'CHANGEINOI': 391, 'LTP': 3.95, 'trendschangeOI': [391, 404],
                               'trends': [13, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10700: {
                        'CE': {'OI': 7791, 'CHANGEINOI': 46, 'LTP': 3.25, 'trendschangeOI': [46, 97],
                               'trends': [51, 0, 0, 0, 0]},
                        'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 934.65, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10750: {
                        'CE': {'OI': 433, 'CHANGEINOI': 17, 'LTP': 2.85, 'trendschangeOI': [17, 16],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10800: {
                        'CE': {'OI': 5115, 'CHANGEINOI': -951, 'LTP': 2.25, 'trendschangeOI': [-951, -1010],
                               'trends': [-59, 0, 0, 0, 0]},
                        'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 1110.4, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10850: {
                        'CE': {'OI': 104, 'CHANGEINOI': 27, 'LTP': 2.05, 'trendschangeOI': [27, 27],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10900: {
                        'CE': {'OI': 2294, 'CHANGEINOI': -386, 'LTP': 1.7, 'trendschangeOI': [-386, -419],
                               'trends': [-33, 0, 0, 0, 0]},
                        'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10950: {
                        'CE': {'OI': 144, 'CHANGEINOI': 102, 'LTP': 1.6, 'trendschangeOI': [102, 102],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11000: {
                        'CE': {'OI': 12775, 'CHANGEINOI': -290, 'LTP': 1.35, 'trendschangeOI': [-290, -460],
                               'trends': [-170, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11050: {
                        'CE': {'OI': 71, 'CHANGEINOI': 21, 'LTP': 1.5, 'trendschangeOI': [21, 21],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11100: {
                        'CE': {'OI': 657, 'CHANGEINOI': -243, 'LTP': 1.2, 'trendschangeOI': [-243, -244],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11150: {
                        'CE': {'OI': 49, 'CHANGEINOI': 7, 'LTP': 1.1, 'trendschangeOI': [7, 7],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11200: {
                        'CE': {'OI': 1749, 'CHANGEINOI': 126, 'LTP': 0.95, 'trendschangeOI': [126, 111],
                               'trends': [-15, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11250: {
                        'CE': {'OI': 16, 'CHANGEINOI': 14, 'LTP': 1, 'trendschangeOI': [14, 14],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11300: {
                        'CE': {'OI': 179, 'CHANGEINOI': -8, 'LTP': 0.9, 'trendschangeOI': [-8, -8],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 2, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11350: {
                        'CE': {'OI': 7, 'CHANGEINOI': 5, 'LTP': 1.1, 'trendschangeOI': [5, 5],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11400: {
                        'CE': {'OI': 101, 'CHANGEINOI': 7, 'LTP': 0.8, 'trendschangeOI': [7, 7],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11450: {
                        'CE': {'OI': 34, 'CHANGEINOI': 4, 'LTP': 0.75, 'trendschangeOI': [4, 4],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11500: {
                        'CE': {'OI': 2597, 'CHANGEINOI': 367, 'LTP': 0.7, 'trendschangeOI': [367, 367],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11550: {
                        'CE': {'OI': 4, 'CHANGEINOI': 3, 'LTP': 0.5, 'trendschangeOI': [3, 3],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11600: {
                        'CE': {'OI': 41, 'CHANGEINOI': 17, 'LTP': 0.6, 'trendschangeOI': [17, 15],
                               'trends': [-2, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11650: {
                        'CE': {'OI': 162, 'CHANGEINOI': 108, 'LTP': 0.7, 'trendschangeOI': [108, 108],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                               'trends': [0, 0, 0, 0, 0]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'TIME': '13:04:26', 'DATE': '12-Jun-2020',
                  'PRICE': 20058.05, 'turnoverPRICE': 20050, 14300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2581, 'CHANGEINOI': 2500, 'LTP': 6.3, 'trendschangeOI': [2500, 2484],
                            'trends': [-16, 0, 0, 0, 0]}}, 14400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 3.05, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]}}, 14600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 424, 'CHANGEINOI': 424, 'LTP': 7.35, 'trendschangeOI': [424, 430],
                            'trends': [6, 0, 0, 0, 0]}}, 15100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 9, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 928, 'CHANGEINOI': 928, 'LTP': 10.35, 'trendschangeOI': [928, 946],
                            'trends': [18, 0, 0, 0, 0]}}, 15600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16000: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 4197.3, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 7276, 'CHANGEINOI': 6123, 'LTP': 15.35, 'trendschangeOI': [6123, 6079],
                            'trends': [-44, 0, 0, 0, 0]}}, 16100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 13, 'CHANGEINOI': 13, 'LTP': 19, 'trendschangeOI': [13, 13],
                            'trends': [0, 0, 0, 0, 0]}}, 16300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3384.9, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4675, 'CHANGEINOI': 3973, 'LTP': 23.75, 'trendschangeOI': [3973, 3890],
                            'trends': [-83, 0, 0, 0, 0]}}, 16600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': 25, 'LTP': 30, 'trendschangeOI': [25, 25],
                            'trends': [0, 0, 0, 0, 0]}}, 16800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 45, 'CHANGEINOI': 45, 'LTP': 37, 'trendschangeOI': [45, 45],
                            'trends': [0, 0, 0, 0, 0]}}, 17000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3200, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 9747, 'CHANGEINOI': 7913, 'LTP': 38, 'trendschangeOI': [7913, 7823],
                            'trends': [-90, 0, 0, 0, 0]}}, 17100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': 25, 'LTP': 42.7, 'trendschangeOI': [25, 25],
                            'trends': [0, 0, 0, 0, 0]}}, 17200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 71, 'CHANGEINOI': 71, 'LTP': 45, 'trendschangeOI': [71, 70],
                            'trends': [0, 0, 0, 0, 0]}}, 17300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 18, 'CHANGEINOI': 18, 'LTP': 49.05, 'trendschangeOI': [18, 18],
                            'trends': [0, 0, 0, 0, 0]}}, 17400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 285, 'CHANGEINOI': 275, 'LTP': 55.15, 'trendschangeOI': [275, 276],
                            'trends': [1, 0, 0, 0, 0]}}, 17500: {
                     'CE': {'OI': 5, 'CHANGEINOI': 2, 'LTP': 2350.35, 'trendschangeOI': [2, 2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 10599, 'CHANGEINOI': 9009, 'LTP': 62.1, 'trendschangeOI': [9009, 8928],
                            'trends': [-81, 0, 0, 0, 0]}}, 17600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 285, 'CHANGEINOI': 285, 'LTP': 68.9, 'trendschangeOI': [285, 295],
                            'trends': [10, 0, 0, 0, 0]}}, 17700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2266.3, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 714, 'CHANGEINOI': 662, 'LTP': 75.15, 'trendschangeOI': [662, 674],
                            'trends': [12, 0, 0, 0, 0]}}, 17800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1749, 'CHANGEINOI': 1646, 'LTP': 83.45, 'trendschangeOI': [1646, 1607],
                            'trends': [-39, 0, 0, 0, 0]}}, 17900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 297, 'CHANGEINOI': 297, 'LTP': 92.6, 'trendschangeOI': [297, 310],
                            'trends': [13, 0, 0, 0, 0]}}, 18000: {
                     'CE': {'OI': 79, 'CHANGEINOI': 22, 'LTP': 2150, 'trendschangeOI': [22, 21],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 17316, 'CHANGEINOI': 11393, 'LTP': 101.05, 'trendschangeOI': [11393, 11320],
                            'trends': [-73, 0, 0, 0, 0]}}, 18100: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 2217.05, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1340, 'CHANGEINOI': 1139, 'LTP': 111.85, 'trendschangeOI': [1139, 1128],
                            'trends': [-11, 0, 0, 0, 0]}}, 18200: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1824, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1973, 'CHANGEINOI': 1876, 'LTP': 123.25, 'trendschangeOI': [1876, 1794],
                            'trends': [-82, 0, 0, 0, 0]}}, 18300: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1620.9, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 865, 'CHANGEINOI': 851, 'LTP': 135.25, 'trendschangeOI': [851, 882],
                            'trends': [31, 0, 0, 0, 0]}}, 18400: {
                     'CE': {'OI': 11, 'CHANGEINOI': 11, 'LTP': 1779.75, 'trendschangeOI': [11, 11],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1689, 'CHANGEINOI': 1615, 'LTP': 149.7, 'trendschangeOI': [1615, 1618],
                            'trends': [3, 0, 0, 0, 0]}}, 18500: {
                     'CE': {'OI': 154, 'CHANGEINOI': 67, 'LTP': 1670, 'trendschangeOI': [67, 67],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 15819, 'CHANGEINOI': 10018, 'LTP': 163.1, 'trendschangeOI': [10018, 9688],
                            'trends': [-330, 0, 0, 0, 0]}}, 18600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1663.4, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1332, 'CHANGEINOI': 1242, 'LTP': 180, 'trendschangeOI': [1242, 1233],
                            'trends': [-9, 0, 0, 0, 0]}}, 18700: {
                     'CE': {'OI': 2, 'CHANGEINOI': 2, 'LTP': 1534.45, 'trendschangeOI': [2, 2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1345, 'CHANGEINOI': 1109, 'LTP': 198, 'trendschangeOI': [1109, 1110],
                            'trends': [1, 0, 0, 0, 0]}}, 18800: {
                     'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 1558.95, 'trendschangeOI': [5, 5],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2363, 'CHANGEINOI': 1906, 'LTP': 217.35, 'trendschangeOI': [1906, 1868],
                            'trends': [-38, 0, 0, 0, 0]}}, 18900: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1250, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1599, 'CHANGEINOI': 1319, 'LTP': 238.1, 'trendschangeOI': [1319, 1301],
                            'trends': [-18, 0, 0, 0, 0]}}, 19000: {
                     'CE': {'OI': 977, 'CHANGEINOI': 735, 'LTP': 1293.9, 'trendschangeOI': [735, 747],
                            'trends': [12, 0, 0, 0, 0]},
                     'PE': {'OI': 24971, 'CHANGEINOI': 12878, 'LTP': 261.25, 'trendschangeOI': [12878, 12026],
                            'trends': [-852, 0, 0, 0, 0]}}, 19100: {
                     'CE': {'OI': 9, 'CHANGEINOI': 9, 'LTP': 1355.8, 'trendschangeOI': [9, 9],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1764, 'CHANGEINOI': 1655, 'LTP': 286.2, 'trendschangeOI': [1655, 1615],
                            'trends': [-40, 0, 0, 0, 0]}}, 19200: {
                     'CE': {'OI': 34, 'CHANGEINOI': 34, 'LTP': 1140.8, 'trendschangeOI': [34, 34],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4759, 'CHANGEINOI': 4593, 'LTP': 312.4, 'trendschangeOI': [4593, 4520],
                            'trends': [-73, 0, 0, 0, 0]}}, 19300: {
                     'CE': {'OI': 38, 'CHANGEINOI': 38, 'LTP': 1070, 'trendschangeOI': [38, 38],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 3646, 'CHANGEINOI': 3278, 'LTP': 342.5, 'trendschangeOI': [3278, 3231],
                            'trends': [-47, 0, 0, 0, 0]}}, 19400: {
                     'CE': {'OI': 46, 'CHANGEINOI': 46, 'LTP': 980.3, 'trendschangeOI': [46, 56],
                            'trends': [10, 0, 0, 0, 0]},
                     'PE': {'OI': 2007, 'CHANGEINOI': 1499, 'LTP': 370, 'trendschangeOI': [1499, 1468],
                            'trends': [-31, 0, 0, 0, 0]}}, 19500: {
                     'CE': {'OI': 3453, 'CHANGEINOI': 3241, 'LTP': 939.9, 'trendschangeOI': [3241, 3245],
                            'trends': [4, 0, 0, 0, 0]},
                     'PE': {'OI': 16751, 'CHANGEINOI': 2953, 'LTP': 404.95, 'trendschangeOI': [2953, 2830],
                            'trends': [-123, 0, 0, 0, 0]}}, 19600: {
                     'CE': {'OI': 485, 'CHANGEINOI': 484, 'LTP': 878.4, 'trendschangeOI': [484, 463],
                            'trends': [-21, 0, 0, 0, 0]},
                     'PE': {'OI': 2287, 'CHANGEINOI': 2099, 'LTP': 440, 'trendschangeOI': [2099, 2103],
                            'trends': [4, 0, 0, 0, 0]}}, 19700: {
                     'CE': {'OI': 1303, 'CHANGEINOI': 1303, 'LTP': 810, 'trendschangeOI': [1303, 1320],
                            'trends': [17, 0, 0, 0, 0]},
                     'PE': {'OI': 4274, 'CHANGEINOI': 3680, 'LTP': 479.8, 'trendschangeOI': [3680, 3603],
                            'trends': [-77, 0, 0, 0, 0]}}, 19800: {
                     'CE': {'OI': 2152, 'CHANGEINOI': 2151, 'LTP': 749.25, 'trendschangeOI': [2151, 2250],
                            'trends': [99, 0, 0, 0, 0]},
                     'PE': {'OI': 4257, 'CHANGEINOI': 3784, 'LTP': 518.25, 'trendschangeOI': [3784, 3618],
                            'trends': [-166, 0, 0, 0, 0]}}, 19900: {
                     'CE': {'OI': 1656, 'CHANGEINOI': 1654, 'LTP': 692.9, 'trendschangeOI': [1654, 1730],
                            'trends': [76, 0, 0, 0, 0]},
                     'PE': {'OI': 3586, 'CHANGEINOI': 3261, 'LTP': 563.15, 'trendschangeOI': [3261, 3188],
                            'trends': [-73, 0, 0, 0, 0]}}, 20000: {
                     'CE': {'OI': 10843, 'CHANGEINOI': 9278, 'LTP': 638, 'trendschangeOI': [9278, 9218],
                            'trends': [-60, 0, 0, 0, 0]},
                     'PE': {'OI': 12143, 'CHANGEINOI': 2022, 'LTP': 606, 'trendschangeOI': [2022, 1652],
                            'trends': [-370, 0, 0, 0, 0]}}, 20100: {
                     'CE': {'OI': 1696, 'CHANGEINOI': 1696, 'LTP': 588.55, 'trendschangeOI': [1696, 1596],
                            'trends': [000, 0, 0, 0, 0]},
                     'PE': {'OI': 1129, 'CHANGEINOI': 708, 'LTP': 657.8, 'trendschangeOI': [708, 637],
                            'trends': [-71, 0, 0, 0, 0]}}, 20200: {
                     'CE': {'OI': 2598, 'CHANGEINOI': 2566, 'LTP': 540.95, 'trendschangeOI': [2566, 2543],
                            'trends': [-23, 0, 0, 0, 0]},
                     'PE': {'OI': 901, 'CHANGEINOI': -11, 'LTP': 703.05, 'trendschangeOI': [-11, -8],
                            'trends': [3, 0, 0, 0, 0]}}, 20300: {
                     'CE': {'OI': 1797, 'CHANGEINOI': 1722, 'LTP': 496, 'trendschangeOI': [1722, 1584],
                            'trends': [-138, 0, 0, 0, 0]},
                     'PE': {'OI': 581, 'CHANGEINOI': -393, 'LTP': 754.05, 'trendschangeOI': [-393, -379],
                            'trends': [14, 0, 0, 0, 0]}}, 20400: {
                     'CE': {'OI': 2033, 'CHANGEINOI': 1907, 'LTP': 451.05, 'trendschangeOI': [1907, 2044],
                            'trends': [137, 0, 0, 0, 0]},
                     'PE': {'OI': 727, 'CHANGEINOI': -12, 'LTP': 814.7, 'trendschangeOI': [-12, -12],
                            'trends': [0, 0, 0, 0, 0]}}, 20500: {
                     'CE': {'OI': 11028, 'CHANGEINOI': 6925, 'LTP': 408.2, 'trendschangeOI': [6925, 6640],
                            'trends': [-285, 0, 0, 0, 0]},
                     'PE': {'OI': 4373, 'CHANGEINOI': -1491, 'LTP': 872, 'trendschangeOI': [-1491, -1548],
                            'trends': [-57, 0, 0, 0, 0]}}, 20600: {
                     'CE': {'OI': 2141, 'CHANGEINOI': 1197, 'LTP': 372.25, 'trendschangeOI': [1197, 1281],
                            'trends': [84, 0, 0, 0, 0]},
                     'PE': {'OI': 424, 'CHANGEINOI': -89, 'LTP': 942.45, 'trendschangeOI': [-89, -162],
                            'trends': [-73, 0, 0, 0, 0]}}, 20700: {
                     'CE': {'OI': 2227, 'CHANGEINOI': 1374, 'LTP': 334.75, 'trendschangeOI': [1374, 1334],
                            'trends': [-40, 0, 0, 0, 0]},
                     'PE': {'OI': 370, 'CHANGEINOI': -40, 'LTP': 994.4, 'trendschangeOI': [-40, -40],
                            'trends': [0, 0, 0, 0, 0]}}, 20800: {
                     'CE': {'OI': 3648, 'CHANGEINOI': 2350, 'LTP': 302.4, 'trendschangeOI': [2350, 2308],
                            'trends': [-42, 0, 0, 0, 0]},
                     'PE': {'OI': 365, 'CHANGEINOI': -115, 'LTP': 1096.55, 'trendschangeOI': [-115, -109],
                            'trends': [6, 0, 0, 0, 0]}}, 20900: {
                     'CE': {'OI': 1888, 'CHANGEINOI': 1376, 'LTP': 274.55, 'trendschangeOI': [1376, 1409],
                            'trends': [33, 0, 0, 0, 0]},
                     'PE': {'OI': 237, 'CHANGEINOI': -47, 'LTP': 1173.6, 'trendschangeOI': [-47, -45],
                            'trends': [2, 0, 0, 0, 0]}}, 21000: {
                     'CE': {'OI': 20894, 'CHANGEINOI': 9973, 'LTP': 245, 'trendschangeOI': [9973, 10221],
                            'trends': [248, 0, 0, 0, 0]},
                     'PE': {'OI': 3823, 'CHANGEINOI': -360, 'LTP': 1210.65, 'trendschangeOI': [-360, -354],
                            'trends': [6, 0, 0, 0, 0]}}, 21100: {
                     'CE': {'OI': 2368, 'CHANGEINOI': 1558, 'LTP': 220, 'trendschangeOI': [1558, 1514],
                            'trends': [-44, 0, 0, 0, 0]},
                     'PE': {'OI': 353, 'CHANGEINOI': -20, 'LTP': 1291.2, 'trendschangeOI': [-20, -20],
                            'trends': [0, 0, 0, 0, 0]}}, 21200: {
                     'CE': {'OI': 2725, 'CHANGEINOI': 1228, 'LTP': 196.8, 'trendschangeOI': [1228, 1453],
                            'trends': [225, 0, 0, 0, 0]},
                     'PE': {'OI': 155, 'CHANGEINOI': -19, 'LTP': 1510.2, 'trendschangeOI': [-19, -19],
                            'trends': [0, 0, 0, 0, 0]}}, 21300: {
                     'CE': {'OI': 2525, 'CHANGEINOI': 1475, 'LTP': 176.35, 'trendschangeOI': [1475, 1510],
                            'trends': [35, 0, 0, 0, 0]},
                     'PE': {'OI': 87, 'CHANGEINOI': 0, 'LTP': 1498.5, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 21400: {
                     'CE': {'OI': 1565, 'CHANGEINOI': 685, 'LTP': 155.4, 'trendschangeOI': [685, 677],
                            'trends': [-8, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': -2, 'LTP': 1308.6, 'trendschangeOI': [-2, -2],
                            'trends': [0, 0, 0, 0, 0]}}, 21500: {
                     'CE': {'OI': 17012, 'CHANGEINOI': 5697, 'LTP': 138.4, 'trendschangeOI': [5697, 5571],
                            'trends': [-126, 0, 0, 0, 0]},
                     'PE': {'OI': 968, 'CHANGEINOI': -478, 'LTP': 1601.15, 'trendschangeOI': [-478, -475],
                            'trends': [3, 0, 0, 0, 0]}}, 21600: {
                     'CE': {'OI': 1996, 'CHANGEINOI': 1302, 'LTP': 123.3, 'trendschangeOI': [1302, 1375],
                            'trends': [73, 0, 0, 0, 0]},
                     'PE': {'OI': 10, 'CHANGEINOI': 2, 'LTP': 1641.1, 'trendschangeOI': [2, 2],
                            'trends': [0, 0, 0, 0, 0]}}, 21700: {
                     'CE': {'OI': 1898, 'CHANGEINOI': 1395, 'LTP': 109.4, 'trendschangeOI': [1395, 1402],
                            'trends': [7, 0, 0, 0, 0]},
                     'PE': {'OI': 13, 'CHANGEINOI': 0, 'LTP': 1959.1, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 21800: {
                     'CE': {'OI': 4256, 'CHANGEINOI': 3083, 'LTP': 96.6, 'trendschangeOI': [3083, 3184],
                            'trends': [101, 0, 0, 0, 0]},
                     'PE': {'OI': 2, 'CHANGEINOI': 1, 'LTP': 2140.85, 'trendschangeOI': [1, 1],
                            'trends': [0, 0, 0, 0, 0]}}, 21900: {
                     'CE': {'OI': 1409, 'CHANGEINOI': 996, 'LTP': 85.9, 'trendschangeOI': [996, 957],
                            'trends': [-39, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22000: {
                     'CE': {'OI': 20080, 'CHANGEINOI': 9052, 'LTP': 76.1, 'trendschangeOI': [9052, 8904],
                            'trends': [-148, 0, 0, 0, 0]},
                     'PE': {'OI': 355, 'CHANGEINOI': -19, 'LTP': 2004.9, 'trendschangeOI': [-19, -20],
                            'trends': [0, 0, 0, 0, 0]}}, 22100: {
                     'CE': {'OI': 856, 'CHANGEINOI': 588, 'LTP': 67.4, 'trendschangeOI': [588, 639],
                            'trends': [51, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22200: {
                     'CE': {'OI': 1186, 'CHANGEINOI': 686, 'LTP': 59.35, 'trendschangeOI': [686, 710],
                            'trends': [24, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22300: {
                     'CE': {'OI': 805, 'CHANGEINOI': 615, 'LTP': 52.5, 'trendschangeOI': [615, 634],
                            'trends': [19, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22400: {
                     'CE': {'OI': 795, 'CHANGEINOI': 484, 'LTP': 46.65, 'trendschangeOI': [484, 473],
                            'trends': [-11, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22500: {
                     'CE': {'OI': 12837, 'CHANGEINOI': 4756, 'LTP': 41.25, 'trendschangeOI': [4756, 4640],
                            'trends': [-116, 0, 0, 0, 0]},
                     'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22600: {
                     'CE': {'OI': 1098, 'CHANGEINOI': 455, 'LTP': 36.85, 'trendschangeOI': [455, 445],
                            'trends': [00, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22700: {
                     'CE': {'OI': 689, 'CHANGEINOI': 493, 'LTP': 33.1, 'trendschangeOI': [493, 485],
                            'trends': [-8, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22800: {
                     'CE': {'OI': 728, 'CHANGEINOI': 437, 'LTP': 28.65, 'trendschangeOI': [437, 435],
                            'trends': [-2, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22900: {
                     'CE': {'OI': 688, 'CHANGEINOI': 374, 'LTP': 25.35, 'trendschangeOI': [374, 376],
                            'trends': [2, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23000: {
                     'CE': {'OI': 13043, 'CHANGEINOI': 2249, 'LTP': 22, 'trendschangeOI': [2249, 2525],
                            'trends': [276, 0, 0, 0, 0]},
                     'PE': {'OI': 33, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23100: {
                     'CE': {'OI': 351, 'CHANGEINOI': 241, 'LTP': 20.95, 'trendschangeOI': [241, 240],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23200: {
                     'CE': {'OI': 756, 'CHANGEINOI': 159, 'LTP': 16.5, 'trendschangeOI': [159, 157],
                            'trends': [-2, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23300: {
                     'CE': {'OI': 22, 'CHANGEINOI': 22, 'LTP': 14, 'trendschangeOI': [22, 17],
                            'trends': [-5, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23400: {
                     'CE': {'OI': 193, 'CHANGEINOI': 67, 'LTP': 12.95, 'trendschangeOI': [67, 70],
                            'trends': [3, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23500: {
                     'CE': {'OI': 8813, 'CHANGEINOI': 2870, 'LTP': 11.8, 'trendschangeOI': [2870, 2758],
                            'trends': [-112, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23600: {
                     'CE': {'OI': 121, 'CHANGEINOI': 106, 'LTP': 11, 'trendschangeOI': [106, 107],
                            'trends': [1, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23700: {
                     'CE': {'OI': 124, 'CHANGEINOI': 124, 'LTP': 11, 'trendschangeOI': [124, 124],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23800: {
                     'CE': {'OI': 307, 'CHANGEINOI': 176, 'LTP': 9.2, 'trendschangeOI': [176, 171],
                            'trends': [-5, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23900: {
                     'CE': {'OI': 409, 'CHANGEINOI': 213, 'LTP': 9.4, 'trendschangeOI': [213, 206],
                            'trends': [-7, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24000: {
                     'CE': {'OI': 5601, 'CHANGEINOI': 1234, 'LTP': 7.35, 'trendschangeOI': [1234, 1267],
                            'trends': [33, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24100: {
                     'CE': {'OI': 47, 'CHANGEINOI': 38, 'LTP': 6.3, 'trendschangeOI': [38, 38],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24200: {
                     'CE': {'OI': 59, 'CHANGEINOI': 34, 'LTP': 6.75, 'trendschangeOI': [34, 34],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24300: {
                     'CE': {'OI': 56, 'CHANGEINOI': 16, 'LTP': 6.85, 'trendschangeOI': [16, 16],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24400: {
                     'CE': {'OI': 172, 'CHANGEINOI': -61, 'LTP': 6.15, 'trendschangeOI': [-61, -61],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24500: {
                     'CE': {'OI': 5363, 'CHANGEINOI': 949, 'LTP': 5.8, 'trendschangeOI': [949, 945],
                            'trends': [-4, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0],
                            'trends': [0, 0, 0, 0, 0]}}}],
                [{'index': 'NIFTY', 'marketstatus': True, 'TIME': '13:10:26', 'DATE': '12-Jun-2020', 'PRICE': 9752.85,
                  'turnoverPRICE': 9750, 7300: {'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                                                       'trends': [0, 0, 0, 0, 0]},
                                                'PE': {'OI': 75, 'CHANGEINOI': 49, 'LTP': 0.65,
                                                       'trendschangeOI': [49, 53, 52], 'trends': [4, 3, 0, 0, 0]}},
                  7350: {'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                                'trends': [0, 0, 0, 0, 0]},
                         'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1.7, 'trendschangeOI': [1, 1, 1],
                                'trends': [0, 0, 0, 0, 0]}}, 7400: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1.15, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7450: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0.75, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7500: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 834, 'CHANGEINOI': 829, 'LTP': 1.3, 'trendschangeOI': [829, 830, 830],
                               'trends': [1, 1, 0, 0, 0]}}, 7550: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7600: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7650: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7700: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7750: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7800: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2.9, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7850: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 7900: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 14, 'CHANGEINOI': 14, 'LTP': 1.8, 'trendschangeOI': [14, 8, 8],
                               'trends': [-6, -6, 0, 0, 0]}}, 7950: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8000: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3634, 'CHANGEINOI': 1741, 'LTP': 1.95, 'trendschangeOI': [1741, 1760, 1781],
                               'trends': [19, 40, 0, 0, 0]}}, 8050: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8100: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8150: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8200: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8250: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8300: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 302, 'CHANGEINOI': 302, 'LTP': 3, 'trendschangeOI': [302, 303, 306],
                               'trends': [1, 4, 0, 0, 0]}}, 8350: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8400: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 739, 'CHANGEINOI': 737, 'LTP': 4, 'trendschangeOI': [737, 735, 734],
                               'trends': [-2, -3, 0, 0, 0]}}, 8450: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8500: {
                        'CE': {'OI': 7, 'CHANGEINOI': 1, 'LTP': 1224.95, 'trendschangeOI': [1, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 7708, 'CHANGEINOI': 3782, 'LTP': 5.05, 'trendschangeOI': [3782, 3750, 3755],
                               'trends': [-32, -27, 0, 0, 0]}}, 8550: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8600: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3062, 'CHANGEINOI': 2997, 'LTP': 6.55, 'trendschangeOI': [2997, 3107, 3121],
                               'trends': [110, 124, 0, 0, 0]}}, 8650: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8700: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1000, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 4355, 'CHANGEINOI': 3973, 'LTP': 8.6, 'trendschangeOI': [3973, 4026, 3881],
                               'trends': [53, -92, 0, 0, 0]}}, 8750: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 8800: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 4908, 'CHANGEINOI': 3535, 'LTP': 11.4, 'trendschangeOI': [3535, 3511, 3585],
                               'trends': [-24, 50, 0, 0, 0]}}, 8850: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 25, 'CHANGEINOI': 22, 'LTP': 13.2, 'trendschangeOI': [22, 22, 23],
                               'trends': [0, 1, 0, 0, 0]}}, 8900: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 3872, 'CHANGEINOI': 2553, 'LTP': 15.1, 'trendschangeOI': [2553, 2555, 2560],
                               'trends': [2, 7, 0, 0, 0]}}, 8950: {
                        'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 419, 'CHANGEINOI': 411, 'LTP': 17.5, 'trendschangeOI': [411, 396, 398],
                               'trends': [-15, -13, 0, 0, 0]}}, 9000: {
                        'CE': {'OI': 212, 'CHANGEINOI': 187, 'LTP': 749, 'trendschangeOI': [187, 183, 183],
                               'trends': [-4, -4, 0, 0, 0]},
                        'PE': {'OI': 25340, 'CHANGEINOI': 11515, 'LTP': 20.05, 'trendschangeOI': [11515, 11047, 11132],
                               'trends': [-468, -383, 0, 0, 0]}}, 9050: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 645.4, 'trendschangeOI': [1, 1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 819, 'CHANGEINOI': 786, 'LTP': 23.4, 'trendschangeOI': [786, 795, 794],
                               'trends': [9, 8, 0, 0, 0]}}, 9100: {
                        'CE': {'OI': 88, 'CHANGEINOI': 1, 'LTP': 693.9, 'trendschangeOI': [1, 1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 7985, 'CHANGEINOI': 4302, 'LTP': 27.25, 'trendschangeOI': [4302, 4385, 4383],
                               'trends': [83, 81, 0, 0, 0]}}, 9150: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 648.8, 'trendschangeOI': [1, 1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1009, 'CHANGEINOI': 949, 'LTP': 31.35, 'trendschangeOI': [949, 928, 927],
                               'trends': [-21, -22, 0, 0, 0]}}, 9200: {
                        'CE': {'OI': 68, 'CHANGEINOI': 45, 'LTP': 548.6, 'trendschangeOI': [45, 45, 45],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 13295, 'CHANGEINOI': 7732, 'LTP': 36.4, 'trendschangeOI': [7732, 7768, 7697],
                               'trends': [36, -35, 0, 0, 0]}}, 9250: {
                        'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 540.7, 'trendschangeOI': [1, 1, 1],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1315, 'CHANGEINOI': 872, 'LTP': 42.15, 'trendschangeOI': [872, 888, 876],
                               'trends': [16, 4, 0, 0, 0]}}, 9300: {
                        'CE': {'OI': 435, 'CHANGEINOI': -17, 'LTP': 498.45, 'trendschangeOI': [-17, -17, -17],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 19680, 'CHANGEINOI': 11593, 'LTP': 49.1, 'trendschangeOI': [11593, 11370, 11672],
                               'trends': [-223, 79, 0, 0, 0]}}, 9350: {
                        'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 420.3, 'trendschangeOI': [5, 5, 5],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1699, 'CHANGEINOI': 1419, 'LTP': 56.3, 'trendschangeOI': [1419, 1423, 1401],
                               'trends': [4, -18, 0, 0, 0]}}, 9400: {
                        'CE': {'OI': 464, 'CHANGEINOI': 310, 'LTP': 399, 'trendschangeOI': [310, 320, 321],
                               'trends': [10, 11, 0, 0, 0]},
                        'PE': {'OI': 19422, 'CHANGEINOI': 12233, 'LTP': 65.25, 'trendschangeOI': [12233, 12195, 12041],
                               'trends': [-38, -192, 0, 0, 0]}}, 9450: {
                        'CE': {'OI': 38, 'CHANGEINOI': 37, 'LTP': 359.5, 'trendschangeOI': [37, 37, 37],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 1719, 'CHANGEINOI': 1128, 'LTP': 75, 'trendschangeOI': [1128, 1096, 1137],
                               'trends': [-32, 9, 0, 0, 0]}}, 9500: {
                        'CE': {'OI': 3015, 'CHANGEINOI': 1684, 'LTP': 320.05, 'trendschangeOI': [1684, 1710, 1764],
                               'trends': [26, 80, 0, 0, 0]},
                        'PE': {'OI': 27404, 'CHANGEINOI': 11101, 'LTP': 86.2, 'trendschangeOI': [11101, 11157, 10920],
                               'trends': [56, -181, 0, 0, 0]}}, 9550: {
                        'CE': {'OI': 127, 'CHANGEINOI': 124, 'LTP': 284.3, 'trendschangeOI': [124, 131, 155],
                               'trends': [7, 31, 0, 0, 0]},
                        'PE': {'OI': 2053, 'CHANGEINOI': 1614, 'LTP': 99.9, 'trendschangeOI': [1614, 1565, 1622],
                               'trends': [-49, 8, 0, 0, 0]}}, 9600: {
                        'CE': {'OI': 4817, 'CHANGEINOI': 4501, 'LTP': 248.2, 'trendschangeOI': [4501, 4593, 4638],
                               'trends': [92, 137, 0, 0, 0]},
                        'PE': {'OI': 20040, 'CHANGEINOI': 10836, 'LTP': 114.2, 'trendschangeOI': [10836, 10785, 10739],
                               'trends': [-51, -97, 0, 0, 0]}}, 9650: {
                        'CE': {'OI': 1008, 'CHANGEINOI': 1003, 'LTP': 214.3, 'trendschangeOI': [1003, 1000, 1026],
                               'trends': [-3, 23, 0, 0, 0]},
                        'PE': {'OI': 2597, 'CHANGEINOI': 1866, 'LTP': 131.25, 'trendschangeOI': [1866, 2005, 1985],
                               'trends': [139, 119, 0, 0, 0]}}, 9700: {
                        'CE': {'OI': 12059, 'CHANGEINOI': 11288, 'LTP': 184.15, 'trendschangeOI': [11288, 11305, 11421],
                               'trends': [17, 133, 0, 0, 0]},
                        'PE': {'OI': 18991, 'CHANGEINOI': 9498, 'LTP': 150.5, 'trendschangeOI': [9498, 9452, 9555],
                               'trends': [-46, 57, 0, 0, 0]}}, 9750: {
                        'CE': {'OI': 2168, 'CHANGEINOI': 2164, 'LTP': 156.35, 'trendschangeOI': [2164, 2202, 2108],
                               'trends': [38, -56, 0, 0, 0]},
                        'PE': {'OI': 2339, 'CHANGEINOI': 1059, 'LTP': 172, 'trendschangeOI': [1059, 994, 847],
                               'trends': [-65, -212, 0, 0, 0]}}, 9800: {
                        'CE': {'OI': 17414, 'CHANGEINOI': 14054, 'LTP': 131.2, 'trendschangeOI': [14054, 14114, 14332],
                               'trends': [60, 278, 0, 0, 0]},
                        'PE': {'OI': 9261, 'CHANGEINOI': -1546, 'LTP': 197.05, 'trendschangeOI': [-1546, -1610, -1580],
                               'trends': [-64, -34, 0, 0, 0]}}, 9850: {
                        'CE': {'OI': 1309, 'CHANGEINOI': 1205, 'LTP': 108.65, 'trendschangeOI': [1205, 1197, 1225],
                               'trends': [-8, 20, 0, 0, 0]},
                        'PE': {'OI': 902, 'CHANGEINOI': -4, 'LTP': 224.5, 'trendschangeOI': [-4, 0, 29],
                               'trends': [3, 33, 0, 0, 0]}}, 9900: {
                        'CE': {'OI': 22177, 'CHANGEINOI': 13814, 'LTP': 88.35, 'trendschangeOI': [13814, 14029, 14108],
                               'trends': [215, 294, 0, 0, 0]},
                        'PE': {'OI': 6410, 'CHANGEINOI': -3745, 'LTP': 253.5, 'trendschangeOI': [-3745, -3774, -3808],
                               'trends': [-29, -63, 0, 0, 0]}}, 9950: {
                        'CE': {'OI': 2199, 'CHANGEINOI': 1344, 'LTP': 71.5, 'trendschangeOI': [1344, 1428, 1476],
                               'trends': [84, 132, 0, 0, 0]},
                        'PE': {'OI': 473, 'CHANGEINOI': -274, 'LTP': 290.75, 'trendschangeOI': [-274, -269, -268],
                               'trends': [5, 6, 0, 0, 0]}}, 10000: {
                        'CE': {'OI': 27314, 'CHANGEINOI': 13989, 'LTP': 56.8, 'trendschangeOI': [13989, 13998, 14047],
                               'trends': [9, 58, 0, 0, 0]},
                        'PE': {'OI': 7214, 'CHANGEINOI': -727, 'LTP': 320.65, 'trendschangeOI': [-727, -686, -652],
                               'trends': [41, 75, 0, 0, 0]}}, 10050: {
                        'CE': {'OI': 3278, 'CHANGEINOI': 1467, 'LTP': 44.55, 'trendschangeOI': [1467, 1394, 1442],
                               'trends': [-73, -25, 0, 0, 0]},
                        'PE': {'OI': 668, 'CHANGEINOI': -55, 'LTP': 365.75, 'trendschangeOI': [-55, -60, -59],
                               'trends': [-5, -4, 0, 0, 0]}}, 10100: {
                        'CE': {'OI': 16946, 'CHANGEINOI': 2840, 'LTP': 34.8, 'trendschangeOI': [2840, 2804, 2777],
                               'trends': [-36, -63, 0, 0, 0]},
                        'PE': {'OI': 4055, 'CHANGEINOI': -355, 'LTP': 398.85, 'trendschangeOI': [-355, -369, -379],
                               'trends': [-14, -24, 0, 0, 0]}}, 10150: {
                        'CE': {'OI': 4860, 'CHANGEINOI': 3113, 'LTP': 26.85, 'trendschangeOI': [3113, 2948, 2969],
                               'trends': [-165, -144, 0, 0, 0]},
                        'PE': {'OI': 181, 'CHANGEINOI': -38, 'LTP': 427.1, 'trendschangeOI': [-38, -38, -38],
                               'trends': [0, 0, 0, 0, 0]}}, 10200: {
                        'CE': {'OI': 16714, 'CHANGEINOI': 2769, 'LTP': 21.25, 'trendschangeOI': [2769, 2720, 2780],
                               'trends': [-49, 11, 0, 0, 0]},
                        'PE': {'OI': 1029, 'CHANGEINOI': -210, 'LTP': 488.85, 'trendschangeOI': [-210, -212, -212],
                               'trends': [-2, -2, 0, 0, 0]}}, 10250: {
                        'CE': {'OI': 2153, 'CHANGEINOI': 679, 'LTP': 16.6, 'trendschangeOI': [679, 620, 578],
                               'trends': [-59, -101, 0, 0, 0]},
                        'PE': {'OI': 93, 'CHANGEINOI': -17, 'LTP': 505.85, 'trendschangeOI': [-17, -17, -17],
                               'trends': [0, 0, 0, 0, 0]}}, 10300: {
                        'CE': {'OI': 18281, 'CHANGEINOI': 4215, 'LTP': 13.3, 'trendschangeOI': [4215, 4116, 4187],
                               'trends': [-99, -28, 0, 0, 0]},
                        'PE': {'OI': 894, 'CHANGEINOI': -245, 'LTP': 583.9, 'trendschangeOI': [-245, -246, -246],
                               'trends': [0, 0, 0, 0, 0]}}, 10350: {
                        'CE': {'OI': 1447, 'CHANGEINOI': 330, 'LTP': 10.75, 'trendschangeOI': [330, 285, 296],
                               'trends': [-45, -34, 0, 0, 0]},
                        'PE': {'OI': 31, 'CHANGEINOI': 00, 'LTP': 614, 'trendschangeOI': [00, 00, 00],
                               'trends': [0, 0, 0, 0, 0]}}, 10400: {
                        'CE': {'OI': 13621, 'CHANGEINOI': 2111, 'LTP': 9, 'trendschangeOI': [2111, 1963, 2002],
                               'trends': [-148, -109, 0, 0, 0]},
                        'PE': {'OI': 165, 'CHANGEINOI': -13, 'LTP': 686.55, 'trendschangeOI': [-13, -13, -14],
                               'trends': [0, 0, 0, 0, 0]}}, 10450: {
                        'CE': {'OI': 811, 'CHANGEINOI': 27, 'LTP': 7.6, 'trendschangeOI': [27, 25, 1],
                               'trends': [-2, -26, 0, 0, 0]},
                        'PE': {'OI': 7, 'CHANGEINOI': 0, 'LTP': 732.7, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10500: {
                        'CE': {'OI': 26433, 'CHANGEINOI': 7507, 'LTP': 6.4, 'trendschangeOI': [7507, 7426, 7328],
                               'trends': [-81, -179, 0, 0, 0]},
                        'PE': {'OI': 647, 'CHANGEINOI': -3, 'LTP': 749.5, 'trendschangeOI': [-3, -3, -3],
                               'trends': [0, 0, 0, 0, 0]}}, 10550: {
                        'CE': {'OI': 805, 'CHANGEINOI': 16, 'LTP': 5.45, 'trendschangeOI': [16, 29, 17],
                               'trends': [13, 1, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10600: {
                        'CE': {'OI': 11641, 'CHANGEINOI': 2110, 'LTP': 4.45, 'trendschangeOI': [2110, 2072, 2005],
                               'trends': [-38, -105, 0, 0, 0]},
                        'PE': {'OI': 49, 'CHANGEINOI': 0, 'LTP': 889.45, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10650: {
                        'CE': {'OI': 812, 'CHANGEINOI': 391, 'LTP': 3.95, 'trendschangeOI': [391, 391, 404],
                               'trends': [0, 13, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10700: {
                        'CE': {'OI': 7777, 'CHANGEINOI': 32, 'LTP': 3.1, 'trendschangeOI': [32, 46, 97],
                               'trends': [14, 65, 0, 0, 0]},
                        'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 934.65, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10750: {
                        'CE': {'OI': 435, 'CHANGEINOI': 19, 'LTP': 2.8, 'trendschangeOI': [19, 17, 16],
                               'trends': [-2, -3, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10800: {
                        'CE': {'OI': 5121, 'CHANGEINOI': -945, 'LTP': 2.2, 'trendschangeOI': [-945, -951, -1010],
                               'trends': [-6, -65, 0, 0, 0]},
                        'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 1110.4, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10850: {
                        'CE': {'OI': 103, 'CHANGEINOI': 26, 'LTP': 1.8, 'trendschangeOI': [26, 27, 27],
                               'trends': [1, 1, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10900: {
                        'CE': {'OI': 2331, 'CHANGEINOI': -349, 'LTP': 1.65, 'trendschangeOI': [-349, -386, -419],
                               'trends': [-37, -70, 0, 0, 0]},
                        'PE': {'OI': 1, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 10950: {
                        'CE': {'OI': 145, 'CHANGEINOI': 103, 'LTP': 1.5, 'trendschangeOI': [103, 102, 102],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11000: {
                        'CE': {'OI': 12907, 'CHANGEINOI': -158, 'LTP': 1.4, 'trendschangeOI': [-158, -290, -460],
                               'trends': [-132, -302, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11050: {
                        'CE': {'OI': 71, 'CHANGEINOI': 21, 'LTP': 1.5, 'trendschangeOI': [21, 21, 21],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11100: {
                        'CE': {'OI': 658, 'CHANGEINOI': -242, 'LTP': 1.2, 'trendschangeOI': [-242, -243, -244],
                               'trends': [0, -2, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11150: {
                        'CE': {'OI': 49, 'CHANGEINOI': 7, 'LTP': 1.1, 'trendschangeOI': [7, 7, 7],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11200: {
                        'CE': {'OI': 1752, 'CHANGEINOI': 129, 'LTP': 0.9, 'trendschangeOI': [129, 126, 111],
                               'trends': [-3, -18, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11250: {
                        'CE': {'OI': 16, 'CHANGEINOI': 14, 'LTP': 1, 'trendschangeOI': [14, 14, 14],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11300: {
                        'CE': {'OI': 179, 'CHANGEINOI': -8, 'LTP': 0.9, 'trendschangeOI': [-8, -8, -8],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 2, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11350: {
                        'CE': {'OI': 7, 'CHANGEINOI': 5, 'LTP': 1.1, 'trendschangeOI': [5, 5, 5],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11400: {
                        'CE': {'OI': 101, 'CHANGEINOI': 7, 'LTP': 0.8, 'trendschangeOI': [7, 7, 7],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11450: {
                        'CE': {'OI': 34, 'CHANGEINOI': 4, 'LTP': 0.75, 'trendschangeOI': [4, 4, 4],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11500: {
                        'CE': {'OI': 2637, 'CHANGEINOI': 407, 'LTP': 0.7, 'trendschangeOI': [407, 367, 367],
                               'trends': [-40, -40, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11550: {
                        'CE': {'OI': 4, 'CHANGEINOI': 3, 'LTP': 0.5, 'trendschangeOI': [3, 3, 3],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11600: {
                        'CE': {'OI': 41, 'CHANGEINOI': 17, 'LTP': 0.6, 'trendschangeOI': [17, 17, 15],
                               'trends': [0, -2, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}, 11650: {
                        'CE': {'OI': 162, 'CHANGEINOI': 108, 'LTP': 0.7, 'trendschangeOI': [108, 108, 108],
                               'trends': [0, 0, 0, 0, 0]},
                        'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                               'trends': [0, 0, 0, 0, 0]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'TIME': '13:09:56', 'DATE': '12-Jun-2020',
                  'PRICE': 19986.45, 'turnoverPRICE': 19950, 14300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2587, 'CHANGEINOI': 2506, 'LTP': 6.35, 'trendschangeOI': [2506, 2500, 2484],
                            'trends': [-6, -22, 0, 0, 0]}}, 14400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 3.05, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]}}, 14600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 14900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 408, 'CHANGEINOI': 408, 'LTP': 7.95, 'trendschangeOI': [408, 424, 430],
                            'trends': [16, 22, 0, 0, 0]}}, 15100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 9, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 875, 'CHANGEINOI': 875, 'LTP': 10.6, 'trendschangeOI': [875, 928, 946],
                            'trends': [53, 71, 0, 0, 0]}}, 15600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 15900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16000: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 4197.3, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 7326, 'CHANGEINOI': 6173, 'LTP': 15.65, 'trendschangeOI': [6173, 6123, 6079],
                            'trends': [-50, -94, 0, 0, 0]}}, 16100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 13, 'CHANGEINOI': 13, 'LTP': 19, 'trendschangeOI': [13, 13, 13],
                            'trends': [0, 0, 0, 0, 0]}}, 16300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16500: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3384.9, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4731, 'CHANGEINOI': 4029, 'LTP': 24.8, 'trendschangeOI': [4029, 3973, 3890],
                            'trends': [-56, -139, 0, 0, 0]}}, 16600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 26, 'CHANGEINOI': 26, 'LTP': 29.6, 'trendschangeOI': [26, 25, 25],
                            'trends': [0, 0, 0, 0, 0]}}, 16800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 16900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 45, 'CHANGEINOI': 45, 'LTP': 37, 'trendschangeOI': [45, 45, 45],
                            'trends': [0, 0, 0, 0, 0]}}, 17000: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 3200, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 9849, 'CHANGEINOI': 8015, 'LTP': 40.8, 'trendschangeOI': [8015, 7913, 7823],
                            'trends': [-102, -192, 0, 0, 0]}}, 17100: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': 25, 'LTP': 43.7, 'trendschangeOI': [25, 25, 25],
                            'trends': [0, 0, 0, 0, 0]}}, 17200: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 78, 'CHANGEINOI': 78, 'LTP': 50.5, 'trendschangeOI': [78, 71, 70],
                            'trends': [-7, -8, 0, 0, 0]}}, 17300: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 11, 'CHANGEINOI': 11, 'LTP': 56.1, 'trendschangeOI': [11, 18, 18],
                            'trends': [7, 7, 0, 0, 0]}}, 17400: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 302, 'CHANGEINOI': 292, 'LTP': 61.95, 'trendschangeOI': [292, 275, 276],
                            'trends': [-17, -16, 0, 0, 0]}}, 17500: {
                     'CE': {'OI': 5, 'CHANGEINOI': 2, 'LTP': 2350.35, 'trendschangeOI': [2, 2, 2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 10525, 'CHANGEINOI': 8935, 'LTP': 66.8, 'trendschangeOI': [8935, 9009, 8928],
                            'trends': [74, -7, 0, 0, 0]}}, 17600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 277, 'CHANGEINOI': 277, 'LTP': 73.4, 'trendschangeOI': [277, 285, 295],
                            'trends': [8, 18, 0, 0, 0]}}, 17700: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 2266.3, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 721, 'CHANGEINOI': 669, 'LTP': 80.6, 'trendschangeOI': [669, 662, 674],
                            'trends': [-7, 5, 0, 0, 0]}}, 17800: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1748, 'CHANGEINOI': 1645, 'LTP': 89.65, 'trendschangeOI': [1645, 1646, 1607],
                            'trends': [1, -38, 0, 0, 0]}}, 17900: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 323, 'CHANGEINOI': 323, 'LTP': 98, 'trendschangeOI': [323, 297, 310],
                            'trends': [-26, -13, 0, 0, 0]}}, 18000: {
                     'CE': {'OI': 79, 'CHANGEINOI': 22, 'LTP': 2150, 'trendschangeOI': [22, 22, 21],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 17309, 'CHANGEINOI': 11386, 'LTP': 108.9, 'trendschangeOI': [11386, 11393, 11320],
                            'trends': [7, -66, 0, 0, 0]}}, 18100: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 2217.05, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1425, 'CHANGEINOI': 1224, 'LTP': 118.35, 'trendschangeOI': [1224, 1139, 1128],
                            'trends': [-85, -96, 0, 0, 0]}}, 18200: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1824, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1981, 'CHANGEINOI': 1884, 'LTP': 131.5, 'trendschangeOI': [1884, 1876, 1794],
                            'trends': [-8, -90, 0, 0, 0]}}, 18300: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1620.9, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 852, 'CHANGEINOI': 838, 'LTP': 144.4, 'trendschangeOI': [838, 851, 882],
                            'trends': [13, 44, 0, 0, 0]}}, 18400: {
                     'CE': {'OI': 11, 'CHANGEINOI': 11, 'LTP': 1779.75, 'trendschangeOI': [11, 11, 11],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1717, 'CHANGEINOI': 1643, 'LTP': 156.9, 'trendschangeOI': [1643, 1615, 1618],
                            'trends': [-28, -25, 0, 0, 0]}}, 18500: {
                     'CE': {'OI': 154, 'CHANGEINOI': 67, 'LTP': 1636.25, 'trendschangeOI': [67, 67, 67],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 15930, 'CHANGEINOI': 10129, 'LTP': 171.15, 'trendschangeOI': [10129, 10018, 9688],
                            'trends': [-111, -441, 0, 0, 0]}}, 18600: {
                     'CE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 1663.4, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1370, 'CHANGEINOI': 1280, 'LTP': 190.1, 'trendschangeOI': [1280, 1242, 1233],
                            'trends': [-38, -47, 0, 0, 0]}}, 18700: {
                     'CE': {'OI': 2, 'CHANGEINOI': 2, 'LTP': 1534.45, 'trendschangeOI': [2, 2, 2],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1353, 'CHANGEINOI': 1117, 'LTP': 208.3, 'trendschangeOI': [1117, 1109, 1110],
                            'trends': [-8, -7, 0, 0, 0]}}, 18800: {
                     'CE': {'OI': 5, 'CHANGEINOI': 5, 'LTP': 1558.95, 'trendschangeOI': [5, 5, 5],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 2294, 'CHANGEINOI': 1837, 'LTP': 228.9, 'trendschangeOI': [1837, 1906, 1868],
                            'trends': [69, 31, 0, 0, 0]}}, 18900: {
                     'CE': {'OI': 1, 'CHANGEINOI': 1, 'LTP': 1250, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1638, 'CHANGEINOI': 1358, 'LTP': 250.3, 'trendschangeOI': [1358, 1319, 1301],
                            'trends': [-39, -57, 0, 0, 0]}}, 19000: {
                     'CE': {'OI': 973, 'CHANGEINOI': 731, 'LTP': 1225, 'trendschangeOI': [731, 735, 747],
                            'trends': [4, 16, 0, 0, 0]},
                     'PE': {'OI': 24767, 'CHANGEINOI': 12674, 'LTP': 275, 'trendschangeOI': [12674, 12878, 12026],
                            'trends': [204, -648, 0, 0, 0]}}, 19100: {
                     'CE': {'OI': 9, 'CHANGEINOI': 9, 'LTP': 1355.8, 'trendschangeOI': [9, 9, 9],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 1713, 'CHANGEINOI': 1604, 'LTP': 301, 'trendschangeOI': [1604, 1655, 1615],
                            'trends': [51, 11, 0, 0, 0]}}, 19200: {
                     'CE': {'OI': 34, 'CHANGEINOI': 34, 'LTP': 1140.8, 'trendschangeOI': [34, 34, 34],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 4602, 'CHANGEINOI': 4436, 'LTP': 329.15, 'trendschangeOI': [4436, 4593, 4520],
                            'trends': [157, 84, 0, 0, 0]}}, 19300: {
                     'CE': {'OI': 37, 'CHANGEINOI': 37, 'LTP': 1020, 'trendschangeOI': [37, 38, 38],
                            'trends': [1, 1, 0, 0, 0]},
                     'PE': {'OI': 3670, 'CHANGEINOI': 3302, 'LTP': 358, 'trendschangeOI': [3302, 3278, 3231],
                            'trends': [-24, -71, 0, 0, 0]}}, 19400: {
                     'CE': {'OI': 52, 'CHANGEINOI': 52, 'LTP': 945, 'trendschangeOI': [52, 46, 56],
                            'trends': [-6, 4, 0, 0, 0]},
                     'PE': {'OI': 2174, 'CHANGEINOI': 1666, 'LTP': 391.85, 'trendschangeOI': [1666, 1499, 1468],
                            'trends': [-167, -198, 0, 0, 0]}}, 19500: {
                     'CE': {'OI': 3478, 'CHANGEINOI': 3266, 'LTP': 897.65, 'trendschangeOI': [3266, 3241, 3245],
                            'trends': [-25, -21, 0, 0, 0]},
                     'PE': {'OI': 16422, 'CHANGEINOI': 2624, 'LTP': 425.95, 'trendschangeOI': [2624, 2953, 2830],
                            'trends': [329, 206, 0, 0, 0]}}, 19600: {
                     'CE': {'OI': 465, 'CHANGEINOI': 464, 'LTP': 828.85, 'trendschangeOI': [464, 484, 463],
                            'trends': [20, 0, 0, 0, 0]},
                     'PE': {'OI': 2281, 'CHANGEINOI': 2093, 'LTP': 463.55, 'trendschangeOI': [2093, 2099, 2103],
                            'trends': [6, 10, 0, 0, 0]}}, 19700: {
                     'CE': {'OI': 1278, 'CHANGEINOI': 1278, 'LTP': 771.4, 'trendschangeOI': [1278, 1303, 1320],
                            'trends': [25, 42, 0, 0, 0]},
                     'PE': {'OI': 4306, 'CHANGEINOI': 3712, 'LTP': 500, 'trendschangeOI': [3712, 3680, 3603],
                            'trends': [-32, -109, 0, 0, 0]}}, 19800: {
                     'CE': {'OI': 2142, 'CHANGEINOI': 2141, 'LTP': 713.05, 'trendschangeOI': [2141, 2151, 2250],
                            'trends': [10, 109, 0, 0, 0]},
                     'PE': {'OI': 4233, 'CHANGEINOI': 3760, 'LTP': 545.1, 'trendschangeOI': [3760, 3784, 3618],
                            'trends': [24, -142, 0, 0, 0]}}, 19900: {
                     'CE': {'OI': 1712, 'CHANGEINOI': 1710, 'LTP': 660, 'trendschangeOI': [1710, 1654, 1730],
                            'trends': [-56, 20, 0, 0, 0]},
                     'PE': {'OI': 3094, 'CHANGEINOI': 2769, 'LTP': 590.75, 'trendschangeOI': [2769, 3261, 3188],
                            'trends': [492, 419, 0, 0, 0]}}, 20000: {
                     'CE': {'OI': 10939, 'CHANGEINOI': 9374, 'LTP': 605, 'trendschangeOI': [9374, 9278, 9218],
                            'trends': [-96, -156, 0, 0, 0]},
                     'PE': {'OI': 12011, 'CHANGEINOI': 1890, 'LTP': 634.6, 'trendschangeOI': [1890, 2022, 1652],
                            'trends': [132, -238, 0, 0, 0]}}, 20100: {
                     'CE': {'OI': 1551, 'CHANGEINOI': 1551, 'LTP': 557.95, 'trendschangeOI': [1551, 1696, 1596],
                            'trends': [145, 45, 0, 0, 0]},
                     'PE': {'OI': 1181, 'CHANGEINOI': 760, 'LTP': 684.9, 'trendschangeOI': [760, 708, 637],
                            'trends': [-52, -123, 0, 0, 0]}}, 20200: {
                     'CE': {'OI': 2535, 'CHANGEINOI': 2503, 'LTP': 513.35, 'trendschangeOI': [2503, 2566, 2543],
                            'trends': [63, 40, 0, 0, 0]},
                     'PE': {'OI': 888, 'CHANGEINOI': -24, 'LTP': 739.65, 'trendschangeOI': [-24, -11, -8],
                            'trends': [13, 16, 0, 0, 0]}}, 20300: {
                     'CE': {'OI': 1819, 'CHANGEINOI': 1744, 'LTP': 467.6, 'trendschangeOI': [1744, 1722, 1584],
                            'trends': [-22, -160, 0, 0, 0]},
                     'PE': {'OI': 581, 'CHANGEINOI': -393, 'LTP': 804.1, 'trendschangeOI': [-393, -393, -379],
                            'trends': [0, 14, 0, 0, 0]}}, 20400: {
                     'CE': {'OI': 2021, 'CHANGEINOI': 1895, 'LTP': 425.8, 'trendschangeOI': [1895, 1907, 2044],
                            'trends': [12, 149, 0, 0, 0]},
                     'PE': {'OI': 728, 'CHANGEINOI': -11, 'LTP': 841.55, 'trendschangeOI': [-11, -12, -12],
                            'trends': [0, 0, 0, 0, 0]}}, 20500: {
                     'CE': {'OI': 10817, 'CHANGEINOI': 6714, 'LTP': 384.3, 'trendschangeOI': [6714, 6925, 6640],
                            'trends': [211, -74, 0, 0, 0]},
                     'PE': {'OI': 4355, 'CHANGEINOI': -1509, 'LTP': 912, 'trendschangeOI': [-1509, -1491, -1548],
                            'trends': [18, -39, 0, 0, 0]}}, 20600: {
                     'CE': {'OI': 2188, 'CHANGEINOI': 1244, 'LTP': 346.9, 'trendschangeOI': [1244, 1197, 1281],
                            'trends': [-47, 37, 0, 0, 0]},
                     'PE': {'OI': 427, 'CHANGEINOI': -86, 'LTP': 999.7, 'trendschangeOI': [-86, -89, -162],
                            'trends': [-3, -76, 0, 0, 0]}}, 20700: {
                     'CE': {'OI': 2235, 'CHANGEINOI': 1382, 'LTP': 315.25, 'trendschangeOI': [1382, 1374, 1334],
                            'trends': [-8, -48, 0, 0, 0]},
                     'PE': {'OI': 368, 'CHANGEINOI': -42, 'LTP': 1036.25, 'trendschangeOI': [-42, -40, -40],
                            'trends': [2, 2, 0, 0, 0]}}, 20800: {
                     'CE': {'OI': 3650, 'CHANGEINOI': 2352, 'LTP': 284.25, 'trendschangeOI': [2352, 2350, 2308],
                            'trends': [-2, -44, 0, 0, 0]},
                     'PE': {'OI': 360, 'CHANGEINOI': -120, 'LTP': 1126.05, 'trendschangeOI': [-120, -115, -109],
                            'trends': [5, 11, 0, 0, 0]}}, 20900: {
                     'CE': {'OI': 1930, 'CHANGEINOI': 1418, 'LTP': 255.4, 'trendschangeOI': [1418, 1376, 1409],
                            'trends': [-42, -9, 0, 0, 0]},
                     'PE': {'OI': 236, 'CHANGEINOI': -48, 'LTP': 1208.35, 'trendschangeOI': [-48, -47, -45],
                            'trends': [1, 3, 0, 0, 0]}}, 21000: {
                     'CE': {'OI': 20807, 'CHANGEINOI': 9886, 'LTP': 230.6, 'trendschangeOI': [9886, 9973, 10221],
                            'trends': [87, 335, 0, 0, 0]},
                     'PE': {'OI': 3824, 'CHANGEINOI': -359, 'LTP': 1275.05, 'trendschangeOI': [-359, -360, -354],
                            'trends': [0, 5, 0, 0, 0]}}, 21100: {
                     'CE': {'OI': 2402, 'CHANGEINOI': 1592, 'LTP': 206.2, 'trendschangeOI': [1592, 1558, 1514],
                            'trends': [-34, -78, 0, 0, 0]},
                     'PE': {'OI': 353, 'CHANGEINOI': -20, 'LTP': 1291.2, 'trendschangeOI': [-20, -20, -20],
                            'trends': [0, 0, 0, 0, 0]}}, 21200: {
                     'CE': {'OI': 2708, 'CHANGEINOI': 1211, 'LTP': 185.25, 'trendschangeOI': [1211, 1228, 1453],
                            'trends': [17, 242, 0, 0, 0]},
                     'PE': {'OI': 155, 'CHANGEINOI': -19, 'LTP': 1510.2, 'trendschangeOI': [-19, -19, -19],
                            'trends': [0, 0, 0, 0, 0]}}, 21300: {
                     'CE': {'OI': 2487, 'CHANGEINOI': 1437, 'LTP': 164.5, 'trendschangeOI': [1437, 1475, 1510],
                            'trends': [38, 73, 0, 0, 0]},
                     'PE': {'OI': 87, 'CHANGEINOI': 0, 'LTP': 1498.5, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 21400: {
                     'CE': {'OI': 1575, 'CHANGEINOI': 695, 'LTP': 145.85, 'trendschangeOI': [695, 685, 677],
                            'trends': [00, -18, 0, 0, 0]},
                     'PE': {'OI': 25, 'CHANGEINOI': -2, 'LTP': 1308.6, 'trendschangeOI': [-2, -2, -2],
                            'trends': [0, 0, 0, 0, 0]}}, 21500: {
                     'CE': {'OI': 17202, 'CHANGEINOI': 5887, 'LTP': 129.95, 'trendschangeOI': [5887, 5697, 5571],
                            'trends': [-190, -316, 0, 0, 0]},
                     'PE': {'OI': 968, 'CHANGEINOI': -478, 'LTP': 1601.15, 'trendschangeOI': [-478, -478, -475],
                            'trends': [0, 3, 0, 0, 0]}}, 21600: {
                     'CE': {'OI': 1951, 'CHANGEINOI': 1257, 'LTP': 115.5, 'trendschangeOI': [1257, 1302, 1375],
                            'trends': [45, 118, 0, 0, 0]},
                     'PE': {'OI': 10, 'CHANGEINOI': 2, 'LTP': 1641.1, 'trendschangeOI': [2, 2, 2],
                            'trends': [0, 0, 0, 0, 0]}}, 21700: {
                     'CE': {'OI': 1964, 'CHANGEINOI': 1461, 'LTP': 101.8, 'trendschangeOI': [1461, 1395, 1402],
                            'trends': [-66, -59, 0, 0, 0]},
                     'PE': {'OI': 13, 'CHANGEINOI': 0, 'LTP': 1959.1, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 21800: {
                     'CE': {'OI': 4226, 'CHANGEINOI': 3053, 'LTP': 89.5, 'trendschangeOI': [3053, 3083, 3184],
                            'trends': [30, 131, 0, 0, 0]},
                     'PE': {'OI': 2, 'CHANGEINOI': 1, 'LTP': 2140.85, 'trendschangeOI': [1, 1, 1],
                            'trends': [0, 0, 0, 0, 0]}}, 21900: {
                     'CE': {'OI': 1410, 'CHANGEINOI': 997, 'LTP': 80.05, 'trendschangeOI': [997, 996, 957],
                            'trends': [0, -40, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22000: {
                     'CE': {'OI': 20172, 'CHANGEINOI': 9144, 'LTP': 71.7, 'trendschangeOI': [9144, 9052, 8904],
                            'trends': [-92, -240, 0, 0, 0]},
                     'PE': {'OI': 355, 'CHANGEINOI': -19, 'LTP': 2110.05, 'trendschangeOI': [-19, -19, -20],
                            'trends': [0, 0, 0, 0, 0]}}, 22100: {
                     'CE': {'OI': 816, 'CHANGEINOI': 548, 'LTP': 63.1, 'trendschangeOI': [548, 588, 639],
                            'trends': [40, 91, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22200: {
                     'CE': {'OI': 1182, 'CHANGEINOI': 682, 'LTP': 56, 'trendschangeOI': [682, 686, 710],
                            'trends': [4, 28, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22300: {
                     'CE': {'OI': 857, 'CHANGEINOI': 667, 'LTP': 49.25, 'trendschangeOI': [667, 615, 634],
                            'trends': [-52, -33, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22400: {
                     'CE': {'OI': 746, 'CHANGEINOI': 435, 'LTP': 43.65, 'trendschangeOI': [435, 484, 473],
                            'trends': [49, 38, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22500: {
                     'CE': {'OI': 12794, 'CHANGEINOI': 4713, 'LTP': 38.3, 'trendschangeOI': [4713, 4756, 4640],
                            'trends': [43, -73, 0, 0, 0]},
                     'PE': {'OI': 3, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22600: {
                     'CE': {'OI': 1100, 'CHANGEINOI': 457, 'LTP': 34.05, 'trendschangeOI': [457, 455, 445],
                            'trends': [-2, -12, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22700: {
                     'CE': {'OI': 704, 'CHANGEINOI': 508, 'LTP': 30, 'trendschangeOI': [508, 493, 485],
                            'trends': [-15, -23, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22800: {
                     'CE': {'OI': 741, 'CHANGEINOI': 450, 'LTP': 26.15, 'trendschangeOI': [450, 437, 435],
                            'trends': [-13, -15, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 22900: {
                     'CE': {'OI': 710, 'CHANGEINOI': 396, 'LTP': 22.65, 'trendschangeOI': [396, 374, 376],
                            'trends': [-22, -20, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23000: {
                     'CE': {'OI': 13058, 'CHANGEINOI': 2264, 'LTP': 19.9, 'trendschangeOI': [2264, 2249, 2525],
                            'trends': [-15, 261, 0, 0, 0]},
                     'PE': {'OI': 33, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23100: {
                     'CE': {'OI': 332, 'CHANGEINOI': 222, 'LTP': 18.1, 'trendschangeOI': [222, 241, 240],
                            'trends': [19, 18, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23200: {
                     'CE': {'OI': 737, 'CHANGEINOI': 140, 'LTP': 15.6, 'trendschangeOI': [140, 159, 157],
                            'trends': [19, 17, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23300: {
                     'CE': {'OI': 39, 'CHANGEINOI': 39, 'LTP': 14.1, 'trendschangeOI': [39, 22, 17],
                            'trends': [-17, -22, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23400: {
                     'CE': {'OI': 198, 'CHANGEINOI': 72, 'LTP': 12.75, 'trendschangeOI': [72, 67, 70],
                            'trends': [-5, -2, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23500: {
                     'CE': {'OI': 8800, 'CHANGEINOI': 2857, 'LTP': 10.7, 'trendschangeOI': [2857, 2870, 2758],
                            'trends': [13, -99, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23600: {
                     'CE': {'OI': 122, 'CHANGEINOI': 107, 'LTP': 11, 'trendschangeOI': [107, 106, 107],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23700: {
                     'CE': {'OI': 124, 'CHANGEINOI': 124, 'LTP': 11, 'trendschangeOI': [124, 124, 124],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23800: {
                     'CE': {'OI': 305, 'CHANGEINOI': 174, 'LTP': 8.7, 'trendschangeOI': [174, 176, 171],
                            'trends': [2, -3, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 23900: {
                     'CE': {'OI': 409, 'CHANGEINOI': 213, 'LTP': 9.4, 'trendschangeOI': [213, 213, 206],
                            'trends': [0, -7, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24000: {
                     'CE': {'OI': 5678, 'CHANGEINOI': 1311, 'LTP': 7, 'trendschangeOI': [1311, 1234, 1267],
                            'trends': [-77, -44, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24100: {
                     'CE': {'OI': 47, 'CHANGEINOI': 38, 'LTP': 6.3, 'trendschangeOI': [38, 38, 38],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24200: {
                     'CE': {'OI': 59, 'CHANGEINOI': 34, 'LTP': 6.2, 'trendschangeOI': [34, 34, 34],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24300: {
                     'CE': {'OI': 56, 'CHANGEINOI': 16, 'LTP': 6.65, 'trendschangeOI': [16, 16, 16],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24400: {
                     'CE': {'OI': 173, 'CHANGEINOI': -60, 'LTP': 6.7, 'trendschangeOI': [-60, -61, -61],
                            'trends': [0, 0, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}, 24500: {
                     'CE': {'OI': 5384, 'CHANGEINOI': 970, 'LTP': 5.55, 'trendschangeOI': [970, 949, 945],
                            'trends': [-21, -25, 0, 0, 0]},
                     'PE': {'OI': 0, 'CHANGEINOI': 0, 'LTP': 0, 'trendschangeOI': [0, 0, 0],
                            'trends': [0, 0, 0, 0, 0]}}}]]
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
    # testing end
