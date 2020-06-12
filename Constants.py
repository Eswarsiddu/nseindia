from typing import Tuple, Dict


class Constants:
    URLS: Tuple[str, str] = ('https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY',
                             'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY')
    NIFTY: int = 0
    BANK_NIFTY: int = 1
    STRIKE_PRICE: str = 'strikeprice'
    CALLS: str = 'CE'
    PUTS: str = 'PE'
    INDEX: str = "index"
    OI: str = "oi"
    CHANGE_IN_OI: str = "changeinoi"
    LTP: str = "ltp"
    TIME: str = "time"
    DATE: str = "date"
    PRICE: str = "price"
    TURNOVER_PRICE: str = "turnoverprice"
    MARKET_STATUS: str = "marketstatus"
    TRENDS: str = "trends"
    TREND_CHANGE_OF_OI: str = "trendschangeoi"

    # testing
    TESTING: bool = True
    Testing_index: int = -1
    testdata = [[{'index': 'NIFTY', 'marketstatus': True, 'time': '12:58:56', 'date': '12-Jun-2020', 'price': 9766.25,
                  'turnoverprice': 9750, 7300: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 78, 'changeinoi': 52, 'ltp': 0.8, 'trendschangeoi': [52], 'trends': [-1, -1, -1, -1, -1]}},
                  7350: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 1.7, 'trendschangeoi': [1],
                             'trends': [-1, -1, -1, -1, -1]}}, 7400: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 1.15, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  7450: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0.75, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 7500: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 835, 'changeinoi': 830, 'ltp': 1.15, 'trendschangeoi': [830], 'trends': [-1, -1, -1, -1, -1]}},
                  7550: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 7600: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 7650: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 7700: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 7750: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 7800: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 2.9, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  7850: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 7900: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 8, 'changeinoi': 8, 'ltp': 1.95, 'trendschangeoi': [8], 'trends': [-1, -1, -1, -1, -1]}},
                  7950: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 8000: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 3674, 'changeinoi': 1781, 'ltp': 1.9, 'trendschangeoi': [1781],
                   'trends': [-1, -1, -1, -1, -1]}}, 8050: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8100: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8150: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8200: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8250: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8300: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 306, 'changeinoi': 306, 'ltp': 3, 'trendschangeoi': [306], 'trends': [-1, -1, -1, -1, -1]}},
                  8350: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 8400: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 736, 'changeinoi': 734, 'ltp': 3.95, 'trendschangeoi': [734], 'trends': [-1, -1, -1, -1, -1]}},
                  8450: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 8500: {
            'CE': {'oi': 6, 'changeinoi': 0, 'ltp': 1210, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 7681, 'changeinoi': 3755, 'ltp': 4.95, 'trendschangeoi': [3755],
                   'trends': [-1, -1, -1, -1, -1]}}, 8550: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8600: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 3186, 'changeinoi': 3121, 'ltp': 6.35, 'trendschangeoi': [3121],
                   'trends': [-1, -1, -1, -1, -1]}}, 8650: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8700: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1000, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 4263, 'changeinoi': 3881, 'ltp': 8.35, 'trendschangeoi': [3881],
                   'trends': [-1, -1, -1, -1, -1]}}, 8750: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 8800: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 4958, 'changeinoi': 3585, 'ltp': 10.9, 'trendschangeoi': [3585],
                   'trends': [-1, -1, -1, -1, -1]}}, 8850: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 26, 'changeinoi': 23, 'ltp': 13.35, 'trendschangeoi': [23], 'trends': [-1, -1, -1, -1, -1]}},
                  8900: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 3879, 'changeinoi': 2560, 'ltp': 14.8, 'trendschangeoi': [2560],
                             'trends': [-1, -1, -1, -1, -1]}}, 8950: {
            'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 406, 'changeinoi': 398, 'ltp': 16.8, 'trendschangeoi': [398], 'trends': [-1, -1, -1, -1, -1]}},
                  9000: {'CE': {'oi': 208, 'changeinoi': 183, 'ltp': 762, 'trendschangeoi': [183],
                                'trends': [-1, -1, -1, -1, -1]},
                         'PE': {'oi': 24957, 'changeinoi': 11132, 'ltp': 19.7, 'trendschangeoi': [11132],
                                'trends': [-1, -1, -1, -1, -1]}}, 9050: {
            'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 645.4, 'trendschangeoi': [1], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 827, 'changeinoi': 794, 'ltp': 22.75, 'trendschangeoi': [794],
                   'trends': [-1, -1, -1, -1, -1]}}, 9100: {
            'CE': {'oi': 88, 'changeinoi': 1, 'ltp': 693.9, 'trendschangeoi': [1], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 8066, 'changeinoi': 4383, 'ltp': 26.4, 'trendschangeoi': [4383],
                   'trends': [-1, -1, -1, -1, -1]}}, 9150: {
            'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 648.8, 'trendschangeoi': [1], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 987, 'changeinoi': 927, 'ltp': 30.45, 'trendschangeoi': [927],
                   'trends': [-1, -1, -1, -1, -1]}}, 9200: {
            'CE': {'oi': 68, 'changeinoi': 45, 'ltp': 548.6, 'trendschangeoi': [45], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 13260, 'changeinoi': 7697, 'ltp': 35.5, 'trendschangeoi': [7697],
                   'trends': [-1, -1, -1, -1, -1]}}, 9250: {
            'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 540.7, 'trendschangeoi': [1], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1319, 'changeinoi': 876, 'ltp': 40.9, 'trendschangeoi': [876],
                   'trends': [-1, -1, -1, -1, -1]}}, 9300: {
            'CE': {'oi': 435, 'changeinoi': -17, 'ltp': 498.45, 'trendschangeoi': [-17],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 19759, 'changeinoi': 11672, 'ltp': 47.35, 'trendschangeoi': [11672],
                   'trends': [-1, -1, -1, -1, -1]}}, 9350: {
            'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 420.3, 'trendschangeoi': [5], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1681, 'changeinoi': 1401, 'ltp': 54.7, 'trendschangeoi': [1401],
                   'trends': [-1, -1, -1, -1, -1]}}, 9400: {
            'CE': {'oi': 475, 'changeinoi': 321, 'ltp': 403.05, 'trendschangeoi': [321],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 19230, 'changeinoi': 12041, 'ltp': 63.25, 'trendschangeoi': [12041],
                   'trends': [-1, -1, -1, -1, -1]}}, 9450: {
            'CE': {'oi': 38, 'changeinoi': 37, 'ltp': 356.1, 'trendschangeoi': [37], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1728, 'changeinoi': 1137, 'ltp': 72.45, 'trendschangeoi': [1137],
                   'trends': [-1, -1, -1, -1, -1]}}, 9500: {
            'CE': {'oi': 3095, 'changeinoi': 1764, 'ltp': 327.7, 'trendschangeoi': [1764],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 27223, 'changeinoi': 10920, 'ltp': 83.95, 'trendschangeoi': [10920],
                   'trends': [-1, -1, -1, -1, -1]}}, 9550: {
            'CE': {'oi': 158, 'changeinoi': 155, 'ltp': 290.8, 'trendschangeoi': [155], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 2061, 'changeinoi': 1622, 'ltp': 96.3, 'trendschangeoi': [1622],
                   'trends': [-1, -1, -1, -1, -1]}}, 9600: {
            'CE': {'oi': 4954, 'changeinoi': 4638, 'ltp': 254, 'trendschangeoi': [4638],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 19943, 'changeinoi': 10739, 'ltp': 111.3, 'trendschangeoi': [10739],
                   'trends': [-1, -1, -1, -1, -1]}}, 9650: {
            'CE': {'oi': 1031, 'changeinoi': 1026, 'ltp': 220.45, 'trendschangeoi': [1026],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 2716, 'changeinoi': 1985, 'ltp': 128, 'trendschangeoi': [1985],
                   'trends': [-1, -1, -1, -1, -1]}}, 9700: {
            'CE': {'oi': 12192, 'changeinoi': 11421, 'ltp': 189, 'trendschangeoi': [11421],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 19048, 'changeinoi': 9555, 'ltp': 146.55, 'trendschangeoi': [9555],
                   'trends': [-1, -1, -1, -1, -1]}}, 9750: {
            'CE': {'oi': 2112, 'changeinoi': 2108, 'ltp': 161, 'trendschangeoi': [2108],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 2127, 'changeinoi': 847, 'ltp': 167, 'trendschangeoi': [847], 'trends': [-1, -1, -1, -1, -1]}},
                  9800: {'CE': {'oi': 17692, 'changeinoi': 14332, 'ltp': 135.6, 'trendschangeoi': [14332],
                                'trends': [-1, -1, -1, -1, -1]},
                         'PE': {'oi': 9227, 'changeinoi': -1580, 'ltp': 191.9, 'trendschangeoi': [-1580],
                                'trends': [-1, -1, -1, -1, -1]}}, 9850: {
            'CE': {'oi': 1329, 'changeinoi': 1225, 'ltp': 112.4, 'trendschangeoi': [1225],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 935, 'changeinoi': 29, 'ltp': 220.55, 'trendschangeoi': [29], 'trends': [-1, -1, -1, -1, -1]}},
                  9900: {'CE': {'oi': 22471, 'changeinoi': 14108, 'ltp': 91.4, 'trendschangeoi': [14108],
                                'trends': [-1, -1, -1, -1, -1]},
                         'PE': {'oi': 6347, 'changeinoi': -3808, 'ltp': 247.15, 'trendschangeoi': [-3808],
                                'trends': [-1, -1, -1, -1, -1]}}, 9950: {
            'CE': {'oi': 2331, 'changeinoi': 1476, 'ltp': 74.9, 'trendschangeoi': [1476],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 479, 'changeinoi': -268, 'ltp': 279.4, 'trendschangeoi': [-268],
                   'trends': [-1, -1, -1, -1, -1]}}, 10000: {
            'CE': {'oi': 27372, 'changeinoi': 14047, 'ltp': 59.4, 'trendschangeoi': [14047],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 7289, 'changeinoi': -652, 'ltp': 316, 'trendschangeoi': [-652],
                   'trends': [-1, -1, -1, -1, -1]}}, 10050: {
            'CE': {'oi': 3253, 'changeinoi': 1442, 'ltp': 46.9, 'trendschangeoi': [1442],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 664, 'changeinoi': -59, 'ltp': 351.2, 'trendschangeoi': [-59],
                   'trends': [-1, -1, -1, -1, -1]}}, 10100: {
            'CE': {'oi': 16883, 'changeinoi': 2777, 'ltp': 36.45, 'trendschangeoi': [2777],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 4031, 'changeinoi': -379, 'ltp': 391.55, 'trendschangeoi': [-379],
                   'trends': [-1, -1, -1, -1, -1]}}, 10150: {
            'CE': {'oi': 4716, 'changeinoi': 2969, 'ltp': 28.4, 'trendschangeoi': [2969],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 181, 'changeinoi': -38, 'ltp': 427.1, 'trendschangeoi': [-38],
                   'trends': [-1, -1, -1, -1, -1]}}, 10200: {
            'CE': {'oi': 16725, 'changeinoi': 2780, 'ltp': 22.25, 'trendschangeoi': [2780],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1027, 'changeinoi': -212, 'ltp': 475.55, 'trendschangeoi': [-212],
                   'trends': [-1, -1, -1, -1, -1]}}, 10250: {
            'CE': {'oi': 2052, 'changeinoi': 578, 'ltp': 17.4, 'trendschangeoi': [578], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 93, 'changeinoi': -17, 'ltp': 505.85, 'trendschangeoi': [-17],
                   'trends': [-1, -1, -1, -1, -1]}}, 10300: {
            'CE': {'oi': 18253, 'changeinoi': 4187, 'ltp': 13.75, 'trendschangeoi': [4187],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 893, 'changeinoi': -246, 'ltp': 556.95, 'trendschangeoi': [-246],
                   'trends': [-1, -1, -1, -1, -1]}}, 10350: {
            'CE': {'oi': 1413, 'changeinoi': 296, 'ltp': 11.1, 'trendschangeoi': [296], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 31, 'changeinoi': -10, 'ltp': 614, 'trendschangeoi': [-10], 'trends': [-1, -1, -1, -1, -1]}},
                  10400: {'CE': {'oi': 13512, 'changeinoi': 2002, 'ltp': 9.25, 'trendschangeoi': [2002],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 164, 'changeinoi': -14, 'ltp': 656, 'trendschangeoi': [-14],
                                 'trends': [-1, -1, -1, -1, -1]}}, 10450: {
            'CE': {'oi': 785, 'changeinoi': 1, 'ltp': 7.7, 'trendschangeoi': [1], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 7, 'changeinoi': 0, 'ltp': 732.7, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  10500: {'CE': {'oi': 26254, 'changeinoi': 7328, 'ltp': 6.55, 'trendschangeoi': [7328],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 647, 'changeinoi': -3, 'ltp': 749.5, 'trendschangeoi': [-3],
                                 'trends': [-1, -1, -1, -1, -1]}}, 10550: {
            'CE': {'oi': 806, 'changeinoi': 17, 'ltp': 5.35, 'trendschangeoi': [17], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 10600: {
            'CE': {'oi': 11536, 'changeinoi': 2005, 'ltp': 4.65, 'trendschangeoi': [2005],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 49, 'changeinoi': -1, 'ltp': 889.45, 'trendschangeoi': [-1], 'trends': [-1, -1, -1, -1, -1]}},
                  10650: {'CE': {'oi': 825, 'changeinoi': 404, 'ltp': 4.2, 'trendschangeoi': [404],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 10700: {
            'CE': {'oi': 7842, 'changeinoi': 97, 'ltp': 3.25, 'trendschangeoi': [97], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 934.65, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  10750: {'CE': {'oi': 432, 'changeinoi': 16, 'ltp': 3, 'trendschangeoi': [16],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 10800: {
            'CE': {'oi': 5056, 'changeinoi': -1010, 'ltp': 2.25, 'trendschangeoi': [-1010],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 1110.4, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  10850: {'CE': {'oi': 104, 'changeinoi': 27, 'ltp': 2.05, 'trendschangeoi': [27],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 10900: {
            'CE': {'oi': 2261, 'changeinoi': -419, 'ltp': 1.7, 'trendschangeoi': [-419],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 10950: {
            'CE': {'oi': 144, 'changeinoi': 102, 'ltp': 1.6, 'trendschangeoi': [102], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11000: {
            'CE': {'oi': 12605, 'changeinoi': -460, 'ltp': 1.4, 'trendschangeoi': [-460],
                   'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11050: {
            'CE': {'oi': 71, 'changeinoi': 21, 'ltp': 1.5, 'trendschangeoi': [21], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11100: {
            'CE': {'oi': 656, 'changeinoi': -244, 'ltp': 1.2, 'trendschangeoi': [-244], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11150: {
            'CE': {'oi': 49, 'changeinoi': 7, 'ltp': 1.1, 'trendschangeoi': [7], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11200: {
            'CE': {'oi': 1734, 'changeinoi': 111, 'ltp': 0.95, 'trendschangeoi': [111], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11250: {
            'CE': {'oi': 16, 'changeinoi': 14, 'ltp': 1, 'trendschangeoi': [14], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11300: {
            'CE': {'oi': 179, 'changeinoi': -8, 'ltp': 0.9, 'trendschangeoi': [-8], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 2, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11350: {
            'CE': {'oi': 7, 'changeinoi': 5, 'ltp': 1.1, 'trendschangeoi': [5], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11400: {
            'CE': {'oi': 101, 'changeinoi': 7, 'ltp': 0.8, 'trendschangeoi': [7], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11450: {
            'CE': {'oi': 34, 'changeinoi': 4, 'ltp': 0.75, 'trendschangeoi': [4], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11500: {
            'CE': {'oi': 2597, 'changeinoi': 367, 'ltp': 0.65, 'trendschangeoi': [367], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11550: {
            'CE': {'oi': 4, 'changeinoi': 3, 'ltp': 0.5, 'trendschangeoi': [3], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11600: {
            'CE': {'oi': 39, 'changeinoi': 15, 'ltp': 0.6, 'trendschangeoi': [15], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}, 11650: {
            'CE': {'oi': 162, 'changeinoi': 108, 'ltp': 0.7, 'trendschangeoi': [108], 'trends': [-1, -1, -1, -1, -1]},
            'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'time': '12:58:56', 'date': '12-Jun-2020',
                  'price': 20058.5, 'turnoverprice': 20050, 14300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 2565, 'changeinoi': 2484, 'ltp': 6.3, 'trendschangeoi': [2484],
                            'trends': [-1, -1, -1, -1, -1]}}, 14400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  14500: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 3.05, 'trendschangeoi': [1],
                             'trends': [-1, -1, -1, -1, -1]}}, 14600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  14700: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 14800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  14900: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 15000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 430, 'changeinoi': 430, 'ltp': 7.9, 'trendschangeoi': [430],
                            'trends': [-1, -1, -1, -1, -1]}}, 15100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  15200: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 15300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  15400: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 9, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 15500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 946, 'changeinoi': 946, 'ltp': 10.75, 'trendschangeoi': [946],
                            'trends': [-1, -1, -1, -1, -1]}}, 15600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  15700: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 15800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  15900: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 16000: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 4197.3, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 7232, 'changeinoi': 6079, 'ltp': 15.55, 'trendschangeoi': [6079],
                            'trends': [-1, -1, -1, -1, -1]}}, 16100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  16200: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 13, 'changeinoi': 13, 'ltp': 19, 'trendschangeoi': [13],
                             'trends': [-1, -1, -1, -1, -1]}}, 16300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  16400: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                             'trends': [-1, -1, -1, -1, -1]}}, 16500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3384.9, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 4592, 'changeinoi': 3890, 'ltp': 24.1, 'trendschangeoi': [3890],
                            'trends': [-1, -1, -1, -1, -1]}}, 16600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  16700: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 25, 'changeinoi': 25, 'ltp': 30, 'trendschangeoi': [25],
                             'trends': [-1, -1, -1, -1, -1]}}, 16800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  16900: {
                      'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                      'PE': {'oi': 45, 'changeinoi': 45, 'ltp': 37, 'trendschangeoi': [45],
                             'trends': [-1, -1, -1, -1, -1]}}, 17000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3200, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 9657, 'changeinoi': 7823, 'ltp': 39.25, 'trendschangeoi': [7823],
                            'trends': [-1, -1, -1, -1, -1]}}, 17100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': 25, 'ltp': 42.7, 'trendschangeoi': [25],
                            'trends': [-1, -1, -1, -1, -1]}}, 17200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 70, 'changeinoi': 70, 'ltp': 46.95, 'trendschangeoi': [70],
                            'trends': [-1, -1, -1, -1, -1]}}, 17300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 18, 'changeinoi': 18, 'ltp': 49.05, 'trendschangeoi': [18],
                            'trends': [-1, -1, -1, -1, -1]}}, 17400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 286, 'changeinoi': 276, 'ltp': 57, 'trendschangeoi': [276],
                            'trends': [-1, -1, -1, -1, -1]}}, 17500: {
                     'CE': {'oi': 5, 'changeinoi': 2, 'ltp': 2350.35, 'trendschangeoi': [2],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 10518, 'changeinoi': 8928, 'ltp': 63.85, 'trendschangeoi': [8928],
                            'trends': [-1, -1, -1, -1, -1]}}, 17600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 295, 'changeinoi': 295, 'ltp': 69.3, 'trendschangeoi': [295],
                            'trends': [-1, -1, -1, -1, -1]}}, 17700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 2266.3, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 726, 'changeinoi': 674, 'ltp': 76.4, 'trendschangeoi': [674],
                            'trends': [-1, -1, -1, -1, -1]}}, 17800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1710, 'changeinoi': 1607, 'ltp': 84.85, 'trendschangeoi': [1607],
                            'trends': [-1, -1, -1, -1, -1]}}, 17900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 310, 'changeinoi': 310, 'ltp': 92.9, 'trendschangeoi': [310],
                            'trends': [-1, -1, -1, -1, -1]}}, 18000: {
                     'CE': {'oi': 78, 'changeinoi': 21, 'ltp': 1950, 'trendschangeoi': [21],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 17243, 'changeinoi': 11320, 'ltp': 102.75, 'trendschangeoi': [11320],
                            'trends': [-1, -1, -1, -1, -1]}}, 18100: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 2217.05, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1329, 'changeinoi': 1128, 'ltp': 114.4, 'trendschangeoi': [1128],
                            'trends': [-1, -1, -1, -1, -1]}}, 18200: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1824, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1891, 'changeinoi': 1794, 'ltp': 124.7, 'trendschangeoi': [1794],
                            'trends': [-1, -1, -1, -1, -1]}}, 18300: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1620.9, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 896, 'changeinoi': 882, 'ltp': 136.95, 'trendschangeoi': [882],
                            'trends': [-1, -1, -1, -1, -1]}}, 18400: {
                     'CE': {'oi': 11, 'changeinoi': 11, 'ltp': 1779.75, 'trendschangeoi': [11],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1692, 'changeinoi': 1618, 'ltp': 149.8, 'trendschangeoi': [1618],
                            'trends': [-1, -1, -1, -1, -1]}}, 18500: {
                     'CE': {'oi': 154, 'changeinoi': 67, 'ltp': 1765.7, 'trendschangeoi': [67],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 15489, 'changeinoi': 9688, 'ltp': 163.4, 'trendschangeoi': [9688],
                            'trends': [-1, -1, -1, -1, -1]}}, 18600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1663.4, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1323, 'changeinoi': 1233, 'ltp': 180.1, 'trendschangeoi': [1233],
                            'trends': [-1, -1, -1, -1, -1]}}, 18700: {
                     'CE': {'oi': 2, 'changeinoi': 2, 'ltp': 1534.45, 'trendschangeoi': [2],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1346, 'changeinoi': 1110, 'ltp': 197.8, 'trendschangeoi': [1110],
                            'trends': [-1, -1, -1, -1, -1]}}, 18800: {
                     'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 1558.95, 'trendschangeoi': [5],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 2325, 'changeinoi': 1868, 'ltp': 217.45, 'trendschangeoi': [1868],
                            'trends': [-1, -1, -1, -1, -1]}}, 18900: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1250, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1581, 'changeinoi': 1301, 'ltp': 237, 'trendschangeoi': [1301],
                            'trends': [-1, -1, -1, -1, -1]}}, 19000: {
                     'CE': {'oi': 989, 'changeinoi': 747, 'ltp': 1280.5, 'trendschangeoi': [747],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 24119, 'changeinoi': 12026, 'ltp': 260.7, 'trendschangeoi': [12026],
                            'trends': [-1, -1, -1, -1, -1]}}, 19100: {
                     'CE': {'oi': 9, 'changeinoi': 9, 'ltp': 1355.8, 'trendschangeoi': [9],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1724, 'changeinoi': 1615, 'ltp': 286.2, 'trendschangeoi': [1615],
                            'trends': [-1, -1, -1, -1, -1]}}, 19200: {
                     'CE': {'oi': 34, 'changeinoi': 34, 'ltp': 1140.8, 'trendschangeoi': [34],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 4686, 'changeinoi': 4520, 'ltp': 313.9, 'trendschangeoi': [4520],
                            'trends': [-1, -1, -1, -1, -1]}}, 19300: {
                     'CE': {'oi': 38, 'changeinoi': 38, 'ltp': 1070, 'trendschangeoi': [38],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 3599, 'changeinoi': 3231, 'ltp': 341.65, 'trendschangeoi': [3231],
                            'trends': [-1, -1, -1, -1, -1]}}, 19400: {
                     'CE': {'oi': 56, 'changeinoi': 56, 'ltp': 1025.2, 'trendschangeoi': [56],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1976, 'changeinoi': 1468, 'ltp': 373.4, 'trendschangeoi': [1468],
                            'trends': [-1, -1, -1, -1, -1]}}, 19500: {
                     'CE': {'oi': 3457, 'changeinoi': 3245, 'ltp': 937, 'trendschangeoi': [3245],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 16628, 'changeinoi': 2830, 'ltp': 403.85, 'trendschangeoi': [2830],
                            'trends': [-1, -1, -1, -1, -1]}}, 19600: {
                     'CE': {'oi': 464, 'changeinoi': 463, 'ltp': 864.2, 'trendschangeoi': [463],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 2291, 'changeinoi': 2103, 'ltp': 442.95, 'trendschangeoi': [2103],
                            'trends': [-1, -1, -1, -1, -1]}}, 19700: {
                     'CE': {'oi': 1320, 'changeinoi': 1320, 'ltp': 819, 'trendschangeoi': [1320],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 4197, 'changeinoi': 3603, 'ltp': 477.95, 'trendschangeoi': [3603],
                            'trends': [-1, -1, -1, -1, -1]}}, 19800: {
                     'CE': {'oi': 2251, 'changeinoi': 2250, 'ltp': 744.9, 'trendschangeoi': [2250],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 4091, 'changeinoi': 3618, 'ltp': 519.25, 'trendschangeoi': [3618],
                            'trends': [-1, -1, -1, -1, -1]}}, 19900: {
                     'CE': {'oi': 1732, 'changeinoi': 1730, 'ltp': 690.4, 'trendschangeoi': [1730],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 3513, 'changeinoi': 3188, 'ltp': 563.1, 'trendschangeoi': [3188],
                            'trends': [-1, -1, -1, -1, -1]}}, 20000: {
                     'CE': {'oi': 10783, 'changeinoi': 9218, 'ltp': 636.8, 'trendschangeoi': [9218],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 11773, 'changeinoi': 1652, 'ltp': 605, 'trendschangeoi': [1652],
                            'trends': [-1, -1, -1, -1, -1]}}, 20100: {
                     'CE': {'oi': 1596, 'changeinoi': 1596, 'ltp': 587.05, 'trendschangeoi': [1596],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 1058, 'changeinoi': 637, 'ltp': 654.65, 'trendschangeoi': [637],
                            'trends': [-1, -1, -1, -1, -1]}}, 20200: {
                     'CE': {'oi': 2575, 'changeinoi': 2543, 'ltp': 537.8, 'trendschangeoi': [2543],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 904, 'changeinoi': -8, 'ltp': 710.45, 'trendschangeoi': [-8],
                            'trends': [-1, -1, -1, -1, -1]}}, 20300: {
                     'CE': {'oi': 1659, 'changeinoi': 1584, 'ltp': 492.2, 'trendschangeoi': [1584],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 595, 'changeinoi': -379, 'ltp': 760, 'trendschangeoi': [-379],
                            'trends': [-1, -1, -1, -1, -1]}}, 20400: {
                     'CE': {'oi': 2170, 'changeinoi': 2044, 'ltp': 447.9, 'trendschangeoi': [2044],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 727, 'changeinoi': -12, 'ltp': 805.85, 'trendschangeoi': [-12],
                            'trends': [-1, -1, -1, -1, -1]}}, 20500: {
                     'CE': {'oi': 10743, 'changeinoi': 6640, 'ltp': 408.35, 'trendschangeoi': [6640],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 4316, 'changeinoi': -1548, 'ltp': 883, 'trendschangeoi': [-1548],
                            'trends': [-1, -1, -1, -1, -1]}}, 20600: {
                     'CE': {'oi': 2225, 'changeinoi': 1281, 'ltp': 371.05, 'trendschangeoi': [1281],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 351, 'changeinoi': -162, 'ltp': 930, 'trendschangeoi': [-162],
                            'trends': [-1, -1, -1, -1, -1]}}, 20700: {
                     'CE': {'oi': 2187, 'changeinoi': 1334, 'ltp': 334.3, 'trendschangeoi': [1334],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 370, 'changeinoi': -40, 'ltp': 985.5, 'trendschangeoi': [-40],
                            'trends': [-1, -1, -1, -1, -1]}}, 20800: {
                     'CE': {'oi': 3606, 'changeinoi': 2308, 'ltp': 302, 'trendschangeoi': [2308],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 371, 'changeinoi': -109, 'ltp': 1075.15, 'trendschangeoi': [-109],
                            'trends': [-1, -1, -1, -1, -1]}}, 20900: {
                     'CE': {'oi': 1921, 'changeinoi': 1409, 'ltp': 272.35, 'trendschangeoi': [1409],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 239, 'changeinoi': -45, 'ltp': 1146.95, 'trendschangeoi': [-45],
                            'trends': [-1, -1, -1, -1, -1]}}, 21000: {
                     'CE': {'oi': 21142, 'changeinoi': 10221, 'ltp': 245.4, 'trendschangeoi': [10221],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 3829, 'changeinoi': -354, 'ltp': 1217.35, 'trendschangeoi': [-354],
                            'trends': [-1, -1, -1, -1, -1]}}, 21100: {
                     'CE': {'oi': 2324, 'changeinoi': 1514, 'ltp': 219.25, 'trendschangeoi': [1514],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 353, 'changeinoi': -20, 'ltp': 1291.2, 'trendschangeoi': [-20],
                            'trends': [-1, -1, -1, -1, -1]}}, 21200: {
                     'CE': {'oi': 2950, 'changeinoi': 1453, 'ltp': 197.35, 'trendschangeoi': [1453],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 155, 'changeinoi': -19, 'ltp': 1510.2, 'trendschangeoi': [-19],
                            'trends': [-1, -1, -1, -1, -1]}}, 21300: {
                     'CE': {'oi': 2560, 'changeinoi': 1510, 'ltp': 175.95, 'trendschangeoi': [1510],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 87, 'changeinoi': 0, 'ltp': 1498.5, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]}}, 21400: {
                     'CE': {'oi': 1557, 'changeinoi': 677, 'ltp': 156.05, 'trendschangeoi': [677],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': -2, 'ltp': 1308.6, 'trendschangeoi': [-2],
                            'trends': [-1, -1, -1, -1, -1]}}, 21500: {
                     'CE': {'oi': 16886, 'changeinoi': 5571, 'ltp': 138.15, 'trendschangeoi': [5571],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 971, 'changeinoi': -475, 'ltp': 1601.3, 'trendschangeoi': [-475],
                            'trends': [-1, -1, -1, -1, -1]}}, 21600: {
                     'CE': {'oi': 2069, 'changeinoi': 1375, 'ltp': 123.9, 'trendschangeoi': [1375],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 10, 'changeinoi': 2, 'ltp': 1641.1, 'trendschangeoi': [2],
                            'trends': [-1, -1, -1, -1, -1]}}, 21700: {
                     'CE': {'oi': 1905, 'changeinoi': 1402, 'ltp': 109.3, 'trendschangeoi': [1402],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 13, 'changeinoi': -1, 'ltp': 1959.1, 'trendschangeoi': [-1],
                            'trends': [-1, -1, -1, -1, -1]}}, 21800: {
                     'CE': {'oi': 4357, 'changeinoi': 3184, 'ltp': 95.95, 'trendschangeoi': [3184],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 2, 'changeinoi': 1, 'ltp': 2140.85, 'trendschangeoi': [1],
                            'trends': [-1, -1, -1, -1, -1]}}, 21900: {
                     'CE': {'oi': 1370, 'changeinoi': 957, 'ltp': 85.95, 'trendschangeoi': [957],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  22000: {'CE': {'oi': 19932, 'changeinoi': 8904, 'ltp': 75.65, 'trendschangeoi': [8904],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 354, 'changeinoi': -20, 'ltp': 2002.3, 'trendschangeoi': [-20],
                                 'trends': [-1, -1, -1, -1, -1]}}, 22100: {
                     'CE': {'oi': 907, 'changeinoi': 639, 'ltp': 67.75, 'trendschangeoi': [639],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  22200: {'CE': {'oi': 1210, 'changeinoi': 710, 'ltp': 59.7, 'trendschangeoi': [710],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 22300: {
                     'CE': {'oi': 824, 'changeinoi': 634, 'ltp': 52.65, 'trendschangeoi': [634],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  22400: {'CE': {'oi': 784, 'changeinoi': 473, 'ltp': 47.65, 'trendschangeoi': [473],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 22500: {
                     'CE': {'oi': 12721, 'changeinoi': 4640, 'ltp': 41.6, 'trendschangeoi': [4640],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  22600: {'CE': {'oi': 1088, 'changeinoi': 445, 'ltp': 37.55, 'trendschangeoi': [445],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 22700: {
                     'CE': {'oi': 681, 'changeinoi': 485, 'ltp': 32.15, 'trendschangeoi': [485],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  22800: {'CE': {'oi': 726, 'changeinoi': 435, 'ltp': 29.6, 'trendschangeoi': [435],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 22900: {
                     'CE': {'oi': 690, 'changeinoi': 376, 'ltp': 25.8, 'trendschangeoi': [376],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  23000: {'CE': {'oi': 13319, 'changeinoi': 2525, 'ltp': 22.05, 'trendschangeoi': [2525],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 33, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 23100: {
                     'CE': {'oi': 350, 'changeinoi': 240, 'ltp': 19.85, 'trendschangeoi': [240],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  23200: {'CE': {'oi': 754, 'changeinoi': 157, 'ltp': 17, 'trendschangeoi': [157],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 23300: {
                     'CE': {'oi': 17, 'changeinoi': 17, 'ltp': 14, 'trendschangeoi': [17],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  23400: {'CE': {'oi': 196, 'changeinoi': 70, 'ltp': 12.8, 'trendschangeoi': [70],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 23500: {
                     'CE': {'oi': 8701, 'changeinoi': 2758, 'ltp': 11.8, 'trendschangeoi': [2758],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  23600: {'CE': {'oi': 122, 'changeinoi': 107, 'ltp': 9.8, 'trendschangeoi': [107],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 23700: {
                     'CE': {'oi': 124, 'changeinoi': 124, 'ltp': 8.4, 'trendschangeoi': [124],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  23800: {'CE': {'oi': 302, 'changeinoi': 171, 'ltp': 9.55, 'trendschangeoi': [171],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 23900: {
                     'CE': {'oi': 402, 'changeinoi': 206, 'ltp': 8.9, 'trendschangeoi': [206],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  24000: {'CE': {'oi': 5634, 'changeinoi': 1267, 'ltp': 7, 'trendschangeoi': [1267],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 24100: {
                     'CE': {'oi': 47, 'changeinoi': 38, 'ltp': 6.3, 'trendschangeoi': [38],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  24200: {'CE': {'oi': 59, 'changeinoi': 34, 'ltp': 6.75, 'trendschangeoi': [34],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 24300: {
                     'CE': {'oi': 56, 'changeinoi': 16, 'ltp': 6.85, 'trendschangeoi': [16],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0], 'trends': [-1, -1, -1, -1, -1]}},
                  24400: {'CE': {'oi': 172, 'changeinoi': -61, 'ltp': 6.15, 'trendschangeoi': [-61],
                                 'trends': [-1, -1, -1, -1, -1]},
                          'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                                 'trends': [-1, -1, -1, -1, -1]}}, 24500: {
                     'CE': {'oi': 5359, 'changeinoi': 945, 'ltp': 5.75, 'trendschangeoi': [945],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0],
                            'trends': [-1, -1, -1, -1, -1]}}}],
                [{'index': 'NIFTY', 'marketstatus': True, 'time': '13:04:26', 'date': '12-Jun-2020', 'price': 9766.8,
                  'turnoverprice': 9750, 7300: {'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                                                       'trends': [0, -1, -1, -1, -1]},
                                                'PE': {'oi': 79, 'changeinoi': 53, 'ltp': 0.8,
                                                       'trendschangeoi': [53, 52], 'trends': [-1, -1, -1, -1, -1]}},
                  7350: {'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                                'trends': [0, -1, -1, -1, -1]},
                         'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 1.7, 'trendschangeoi': [1, 1],
                                'trends': [0, -1, -1, -1, -1]}}, 7400: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 1.15, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7450: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0.75, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7500: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 835, 'changeinoi': 830, 'ltp': 1.15, 'trendschangeoi': [830, 830],
                               'trends': [0, -1, -1, -1, -1]}}, 7550: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7600: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7650: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7700: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7750: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7800: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 2.9, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7850: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 7900: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 8, 'changeinoi': 8, 'ltp': 1.95, 'trendschangeoi': [8, 8],
                               'trends': [0, -1, -1, -1, -1]}}, 7950: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8000: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 3653, 'changeinoi': 1760, 'ltp': 1.9, 'trendschangeoi': [1760, 1781],
                               'trends': [21, -1, -1, -1, -1]}}, 8050: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8100: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8150: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8200: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8250: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8300: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 303, 'changeinoi': 303, 'ltp': 3, 'trendschangeoi': [303, 306],
                               'trends': [3, -1, -1, -1, -1]}}, 8350: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8400: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 737, 'changeinoi': 735, 'ltp': 3.75, 'trendschangeoi': [735, 734],
                               'trends': [-1, -1, -1, -1, -1]}}, 8450: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8500: {
                        'CE': {'oi': 6, 'changeinoi': 0, 'ltp': 1210, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 7676, 'changeinoi': 3750, 'ltp': 4.9, 'trendschangeoi': [3750, 3755],
                               'trends': [5, -1, -1, -1, -1]}}, 8550: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8600: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 3172, 'changeinoi': 3107, 'ltp': 6.4, 'trendschangeoi': [3107, 3121],
                               'trends': [14, -1, -1, -1, -1]}}, 8650: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8700: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1000, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 4408, 'changeinoi': 4026, 'ltp': 8.3, 'trendschangeoi': [4026, 3881],
                               'trends': [-145, -1, -1, -1, -1]}}, 8750: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 8800: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 4884, 'changeinoi': 3511, 'ltp': 10.9, 'trendschangeoi': [3511, 3585],
                               'trends': [74, -1, -1, -1, -1]}}, 8850: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 25, 'changeinoi': 22, 'ltp': 13.25, 'trendschangeoi': [22, 23],
                               'trends': [1, -1, -1, -1, -1]}}, 8900: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 3874, 'changeinoi': 2555, 'ltp': 14.6, 'trendschangeoi': [2555, 2560],
                               'trends': [5, -1, -1, -1, -1]}}, 8950: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 404, 'changeinoi': 396, 'ltp': 17.3, 'trendschangeoi': [396, 398],
                               'trends': [2, -1, -1, -1, -1]}}, 9000: {
                        'CE': {'oi': 208, 'changeinoi': 183, 'ltp': 765, 'trendschangeoi': [183, 183],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 24872, 'changeinoi': 11047, 'ltp': 19.25, 'trendschangeoi': [11047, 11132],
                               'trends': [85, -1, -1, -1, -1]}}, 9050: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 645.4, 'trendschangeoi': [1, 1],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 828, 'changeinoi': 795, 'ltp': 22.65, 'trendschangeoi': [795, 794],
                               'trends': [-1, -1, -1, -1, -1]}}, 9100: {
                        'CE': {'oi': 88, 'changeinoi': 1, 'ltp': 693.9, 'trendschangeoi': [1, 1],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 8068, 'changeinoi': 4385, 'ltp': 25.9, 'trendschangeoi': [4385, 4383],
                               'trends': [-2, -1, -1, -1, -1]}}, 9150: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 648.8, 'trendschangeoi': [1, 1],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 988, 'changeinoi': 928, 'ltp': 30.1, 'trendschangeoi': [928, 927],
                               'trends': [-1, -1, -1, -1, -1]}}, 9200: {
                        'CE': {'oi': 68, 'changeinoi': 45, 'ltp': 548.6, 'trendschangeoi': [45, 45],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 13331, 'changeinoi': 7768, 'ltp': 34.45, 'trendschangeoi': [7768, 7697],
                               'trends': [-71, -1, -1, -1, -1]}}, 9250: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 540.7, 'trendschangeoi': [1, 1],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 1331, 'changeinoi': 888, 'ltp': 39.8, 'trendschangeoi': [888, 876],
                               'trends': [-12, -1, -1, -1, -1]}}, 9300: {
                        'CE': {'oi': 435, 'changeinoi': -17, 'ltp': 498.45, 'trendschangeoi': [-17, -17],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 19457, 'changeinoi': 11370, 'ltp': 46.65, 'trendschangeoi': [11370, 11672],
                               'trends': [302, -1, -1, -1, -1]}}, 9350: {
                        'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 420.3, 'trendschangeoi': [5, 5],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 1703, 'changeinoi': 1423, 'ltp': 53.45, 'trendschangeoi': [1423, 1401],
                               'trends': [-22, -1, -1, -1, -1]}}, 9400: {
                        'CE': {'oi': 474, 'changeinoi': 320, 'ltp': 403.05, 'trendschangeoi': [320, 321],
                               'trends': [1, -1, -1, -1, -1]},
                        'PE': {'oi': 19384, 'changeinoi': 12195, 'ltp': 62.05, 'trendschangeoi': [12195, 12041],
                               'trends': [-154, -1, -1, -1, -1]}}, 9450: {
                        'CE': {'oi': 38, 'changeinoi': 37, 'ltp': 356.1, 'trendschangeoi': [37, 37],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 1687, 'changeinoi': 1096, 'ltp': 71, 'trendschangeoi': [1096, 1137],
                               'trends': [41, -1, -1, -1, -1]}}, 9500: {
                        'CE': {'oi': 3041, 'changeinoi': 1710, 'ltp': 333.95, 'trendschangeoi': [1710, 1764],
                               'trends': [54, -1, -1, -1, -1]},
                        'PE': {'oi': 27460, 'changeinoi': 11157, 'ltp': 82.3, 'trendschangeoi': [11157, 10920],
                               'trends': [-237, -1, -1, -1, -1]}}, 9550: {
                        'CE': {'oi': 134, 'changeinoi': 131, 'ltp': 293, 'trendschangeoi': [131, 155],
                               'trends': [24, -1, -1, -1, -1]},
                        'PE': {'oi': 2004, 'changeinoi': 1565, 'ltp': 95.45, 'trendschangeoi': [1565, 1622],
                               'trends': [57, -1, -1, -1, -1]}}, 9600: {
                        'CE': {'oi': 4909, 'changeinoi': 4593, 'ltp': 260.9, 'trendschangeoi': [4593, 4638],
                               'trends': [45, -1, -1, -1, -1]},
                        'PE': {'oi': 19989, 'changeinoi': 10785, 'ltp': 109.2, 'trendschangeoi': [10785, 10739],
                               'trends': [-46, -1, -1, -1, -1]}}, 9650: {
                        'CE': {'oi': 1005, 'changeinoi': 1000, 'ltp': 224.55, 'trendschangeoi': [1000, 1026],
                               'trends': [26, -1, -1, -1, -1]},
                        'PE': {'oi': 2736, 'changeinoi': 2005, 'ltp': 125, 'trendschangeoi': [2005, 1985],
                               'trends': [-20, -1, -1, -1, -1]}}, 9700: {
                        'CE': {'oi': 12076, 'changeinoi': 11305, 'ltp': 195.6, 'trendschangeoi': [11305, 11421],
                               'trends': [116, -1, -1, -1, -1]},
                        'PE': {'oi': 18945, 'changeinoi': 9452, 'ltp': 143.15, 'trendschangeoi': [9452, 9555],
                               'trends': [103, -1, -1, -1, -1]}}, 9750: {
                        'CE': {'oi': 2206, 'changeinoi': 2202, 'ltp': 166.5, 'trendschangeoi': [2202, 2108],
                               'trends': [-94, -1, -1, -1, -1]},
                        'PE': {'oi': 2274, 'changeinoi': 994, 'ltp': 164.75, 'trendschangeoi': [994, 847],
                               'trends': [-147, -1, -1, -1, -1]}}, 9800: {
                        'CE': {'oi': 17474, 'changeinoi': 14114, 'ltp': 139.75, 'trendschangeoi': [14114, 14332],
                               'trends': [218, -1, -1, -1, -1]},
                        'PE': {'oi': 9197, 'changeinoi': -1610, 'ltp': 188.7, 'trendschangeoi': [-1610, -1580],
                               'trends': [30, -1, -1, -1, -1]}}, 9850: {
                        'CE': {'oi': 1301, 'changeinoi': 1197, 'ltp': 115.75, 'trendschangeoi': [1197, 1225],
                               'trends': [28, -1, -1, -1, -1]},
                        'PE': {'oi': 905, 'changeinoi': -1, 'ltp': 214.1, 'trendschangeoi': [-1, 29],
                               'trends': [30, -1, -1, -1, -1]}}, 9900: {
                        'CE': {'oi': 22392, 'changeinoi': 14029, 'ltp': 95.6, 'trendschangeoi': [14029, 14108],
                               'trends': [79, -1, -1, -1, -1]},
                        'PE': {'oi': 6381, 'changeinoi': -3774, 'ltp': 243, 'trendschangeoi': [-3774, -3808],
                               'trends': [-34, -1, -1, -1, -1]}}, 9950: {
                        'CE': {'oi': 2283, 'changeinoi': 1428, 'ltp': 76.85, 'trendschangeoi': [1428, 1476],
                               'trends': [48, -1, -1, -1, -1]},
                        'PE': {'oi': 478, 'changeinoi': -269, 'ltp': 288, 'trendschangeoi': [-269, -268],
                               'trends': [1, -1, -1, -1, -1]}}, 10000: {
                        'CE': {'oi': 27323, 'changeinoi': 13998, 'ltp': 61.05, 'trendschangeoi': [13998, 14047],
                               'trends': [49, -1, -1, -1, -1]},
                        'PE': {'oi': 7255, 'changeinoi': -686, 'ltp': 307.35, 'trendschangeoi': [-686, -652],
                               'trends': [34, -1, -1, -1, -1]}}, 10050: {
                        'CE': {'oi': 3205, 'changeinoi': 1394, 'ltp': 48.15, 'trendschangeoi': [1394, 1442],
                               'trends': [48, -1, -1, -1, -1]},
                        'PE': {'oi': 663, 'changeinoi': -60, 'ltp': 352, 'trendschangeoi': [-60, -59],
                               'trends': [1, -1, -1, -1, -1]}}, 10100: {
                        'CE': {'oi': 16910, 'changeinoi': 2804, 'ltp': 37.6, 'trendschangeoi': [2804, 2777],
                               'trends': [-27, -1, -1, -1, -1]},
                        'PE': {'oi': 4041, 'changeinoi': -369, 'ltp': 384.2, 'trendschangeoi': [-369, -379],
                               'trends': [-10, -1, -1, -1, -1]}}, 10150: {
                        'CE': {'oi': 4695, 'changeinoi': 2948, 'ltp': 29.25, 'trendschangeoi': [2948, 2969],
                               'trends': [21, -1, -1, -1, -1]},
                        'PE': {'oi': 181, 'changeinoi': -38, 'ltp': 427.1, 'trendschangeoi': [-38, -38],
                               'trends': [0, -1, -1, -1, -1]}}, 10200: {
                        'CE': {'oi': 16665, 'changeinoi': 2720, 'ltp': 22.85, 'trendschangeoi': [2720, 2780],
                               'trends': [60, -1, -1, -1, -1]},
                        'PE': {'oi': 1027, 'changeinoi': -212, 'ltp': 471.45, 'trendschangeoi': [-212, -212],
                               'trends': [0, -1, -1, -1, -1]}}, 10250: {
                        'CE': {'oi': 2094, 'changeinoi': 620, 'ltp': 17.85, 'trendschangeoi': [620, 578],
                               'trends': [-42, -1, -1, -1, -1]},
                        'PE': {'oi': 93, 'changeinoi': -17, 'ltp': 505.85, 'trendschangeoi': [-17, -17],
                               'trends': [0, -1, -1, -1, -1]}}, 10300: {
                        'CE': {'oi': 18182, 'changeinoi': 4116, 'ltp': 14.2, 'trendschangeoi': [4116, 4187],
                               'trends': [71, -1, -1, -1, -1]},
                        'PE': {'oi': 893, 'changeinoi': -246, 'ltp': 559.1, 'trendschangeoi': [-246, -246],
                               'trends': [0, -1, -1, -1, -1]}}, 10350: {
                        'CE': {'oi': 1402, 'changeinoi': 285, 'ltp': 11.25, 'trendschangeoi': [285, 296],
                               'trends': [11, -1, -1, -1, -1]},
                        'PE': {'oi': 31, 'changeinoi': -10, 'ltp': 614, 'trendschangeoi': [-10, -10],
                               'trends': [0, -1, -1, -1, -1]}}, 10400: {
                        'CE': {'oi': 13473, 'changeinoi': 1963, 'ltp': 9.4, 'trendschangeoi': [1963, 2002],
                               'trends': [39, -1, -1, -1, -1]},
                        'PE': {'oi': 165, 'changeinoi': -13, 'ltp': 670.75, 'trendschangeoi': [-13, -14],
                               'trends': [-1, -1, -1, -1, -1]}}, 10450: {
                        'CE': {'oi': 809, 'changeinoi': 25, 'ltp': 7.9, 'trendschangeoi': [25, 1],
                               'trends': [-24, -1, -1, -1, -1]},
                        'PE': {'oi': 7, 'changeinoi': 0, 'ltp': 732.7, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10500: {
                        'CE': {'oi': 26352, 'changeinoi': 7426, 'ltp': 6.7, 'trendschangeoi': [7426, 7328],
                               'trends': [-98, -1, -1, -1, -1]},
                        'PE': {'oi': 647, 'changeinoi': -3, 'ltp': 749.5, 'trendschangeoi': [-3, -3],
                               'trends': [0, -1, -1, -1, -1]}}, 10550: {
                        'CE': {'oi': 818, 'changeinoi': 29, 'ltp': 5.5, 'trendschangeoi': [29, 17],
                               'trends': [-12, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10600: {
                        'CE': {'oi': 11603, 'changeinoi': 2072, 'ltp': 4.7, 'trendschangeoi': [2072, 2005],
                               'trends': [-67, -1, -1, -1, -1]},
                        'PE': {'oi': 49, 'changeinoi': -1, 'ltp': 889.45, 'trendschangeoi': [-1, -1],
                               'trends': [0, -1, -1, -1, -1]}}, 10650: {
                        'CE': {'oi': 812, 'changeinoi': 391, 'ltp': 3.95, 'trendschangeoi': [391, 404],
                               'trends': [13, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10700: {
                        'CE': {'oi': 7791, 'changeinoi': 46, 'ltp': 3.25, 'trendschangeoi': [46, 97],
                               'trends': [51, -1, -1, -1, -1]},
                        'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 934.65, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10750: {
                        'CE': {'oi': 433, 'changeinoi': 17, 'ltp': 2.85, 'trendschangeoi': [17, 16],
                               'trends': [-1, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10800: {
                        'CE': {'oi': 5115, 'changeinoi': -951, 'ltp': 2.25, 'trendschangeoi': [-951, -1010],
                               'trends': [-59, -1, -1, -1, -1]},
                        'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 1110.4, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10850: {
                        'CE': {'oi': 104, 'changeinoi': 27, 'ltp': 2.05, 'trendschangeoi': [27, 27],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10900: {
                        'CE': {'oi': 2294, 'changeinoi': -386, 'ltp': 1.7, 'trendschangeoi': [-386, -419],
                               'trends': [-33, -1, -1, -1, -1]},
                        'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 10950: {
                        'CE': {'oi': 144, 'changeinoi': 102, 'ltp': 1.6, 'trendschangeoi': [102, 102],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11000: {
                        'CE': {'oi': 12775, 'changeinoi': -290, 'ltp': 1.35, 'trendschangeoi': [-290, -460],
                               'trends': [-170, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11050: {
                        'CE': {'oi': 71, 'changeinoi': 21, 'ltp': 1.5, 'trendschangeoi': [21, 21],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11100: {
                        'CE': {'oi': 657, 'changeinoi': -243, 'ltp': 1.2, 'trendschangeoi': [-243, -244],
                               'trends': [-1, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11150: {
                        'CE': {'oi': 49, 'changeinoi': 7, 'ltp': 1.1, 'trendschangeoi': [7, 7],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11200: {
                        'CE': {'oi': 1749, 'changeinoi': 126, 'ltp': 0.95, 'trendschangeoi': [126, 111],
                               'trends': [-15, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11250: {
                        'CE': {'oi': 16, 'changeinoi': 14, 'ltp': 1, 'trendschangeoi': [14, 14],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11300: {
                        'CE': {'oi': 179, 'changeinoi': -8, 'ltp': 0.9, 'trendschangeoi': [-8, -8],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 2, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11350: {
                        'CE': {'oi': 7, 'changeinoi': 5, 'ltp': 1.1, 'trendschangeoi': [5, 5],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11400: {
                        'CE': {'oi': 101, 'changeinoi': 7, 'ltp': 0.8, 'trendschangeoi': [7, 7],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11450: {
                        'CE': {'oi': 34, 'changeinoi': 4, 'ltp': 0.75, 'trendschangeoi': [4, 4],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11500: {
                        'CE': {'oi': 2597, 'changeinoi': 367, 'ltp': 0.7, 'trendschangeoi': [367, 367],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11550: {
                        'CE': {'oi': 4, 'changeinoi': 3, 'ltp': 0.5, 'trendschangeoi': [3, 3],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11600: {
                        'CE': {'oi': 41, 'changeinoi': 17, 'ltp': 0.6, 'trendschangeoi': [17, 15],
                               'trends': [-2, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}, 11650: {
                        'CE': {'oi': 162, 'changeinoi': 108, 'ltp': 0.7, 'trendschangeoi': [108, 108],
                               'trends': [0, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                               'trends': [0, -1, -1, -1, -1]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'time': '13:04:26', 'date': '12-Jun-2020',
                  'price': 20058.05, 'turnoverprice': 20050, 14300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 2581, 'changeinoi': 2500, 'ltp': 6.3, 'trendschangeoi': [2500, 2484],
                            'trends': [-16, -1, -1, -1, -1]}}, 14400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 14500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 3.05, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]}}, 14600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 14700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 14800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 14900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 424, 'changeinoi': 424, 'ltp': 7.35, 'trendschangeoi': [424, 430],
                            'trends': [6, -1, -1, -1, -1]}}, 15100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 9, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 928, 'changeinoi': 928, 'ltp': 10.35, 'trendschangeoi': [928, 946],
                            'trends': [18, -1, -1, -1, -1]}}, 15600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 15900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16000: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 4197.3, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 7276, 'changeinoi': 6123, 'ltp': 15.35, 'trendschangeoi': [6123, 6079],
                            'trends': [-44, -1, -1, -1, -1]}}, 16100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 13, 'changeinoi': 13, 'ltp': 19, 'trendschangeoi': [13, 13],
                            'trends': [0, -1, -1, -1, -1]}}, 16300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3384.9, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 4675, 'changeinoi': 3973, 'ltp': 23.75, 'trendschangeoi': [3973, 3890],
                            'trends': [-83, -1, -1, -1, -1]}}, 16600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': 25, 'ltp': 30, 'trendschangeoi': [25, 25],
                            'trends': [0, -1, -1, -1, -1]}}, 16800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 16900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 45, 'changeinoi': 45, 'ltp': 37, 'trendschangeoi': [45, 45],
                            'trends': [0, -1, -1, -1, -1]}}, 17000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3200, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 9747, 'changeinoi': 7913, 'ltp': 38, 'trendschangeoi': [7913, 7823],
                            'trends': [-90, -1, -1, -1, -1]}}, 17100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': 25, 'ltp': 42.7, 'trendschangeoi': [25, 25],
                            'trends': [0, -1, -1, -1, -1]}}, 17200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 71, 'changeinoi': 71, 'ltp': 45, 'trendschangeoi': [71, 70],
                            'trends': [-1, -1, -1, -1, -1]}}, 17300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 18, 'changeinoi': 18, 'ltp': 49.05, 'trendschangeoi': [18, 18],
                            'trends': [0, -1, -1, -1, -1]}}, 17400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 285, 'changeinoi': 275, 'ltp': 55.15, 'trendschangeoi': [275, 276],
                            'trends': [1, -1, -1, -1, -1]}}, 17500: {
                     'CE': {'oi': 5, 'changeinoi': 2, 'ltp': 2350.35, 'trendschangeoi': [2, 2],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 10599, 'changeinoi': 9009, 'ltp': 62.1, 'trendschangeoi': [9009, 8928],
                            'trends': [-81, -1, -1, -1, -1]}}, 17600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 285, 'changeinoi': 285, 'ltp': 68.9, 'trendschangeoi': [285, 295],
                            'trends': [10, -1, -1, -1, -1]}}, 17700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 2266.3, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 714, 'changeinoi': 662, 'ltp': 75.15, 'trendschangeoi': [662, 674],
                            'trends': [12, -1, -1, -1, -1]}}, 17800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1749, 'changeinoi': 1646, 'ltp': 83.45, 'trendschangeoi': [1646, 1607],
                            'trends': [-39, -1, -1, -1, -1]}}, 17900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 297, 'changeinoi': 297, 'ltp': 92.6, 'trendschangeoi': [297, 310],
                            'trends': [13, -1, -1, -1, -1]}}, 18000: {
                     'CE': {'oi': 79, 'changeinoi': 22, 'ltp': 2150, 'trendschangeoi': [22, 21],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 17316, 'changeinoi': 11393, 'ltp': 101.05, 'trendschangeoi': [11393, 11320],
                            'trends': [-73, -1, -1, -1, -1]}}, 18100: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 2217.05, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1340, 'changeinoi': 1139, 'ltp': 111.85, 'trendschangeoi': [1139, 1128],
                            'trends': [-11, -1, -1, -1, -1]}}, 18200: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1824, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1973, 'changeinoi': 1876, 'ltp': 123.25, 'trendschangeoi': [1876, 1794],
                            'trends': [-82, -1, -1, -1, -1]}}, 18300: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1620.9, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 865, 'changeinoi': 851, 'ltp': 135.25, 'trendschangeoi': [851, 882],
                            'trends': [31, -1, -1, -1, -1]}}, 18400: {
                     'CE': {'oi': 11, 'changeinoi': 11, 'ltp': 1779.75, 'trendschangeoi': [11, 11],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1689, 'changeinoi': 1615, 'ltp': 149.7, 'trendschangeoi': [1615, 1618],
                            'trends': [3, -1, -1, -1, -1]}}, 18500: {
                     'CE': {'oi': 154, 'changeinoi': 67, 'ltp': 1670, 'trendschangeoi': [67, 67],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 15819, 'changeinoi': 10018, 'ltp': 163.1, 'trendschangeoi': [10018, 9688],
                            'trends': [-330, -1, -1, -1, -1]}}, 18600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1663.4, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1332, 'changeinoi': 1242, 'ltp': 180, 'trendschangeoi': [1242, 1233],
                            'trends': [-9, -1, -1, -1, -1]}}, 18700: {
                     'CE': {'oi': 2, 'changeinoi': 2, 'ltp': 1534.45, 'trendschangeoi': [2, 2],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1345, 'changeinoi': 1109, 'ltp': 198, 'trendschangeoi': [1109, 1110],
                            'trends': [1, -1, -1, -1, -1]}}, 18800: {
                     'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 1558.95, 'trendschangeoi': [5, 5],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 2363, 'changeinoi': 1906, 'ltp': 217.35, 'trendschangeoi': [1906, 1868],
                            'trends': [-38, -1, -1, -1, -1]}}, 18900: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1250, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1599, 'changeinoi': 1319, 'ltp': 238.1, 'trendschangeoi': [1319, 1301],
                            'trends': [-18, -1, -1, -1, -1]}}, 19000: {
                     'CE': {'oi': 977, 'changeinoi': 735, 'ltp': 1293.9, 'trendschangeoi': [735, 747],
                            'trends': [12, -1, -1, -1, -1]},
                     'PE': {'oi': 24971, 'changeinoi': 12878, 'ltp': 261.25, 'trendschangeoi': [12878, 12026],
                            'trends': [-852, -1, -1, -1, -1]}}, 19100: {
                     'CE': {'oi': 9, 'changeinoi': 9, 'ltp': 1355.8, 'trendschangeoi': [9, 9],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 1764, 'changeinoi': 1655, 'ltp': 286.2, 'trendschangeoi': [1655, 1615],
                            'trends': [-40, -1, -1, -1, -1]}}, 19200: {
                     'CE': {'oi': 34, 'changeinoi': 34, 'ltp': 1140.8, 'trendschangeoi': [34, 34],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 4759, 'changeinoi': 4593, 'ltp': 312.4, 'trendschangeoi': [4593, 4520],
                            'trends': [-73, -1, -1, -1, -1]}}, 19300: {
                     'CE': {'oi': 38, 'changeinoi': 38, 'ltp': 1070, 'trendschangeoi': [38, 38],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 3646, 'changeinoi': 3278, 'ltp': 342.5, 'trendschangeoi': [3278, 3231],
                            'trends': [-47, -1, -1, -1, -1]}}, 19400: {
                     'CE': {'oi': 46, 'changeinoi': 46, 'ltp': 980.3, 'trendschangeoi': [46, 56],
                            'trends': [10, -1, -1, -1, -1]},
                     'PE': {'oi': 2007, 'changeinoi': 1499, 'ltp': 370, 'trendschangeoi': [1499, 1468],
                            'trends': [-31, -1, -1, -1, -1]}}, 19500: {
                     'CE': {'oi': 3453, 'changeinoi': 3241, 'ltp': 939.9, 'trendschangeoi': [3241, 3245],
                            'trends': [4, -1, -1, -1, -1]},
                     'PE': {'oi': 16751, 'changeinoi': 2953, 'ltp': 404.95, 'trendschangeoi': [2953, 2830],
                            'trends': [-123, -1, -1, -1, -1]}}, 19600: {
                     'CE': {'oi': 485, 'changeinoi': 484, 'ltp': 878.4, 'trendschangeoi': [484, 463],
                            'trends': [-21, -1, -1, -1, -1]},
                     'PE': {'oi': 2287, 'changeinoi': 2099, 'ltp': 440, 'trendschangeoi': [2099, 2103],
                            'trends': [4, -1, -1, -1, -1]}}, 19700: {
                     'CE': {'oi': 1303, 'changeinoi': 1303, 'ltp': 810, 'trendschangeoi': [1303, 1320],
                            'trends': [17, -1, -1, -1, -1]},
                     'PE': {'oi': 4274, 'changeinoi': 3680, 'ltp': 479.8, 'trendschangeoi': [3680, 3603],
                            'trends': [-77, -1, -1, -1, -1]}}, 19800: {
                     'CE': {'oi': 2152, 'changeinoi': 2151, 'ltp': 749.25, 'trendschangeoi': [2151, 2250],
                            'trends': [99, -1, -1, -1, -1]},
                     'PE': {'oi': 4257, 'changeinoi': 3784, 'ltp': 518.25, 'trendschangeoi': [3784, 3618],
                            'trends': [-166, -1, -1, -1, -1]}}, 19900: {
                     'CE': {'oi': 1656, 'changeinoi': 1654, 'ltp': 692.9, 'trendschangeoi': [1654, 1730],
                            'trends': [76, -1, -1, -1, -1]},
                     'PE': {'oi': 3586, 'changeinoi': 3261, 'ltp': 563.15, 'trendschangeoi': [3261, 3188],
                            'trends': [-73, -1, -1, -1, -1]}}, 20000: {
                     'CE': {'oi': 10843, 'changeinoi': 9278, 'ltp': 638, 'trendschangeoi': [9278, 9218],
                            'trends': [-60, -1, -1, -1, -1]},
                     'PE': {'oi': 12143, 'changeinoi': 2022, 'ltp': 606, 'trendschangeoi': [2022, 1652],
                            'trends': [-370, -1, -1, -1, -1]}}, 20100: {
                     'CE': {'oi': 1696, 'changeinoi': 1696, 'ltp': 588.55, 'trendschangeoi': [1696, 1596],
                            'trends': [-100, -1, -1, -1, -1]},
                     'PE': {'oi': 1129, 'changeinoi': 708, 'ltp': 657.8, 'trendschangeoi': [708, 637],
                            'trends': [-71, -1, -1, -1, -1]}}, 20200: {
                     'CE': {'oi': 2598, 'changeinoi': 2566, 'ltp': 540.95, 'trendschangeoi': [2566, 2543],
                            'trends': [-23, -1, -1, -1, -1]},
                     'PE': {'oi': 901, 'changeinoi': -11, 'ltp': 703.05, 'trendschangeoi': [-11, -8],
                            'trends': [3, -1, -1, -1, -1]}}, 20300: {
                     'CE': {'oi': 1797, 'changeinoi': 1722, 'ltp': 496, 'trendschangeoi': [1722, 1584],
                            'trends': [-138, -1, -1, -1, -1]},
                     'PE': {'oi': 581, 'changeinoi': -393, 'ltp': 754.05, 'trendschangeoi': [-393, -379],
                            'trends': [14, -1, -1, -1, -1]}}, 20400: {
                     'CE': {'oi': 2033, 'changeinoi': 1907, 'ltp': 451.05, 'trendschangeoi': [1907, 2044],
                            'trends': [137, -1, -1, -1, -1]},
                     'PE': {'oi': 727, 'changeinoi': -12, 'ltp': 814.7, 'trendschangeoi': [-12, -12],
                            'trends': [0, -1, -1, -1, -1]}}, 20500: {
                     'CE': {'oi': 11028, 'changeinoi': 6925, 'ltp': 408.2, 'trendschangeoi': [6925, 6640],
                            'trends': [-285, -1, -1, -1, -1]},
                     'PE': {'oi': 4373, 'changeinoi': -1491, 'ltp': 872, 'trendschangeoi': [-1491, -1548],
                            'trends': [-57, -1, -1, -1, -1]}}, 20600: {
                     'CE': {'oi': 2141, 'changeinoi': 1197, 'ltp': 372.25, 'trendschangeoi': [1197, 1281],
                            'trends': [84, -1, -1, -1, -1]},
                     'PE': {'oi': 424, 'changeinoi': -89, 'ltp': 942.45, 'trendschangeoi': [-89, -162],
                            'trends': [-73, -1, -1, -1, -1]}}, 20700: {
                     'CE': {'oi': 2227, 'changeinoi': 1374, 'ltp': 334.75, 'trendschangeoi': [1374, 1334],
                            'trends': [-40, -1, -1, -1, -1]},
                     'PE': {'oi': 370, 'changeinoi': -40, 'ltp': 994.4, 'trendschangeoi': [-40, -40],
                            'trends': [0, -1, -1, -1, -1]}}, 20800: {
                     'CE': {'oi': 3648, 'changeinoi': 2350, 'ltp': 302.4, 'trendschangeoi': [2350, 2308],
                            'trends': [-42, -1, -1, -1, -1]},
                     'PE': {'oi': 365, 'changeinoi': -115, 'ltp': 1096.55, 'trendschangeoi': [-115, -109],
                            'trends': [6, -1, -1, -1, -1]}}, 20900: {
                     'CE': {'oi': 1888, 'changeinoi': 1376, 'ltp': 274.55, 'trendschangeoi': [1376, 1409],
                            'trends': [33, -1, -1, -1, -1]},
                     'PE': {'oi': 237, 'changeinoi': -47, 'ltp': 1173.6, 'trendschangeoi': [-47, -45],
                            'trends': [2, -1, -1, -1, -1]}}, 21000: {
                     'CE': {'oi': 20894, 'changeinoi': 9973, 'ltp': 245, 'trendschangeoi': [9973, 10221],
                            'trends': [248, -1, -1, -1, -1]},
                     'PE': {'oi': 3823, 'changeinoi': -360, 'ltp': 1210.65, 'trendschangeoi': [-360, -354],
                            'trends': [6, -1, -1, -1, -1]}}, 21100: {
                     'CE': {'oi': 2368, 'changeinoi': 1558, 'ltp': 220, 'trendschangeoi': [1558, 1514],
                            'trends': [-44, -1, -1, -1, -1]},
                     'PE': {'oi': 353, 'changeinoi': -20, 'ltp': 1291.2, 'trendschangeoi': [-20, -20],
                            'trends': [0, -1, -1, -1, -1]}}, 21200: {
                     'CE': {'oi': 2725, 'changeinoi': 1228, 'ltp': 196.8, 'trendschangeoi': [1228, 1453],
                            'trends': [225, -1, -1, -1, -1]},
                     'PE': {'oi': 155, 'changeinoi': -19, 'ltp': 1510.2, 'trendschangeoi': [-19, -19],
                            'trends': [0, -1, -1, -1, -1]}}, 21300: {
                     'CE': {'oi': 2525, 'changeinoi': 1475, 'ltp': 176.35, 'trendschangeoi': [1475, 1510],
                            'trends': [35, -1, -1, -1, -1]},
                     'PE': {'oi': 87, 'changeinoi': 0, 'ltp': 1498.5, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 21400: {
                     'CE': {'oi': 1565, 'changeinoi': 685, 'ltp': 155.4, 'trendschangeoi': [685, 677],
                            'trends': [-8, -1, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': -2, 'ltp': 1308.6, 'trendschangeoi': [-2, -2],
                            'trends': [0, -1, -1, -1, -1]}}, 21500: {
                     'CE': {'oi': 17012, 'changeinoi': 5697, 'ltp': 138.4, 'trendschangeoi': [5697, 5571],
                            'trends': [-126, -1, -1, -1, -1]},
                     'PE': {'oi': 968, 'changeinoi': -478, 'ltp': 1601.15, 'trendschangeoi': [-478, -475],
                            'trends': [3, -1, -1, -1, -1]}}, 21600: {
                     'CE': {'oi': 1996, 'changeinoi': 1302, 'ltp': 123.3, 'trendschangeoi': [1302, 1375],
                            'trends': [73, -1, -1, -1, -1]},
                     'PE': {'oi': 10, 'changeinoi': 2, 'ltp': 1641.1, 'trendschangeoi': [2, 2],
                            'trends': [0, -1, -1, -1, -1]}}, 21700: {
                     'CE': {'oi': 1898, 'changeinoi': 1395, 'ltp': 109.4, 'trendschangeoi': [1395, 1402],
                            'trends': [7, -1, -1, -1, -1]},
                     'PE': {'oi': 13, 'changeinoi': -1, 'ltp': 1959.1, 'trendschangeoi': [-1, -1],
                            'trends': [0, -1, -1, -1, -1]}}, 21800: {
                     'CE': {'oi': 4256, 'changeinoi': 3083, 'ltp': 96.6, 'trendschangeoi': [3083, 3184],
                            'trends': [101, -1, -1, -1, -1]},
                     'PE': {'oi': 2, 'changeinoi': 1, 'ltp': 2140.85, 'trendschangeoi': [1, 1],
                            'trends': [0, -1, -1, -1, -1]}}, 21900: {
                     'CE': {'oi': 1409, 'changeinoi': 996, 'ltp': 85.9, 'trendschangeoi': [996, 957],
                            'trends': [-39, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22000: {
                     'CE': {'oi': 20080, 'changeinoi': 9052, 'ltp': 76.1, 'trendschangeoi': [9052, 8904],
                            'trends': [-148, -1, -1, -1, -1]},
                     'PE': {'oi': 355, 'changeinoi': -19, 'ltp': 2004.9, 'trendschangeoi': [-19, -20],
                            'trends': [-1, -1, -1, -1, -1]}}, 22100: {
                     'CE': {'oi': 856, 'changeinoi': 588, 'ltp': 67.4, 'trendschangeoi': [588, 639],
                            'trends': [51, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22200: {
                     'CE': {'oi': 1186, 'changeinoi': 686, 'ltp': 59.35, 'trendschangeoi': [686, 710],
                            'trends': [24, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22300: {
                     'CE': {'oi': 805, 'changeinoi': 615, 'ltp': 52.5, 'trendschangeoi': [615, 634],
                            'trends': [19, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22400: {
                     'CE': {'oi': 795, 'changeinoi': 484, 'ltp': 46.65, 'trendschangeoi': [484, 473],
                            'trends': [-11, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22500: {
                     'CE': {'oi': 12837, 'changeinoi': 4756, 'ltp': 41.25, 'trendschangeoi': [4756, 4640],
                            'trends': [-116, -1, -1, -1, -1]},
                     'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22600: {
                     'CE': {'oi': 1098, 'changeinoi': 455, 'ltp': 36.85, 'trendschangeoi': [455, 445],
                            'trends': [-10, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22700: {
                     'CE': {'oi': 689, 'changeinoi': 493, 'ltp': 33.1, 'trendschangeoi': [493, 485],
                            'trends': [-8, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22800: {
                     'CE': {'oi': 728, 'changeinoi': 437, 'ltp': 28.65, 'trendschangeoi': [437, 435],
                            'trends': [-2, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 22900: {
                     'CE': {'oi': 688, 'changeinoi': 374, 'ltp': 25.35, 'trendschangeoi': [374, 376],
                            'trends': [2, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23000: {
                     'CE': {'oi': 13043, 'changeinoi': 2249, 'ltp': 22, 'trendschangeoi': [2249, 2525],
                            'trends': [276, -1, -1, -1, -1]},
                     'PE': {'oi': 33, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23100: {
                     'CE': {'oi': 351, 'changeinoi': 241, 'ltp': 20.95, 'trendschangeoi': [241, 240],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23200: {
                     'CE': {'oi': 756, 'changeinoi': 159, 'ltp': 16.5, 'trendschangeoi': [159, 157],
                            'trends': [-2, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23300: {
                     'CE': {'oi': 22, 'changeinoi': 22, 'ltp': 14, 'trendschangeoi': [22, 17],
                            'trends': [-5, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23400: {
                     'CE': {'oi': 193, 'changeinoi': 67, 'ltp': 12.95, 'trendschangeoi': [67, 70],
                            'trends': [3, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23500: {
                     'CE': {'oi': 8813, 'changeinoi': 2870, 'ltp': 11.8, 'trendschangeoi': [2870, 2758],
                            'trends': [-112, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23600: {
                     'CE': {'oi': 121, 'changeinoi': 106, 'ltp': 11, 'trendschangeoi': [106, 107],
                            'trends': [1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23700: {
                     'CE': {'oi': 124, 'changeinoi': 124, 'ltp': 11, 'trendschangeoi': [124, 124],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23800: {
                     'CE': {'oi': 307, 'changeinoi': 176, 'ltp': 9.2, 'trendschangeoi': [176, 171],
                            'trends': [-5, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 23900: {
                     'CE': {'oi': 409, 'changeinoi': 213, 'ltp': 9.4, 'trendschangeoi': [213, 206],
                            'trends': [-7, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24000: {
                     'CE': {'oi': 5601, 'changeinoi': 1234, 'ltp': 7.35, 'trendschangeoi': [1234, 1267],
                            'trends': [33, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24100: {
                     'CE': {'oi': 47, 'changeinoi': 38, 'ltp': 6.3, 'trendschangeoi': [38, 38],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24200: {
                     'CE': {'oi': 59, 'changeinoi': 34, 'ltp': 6.75, 'trendschangeoi': [34, 34],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24300: {
                     'CE': {'oi': 56, 'changeinoi': 16, 'ltp': 6.85, 'trendschangeoi': [16, 16],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24400: {
                     'CE': {'oi': 172, 'changeinoi': -61, 'ltp': 6.15, 'trendschangeoi': [-61, -61],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}, 24500: {
                     'CE': {'oi': 5363, 'changeinoi': 949, 'ltp': 5.8, 'trendschangeoi': [949, 945],
                            'trends': [-4, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0],
                            'trends': [0, -1, -1, -1, -1]}}}],
                [{'index': 'NIFTY', 'marketstatus': True, 'time': '13:10:26', 'date': '12-Jun-2020', 'price': 9752.85,
                  'turnoverprice': 9750, 7300: {'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                                                       'trends': [0, 0, -1, -1, -1]},
                                                'PE': {'oi': 75, 'changeinoi': 49, 'ltp': 0.65,
                                                       'trendschangeoi': [49, 53, 52], 'trends': [4, 3, -1, -1, -1]}},
                  7350: {'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                                'trends': [0, 0, -1, -1, -1]},
                         'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 1.7, 'trendschangeoi': [1, 1, 1],
                                'trends': [0, 0, -1, -1, -1]}}, 7400: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 1.15, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7450: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0.75, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7500: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 834, 'changeinoi': 829, 'ltp': 1.3, 'trendschangeoi': [829, 830, 830],
                               'trends': [1, 1, -1, -1, -1]}}, 7550: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7600: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7650: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7700: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7750: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7800: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 2.9, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7850: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 7900: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 14, 'changeinoi': 14, 'ltp': 1.8, 'trendschangeoi': [14, 8, 8],
                               'trends': [-6, -6, -1, -1, -1]}}, 7950: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8000: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 3634, 'changeinoi': 1741, 'ltp': 1.95, 'trendschangeoi': [1741, 1760, 1781],
                               'trends': [19, 40, -1, -1, -1]}}, 8050: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8100: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8150: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8200: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8250: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8300: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 302, 'changeinoi': 302, 'ltp': 3, 'trendschangeoi': [302, 303, 306],
                               'trends': [1, 4, -1, -1, -1]}}, 8350: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8400: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 739, 'changeinoi': 737, 'ltp': 4, 'trendschangeoi': [737, 735, 734],
                               'trends': [-2, -3, -1, -1, -1]}}, 8450: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8500: {
                        'CE': {'oi': 7, 'changeinoi': 1, 'ltp': 1224.95, 'trendschangeoi': [1, 0, 0],
                               'trends': [-1, -1, -1, -1, -1]},
                        'PE': {'oi': 7708, 'changeinoi': 3782, 'ltp': 5.05, 'trendschangeoi': [3782, 3750, 3755],
                               'trends': [-32, -27, -1, -1, -1]}}, 8550: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8600: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 3062, 'changeinoi': 2997, 'ltp': 6.55, 'trendschangeoi': [2997, 3107, 3121],
                               'trends': [110, 124, -1, -1, -1]}}, 8650: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8700: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1000, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 4355, 'changeinoi': 3973, 'ltp': 8.6, 'trendschangeoi': [3973, 4026, 3881],
                               'trends': [53, -92, -1, -1, -1]}}, 8750: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 8800: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 4908, 'changeinoi': 3535, 'ltp': 11.4, 'trendschangeoi': [3535, 3511, 3585],
                               'trends': [-24, 50, -1, -1, -1]}}, 8850: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 25, 'changeinoi': 22, 'ltp': 13.2, 'trendschangeoi': [22, 22, 23],
                               'trends': [0, 1, -1, -1, -1]}}, 8900: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 3872, 'changeinoi': 2553, 'ltp': 15.1, 'trendschangeoi': [2553, 2555, 2560],
                               'trends': [2, 7, -1, -1, -1]}}, 8950: {
                        'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 419, 'changeinoi': 411, 'ltp': 17.5, 'trendschangeoi': [411, 396, 398],
                               'trends': [-15, -13, -1, -1, -1]}}, 9000: {
                        'CE': {'oi': 212, 'changeinoi': 187, 'ltp': 749, 'trendschangeoi': [187, 183, 183],
                               'trends': [-4, -4, -1, -1, -1]},
                        'PE': {'oi': 25340, 'changeinoi': 11515, 'ltp': 20.05, 'trendschangeoi': [11515, 11047, 11132],
                               'trends': [-468, -383, -1, -1, -1]}}, 9050: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 645.4, 'trendschangeoi': [1, 1, 1],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 819, 'changeinoi': 786, 'ltp': 23.4, 'trendschangeoi': [786, 795, 794],
                               'trends': [9, 8, -1, -1, -1]}}, 9100: {
                        'CE': {'oi': 88, 'changeinoi': 1, 'ltp': 693.9, 'trendschangeoi': [1, 1, 1],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 7985, 'changeinoi': 4302, 'ltp': 27.25, 'trendschangeoi': [4302, 4385, 4383],
                               'trends': [83, 81, -1, -1, -1]}}, 9150: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 648.8, 'trendschangeoi': [1, 1, 1],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 1009, 'changeinoi': 949, 'ltp': 31.35, 'trendschangeoi': [949, 928, 927],
                               'trends': [-21, -22, -1, -1, -1]}}, 9200: {
                        'CE': {'oi': 68, 'changeinoi': 45, 'ltp': 548.6, 'trendschangeoi': [45, 45, 45],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 13295, 'changeinoi': 7732, 'ltp': 36.4, 'trendschangeoi': [7732, 7768, 7697],
                               'trends': [36, -35, -1, -1, -1]}}, 9250: {
                        'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 540.7, 'trendschangeoi': [1, 1, 1],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 1315, 'changeinoi': 872, 'ltp': 42.15, 'trendschangeoi': [872, 888, 876],
                               'trends': [16, 4, -1, -1, -1]}}, 9300: {
                        'CE': {'oi': 435, 'changeinoi': -17, 'ltp': 498.45, 'trendschangeoi': [-17, -17, -17],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 19680, 'changeinoi': 11593, 'ltp': 49.1, 'trendschangeoi': [11593, 11370, 11672],
                               'trends': [-223, 79, -1, -1, -1]}}, 9350: {
                        'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 420.3, 'trendschangeoi': [5, 5, 5],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 1699, 'changeinoi': 1419, 'ltp': 56.3, 'trendschangeoi': [1419, 1423, 1401],
                               'trends': [4, -18, -1, -1, -1]}}, 9400: {
                        'CE': {'oi': 464, 'changeinoi': 310, 'ltp': 399, 'trendschangeoi': [310, 320, 321],
                               'trends': [10, 11, -1, -1, -1]},
                        'PE': {'oi': 19422, 'changeinoi': 12233, 'ltp': 65.25, 'trendschangeoi': [12233, 12195, 12041],
                               'trends': [-38, -192, -1, -1, -1]}}, 9450: {
                        'CE': {'oi': 38, 'changeinoi': 37, 'ltp': 359.5, 'trendschangeoi': [37, 37, 37],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 1719, 'changeinoi': 1128, 'ltp': 75, 'trendschangeoi': [1128, 1096, 1137],
                               'trends': [-32, 9, -1, -1, -1]}}, 9500: {
                        'CE': {'oi': 3015, 'changeinoi': 1684, 'ltp': 320.05, 'trendschangeoi': [1684, 1710, 1764],
                               'trends': [26, 80, -1, -1, -1]},
                        'PE': {'oi': 27404, 'changeinoi': 11101, 'ltp': 86.2, 'trendschangeoi': [11101, 11157, 10920],
                               'trends': [56, -181, -1, -1, -1]}}, 9550: {
                        'CE': {'oi': 127, 'changeinoi': 124, 'ltp': 284.3, 'trendschangeoi': [124, 131, 155],
                               'trends': [7, 31, -1, -1, -1]},
                        'PE': {'oi': 2053, 'changeinoi': 1614, 'ltp': 99.9, 'trendschangeoi': [1614, 1565, 1622],
                               'trends': [-49, 8, -1, -1, -1]}}, 9600: {
                        'CE': {'oi': 4817, 'changeinoi': 4501, 'ltp': 248.2, 'trendschangeoi': [4501, 4593, 4638],
                               'trends': [92, 137, -1, -1, -1]},
                        'PE': {'oi': 20040, 'changeinoi': 10836, 'ltp': 114.2, 'trendschangeoi': [10836, 10785, 10739],
                               'trends': [-51, -97, -1, -1, -1]}}, 9650: {
                        'CE': {'oi': 1008, 'changeinoi': 1003, 'ltp': 214.3, 'trendschangeoi': [1003, 1000, 1026],
                               'trends': [-3, 23, -1, -1, -1]},
                        'PE': {'oi': 2597, 'changeinoi': 1866, 'ltp': 131.25, 'trendschangeoi': [1866, 2005, 1985],
                               'trends': [139, 119, -1, -1, -1]}}, 9700: {
                        'CE': {'oi': 12059, 'changeinoi': 11288, 'ltp': 184.15, 'trendschangeoi': [11288, 11305, 11421],
                               'trends': [17, 133, -1, -1, -1]},
                        'PE': {'oi': 18991, 'changeinoi': 9498, 'ltp': 150.5, 'trendschangeoi': [9498, 9452, 9555],
                               'trends': [-46, 57, -1, -1, -1]}}, 9750: {
                        'CE': {'oi': 2168, 'changeinoi': 2164, 'ltp': 156.35, 'trendschangeoi': [2164, 2202, 2108],
                               'trends': [38, -56, -1, -1, -1]},
                        'PE': {'oi': 2339, 'changeinoi': 1059, 'ltp': 172, 'trendschangeoi': [1059, 994, 847],
                               'trends': [-65, -212, -1, -1, -1]}}, 9800: {
                        'CE': {'oi': 17414, 'changeinoi': 14054, 'ltp': 131.2, 'trendschangeoi': [14054, 14114, 14332],
                               'trends': [60, 278, -1, -1, -1]},
                        'PE': {'oi': 9261, 'changeinoi': -1546, 'ltp': 197.05, 'trendschangeoi': [-1546, -1610, -1580],
                               'trends': [-64, -34, -1, -1, -1]}}, 9850: {
                        'CE': {'oi': 1309, 'changeinoi': 1205, 'ltp': 108.65, 'trendschangeoi': [1205, 1197, 1225],
                               'trends': [-8, 20, -1, -1, -1]},
                        'PE': {'oi': 902, 'changeinoi': -4, 'ltp': 224.5, 'trendschangeoi': [-4, -1, 29],
                               'trends': [3, 33, -1, -1, -1]}}, 9900: {
                        'CE': {'oi': 22177, 'changeinoi': 13814, 'ltp': 88.35, 'trendschangeoi': [13814, 14029, 14108],
                               'trends': [215, 294, -1, -1, -1]},
                        'PE': {'oi': 6410, 'changeinoi': -3745, 'ltp': 253.5, 'trendschangeoi': [-3745, -3774, -3808],
                               'trends': [-29, -63, -1, -1, -1]}}, 9950: {
                        'CE': {'oi': 2199, 'changeinoi': 1344, 'ltp': 71.5, 'trendschangeoi': [1344, 1428, 1476],
                               'trends': [84, 132, -1, -1, -1]},
                        'PE': {'oi': 473, 'changeinoi': -274, 'ltp': 290.75, 'trendschangeoi': [-274, -269, -268],
                               'trends': [5, 6, -1, -1, -1]}}, 10000: {
                        'CE': {'oi': 27314, 'changeinoi': 13989, 'ltp': 56.8, 'trendschangeoi': [13989, 13998, 14047],
                               'trends': [9, 58, -1, -1, -1]},
                        'PE': {'oi': 7214, 'changeinoi': -727, 'ltp': 320.65, 'trendschangeoi': [-727, -686, -652],
                               'trends': [41, 75, -1, -1, -1]}}, 10050: {
                        'CE': {'oi': 3278, 'changeinoi': 1467, 'ltp': 44.55, 'trendschangeoi': [1467, 1394, 1442],
                               'trends': [-73, -25, -1, -1, -1]},
                        'PE': {'oi': 668, 'changeinoi': -55, 'ltp': 365.75, 'trendschangeoi': [-55, -60, -59],
                               'trends': [-5, -4, -1, -1, -1]}}, 10100: {
                        'CE': {'oi': 16946, 'changeinoi': 2840, 'ltp': 34.8, 'trendschangeoi': [2840, 2804, 2777],
                               'trends': [-36, -63, -1, -1, -1]},
                        'PE': {'oi': 4055, 'changeinoi': -355, 'ltp': 398.85, 'trendschangeoi': [-355, -369, -379],
                               'trends': [-14, -24, -1, -1, -1]}}, 10150: {
                        'CE': {'oi': 4860, 'changeinoi': 3113, 'ltp': 26.85, 'trendschangeoi': [3113, 2948, 2969],
                               'trends': [-165, -144, -1, -1, -1]},
                        'PE': {'oi': 181, 'changeinoi': -38, 'ltp': 427.1, 'trendschangeoi': [-38, -38, -38],
                               'trends': [0, 0, -1, -1, -1]}}, 10200: {
                        'CE': {'oi': 16714, 'changeinoi': 2769, 'ltp': 21.25, 'trendschangeoi': [2769, 2720, 2780],
                               'trends': [-49, 11, -1, -1, -1]},
                        'PE': {'oi': 1029, 'changeinoi': -210, 'ltp': 488.85, 'trendschangeoi': [-210, -212, -212],
                               'trends': [-2, -2, -1, -1, -1]}}, 10250: {
                        'CE': {'oi': 2153, 'changeinoi': 679, 'ltp': 16.6, 'trendschangeoi': [679, 620, 578],
                               'trends': [-59, -101, -1, -1, -1]},
                        'PE': {'oi': 93, 'changeinoi': -17, 'ltp': 505.85, 'trendschangeoi': [-17, -17, -17],
                               'trends': [0, 0, -1, -1, -1]}}, 10300: {
                        'CE': {'oi': 18281, 'changeinoi': 4215, 'ltp': 13.3, 'trendschangeoi': [4215, 4116, 4187],
                               'trends': [-99, -28, -1, -1, -1]},
                        'PE': {'oi': 894, 'changeinoi': -245, 'ltp': 583.9, 'trendschangeoi': [-245, -246, -246],
                               'trends': [-1, -1, -1, -1, -1]}}, 10350: {
                        'CE': {'oi': 1447, 'changeinoi': 330, 'ltp': 10.75, 'trendschangeoi': [330, 285, 296],
                               'trends': [-45, -34, -1, -1, -1]},
                        'PE': {'oi': 31, 'changeinoi': -10, 'ltp': 614, 'trendschangeoi': [-10, -10, -10],
                               'trends': [0, 0, -1, -1, -1]}}, 10400: {
                        'CE': {'oi': 13621, 'changeinoi': 2111, 'ltp': 9, 'trendschangeoi': [2111, 1963, 2002],
                               'trends': [-148, -109, -1, -1, -1]},
                        'PE': {'oi': 165, 'changeinoi': -13, 'ltp': 686.55, 'trendschangeoi': [-13, -13, -14],
                               'trends': [0, -1, -1, -1, -1]}}, 10450: {
                        'CE': {'oi': 811, 'changeinoi': 27, 'ltp': 7.6, 'trendschangeoi': [27, 25, 1],
                               'trends': [-2, -26, -1, -1, -1]},
                        'PE': {'oi': 7, 'changeinoi': 0, 'ltp': 732.7, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10500: {
                        'CE': {'oi': 26433, 'changeinoi': 7507, 'ltp': 6.4, 'trendschangeoi': [7507, 7426, 7328],
                               'trends': [-81, -179, -1, -1, -1]},
                        'PE': {'oi': 647, 'changeinoi': -3, 'ltp': 749.5, 'trendschangeoi': [-3, -3, -3],
                               'trends': [0, 0, -1, -1, -1]}}, 10550: {
                        'CE': {'oi': 805, 'changeinoi': 16, 'ltp': 5.45, 'trendschangeoi': [16, 29, 17],
                               'trends': [13, 1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10600: {
                        'CE': {'oi': 11641, 'changeinoi': 2110, 'ltp': 4.45, 'trendschangeoi': [2110, 2072, 2005],
                               'trends': [-38, -105, -1, -1, -1]},
                        'PE': {'oi': 49, 'changeinoi': -1, 'ltp': 889.45, 'trendschangeoi': [-1, -1, -1],
                               'trends': [0, 0, -1, -1, -1]}}, 10650: {
                        'CE': {'oi': 812, 'changeinoi': 391, 'ltp': 3.95, 'trendschangeoi': [391, 391, 404],
                               'trends': [0, 13, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10700: {
                        'CE': {'oi': 7777, 'changeinoi': 32, 'ltp': 3.1, 'trendschangeoi': [32, 46, 97],
                               'trends': [14, 65, -1, -1, -1]},
                        'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 934.65, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10750: {
                        'CE': {'oi': 435, 'changeinoi': 19, 'ltp': 2.8, 'trendschangeoi': [19, 17, 16],
                               'trends': [-2, -3, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10800: {
                        'CE': {'oi': 5121, 'changeinoi': -945, 'ltp': 2.2, 'trendschangeoi': [-945, -951, -1010],
                               'trends': [-6, -65, -1, -1, -1]},
                        'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 1110.4, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10850: {
                        'CE': {'oi': 103, 'changeinoi': 26, 'ltp': 1.8, 'trendschangeoi': [26, 27, 27],
                               'trends': [1, 1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10900: {
                        'CE': {'oi': 2331, 'changeinoi': -349, 'ltp': 1.65, 'trendschangeoi': [-349, -386, -419],
                               'trends': [-37, -70, -1, -1, -1]},
                        'PE': {'oi': 1, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 10950: {
                        'CE': {'oi': 145, 'changeinoi': 103, 'ltp': 1.5, 'trendschangeoi': [103, 102, 102],
                               'trends': [-1, -1, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11000: {
                        'CE': {'oi': 12907, 'changeinoi': -158, 'ltp': 1.4, 'trendschangeoi': [-158, -290, -460],
                               'trends': [-132, -302, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11050: {
                        'CE': {'oi': 71, 'changeinoi': 21, 'ltp': 1.5, 'trendschangeoi': [21, 21, 21],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11100: {
                        'CE': {'oi': 658, 'changeinoi': -242, 'ltp': 1.2, 'trendschangeoi': [-242, -243, -244],
                               'trends': [-1, -2, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11150: {
                        'CE': {'oi': 49, 'changeinoi': 7, 'ltp': 1.1, 'trendschangeoi': [7, 7, 7],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11200: {
                        'CE': {'oi': 1752, 'changeinoi': 129, 'ltp': 0.9, 'trendschangeoi': [129, 126, 111],
                               'trends': [-3, -18, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11250: {
                        'CE': {'oi': 16, 'changeinoi': 14, 'ltp': 1, 'trendschangeoi': [14, 14, 14],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11300: {
                        'CE': {'oi': 179, 'changeinoi': -8, 'ltp': 0.9, 'trendschangeoi': [-8, -8, -8],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 2, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11350: {
                        'CE': {'oi': 7, 'changeinoi': 5, 'ltp': 1.1, 'trendschangeoi': [5, 5, 5],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11400: {
                        'CE': {'oi': 101, 'changeinoi': 7, 'ltp': 0.8, 'trendschangeoi': [7, 7, 7],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11450: {
                        'CE': {'oi': 34, 'changeinoi': 4, 'ltp': 0.75, 'trendschangeoi': [4, 4, 4],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11500: {
                        'CE': {'oi': 2637, 'changeinoi': 407, 'ltp': 0.7, 'trendschangeoi': [407, 367, 367],
                               'trends': [-40, -40, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11550: {
                        'CE': {'oi': 4, 'changeinoi': 3, 'ltp': 0.5, 'trendschangeoi': [3, 3, 3],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11600: {
                        'CE': {'oi': 41, 'changeinoi': 17, 'ltp': 0.6, 'trendschangeoi': [17, 17, 15],
                               'trends': [0, -2, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}, 11650: {
                        'CE': {'oi': 162, 'changeinoi': 108, 'ltp': 0.7, 'trendschangeoi': [108, 108, 108],
                               'trends': [0, 0, -1, -1, -1]},
                        'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                               'trends': [0, 0, -1, -1, -1]}}},
                 {'index': 'BANK NIFTY', 'marketstatus': True, 'time': '13:09:56', 'date': '12-Jun-2020',
                  'price': 19986.45, 'turnoverprice': 19950, 14300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 2587, 'changeinoi': 2506, 'ltp': 6.35, 'trendschangeoi': [2506, 2500, 2484],
                            'trends': [-6, -22, -1, -1, -1]}}, 14400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 14500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1, 'changeinoi': 1, 'ltp': 3.05, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]}}, 14600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 14700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 14800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 14900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 408, 'changeinoi': 408, 'ltp': 7.95, 'trendschangeoi': [408, 424, 430],
                            'trends': [16, 22, -1, -1, -1]}}, 15100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 9, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 875, 'changeinoi': 875, 'ltp': 10.6, 'trendschangeoi': [875, 928, 946],
                            'trends': [53, 71, -1, -1, -1]}}, 15600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 15900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16000: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 4197.3, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 7326, 'changeinoi': 6173, 'ltp': 15.65, 'trendschangeoi': [6173, 6123, 6079],
                            'trends': [-50, -94, -1, -1, -1]}}, 16100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 13, 'changeinoi': 13, 'ltp': 19, 'trendschangeoi': [13, 13, 13],
                            'trends': [0, 0, -1, -1, -1]}}, 16300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16500: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3384.9, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 4731, 'changeinoi': 4029, 'ltp': 24.8, 'trendschangeoi': [4029, 3973, 3890],
                            'trends': [-56, -139, -1, -1, -1]}}, 16600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 26, 'changeinoi': 26, 'ltp': 29.6, 'trendschangeoi': [26, 25, 25],
                            'trends': [-1, -1, -1, -1, -1]}}, 16800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 16900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 45, 'changeinoi': 45, 'ltp': 37, 'trendschangeoi': [45, 45, 45],
                            'trends': [0, 0, -1, -1, -1]}}, 17000: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 3200, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 9849, 'changeinoi': 8015, 'ltp': 40.8, 'trendschangeoi': [8015, 7913, 7823],
                            'trends': [-102, -192, -1, -1, -1]}}, 17100: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': 25, 'ltp': 43.7, 'trendschangeoi': [25, 25, 25],
                            'trends': [0, 0, -1, -1, -1]}}, 17200: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 78, 'changeinoi': 78, 'ltp': 50.5, 'trendschangeoi': [78, 71, 70],
                            'trends': [-7, -8, -1, -1, -1]}}, 17300: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 11, 'changeinoi': 11, 'ltp': 56.1, 'trendschangeoi': [11, 18, 18],
                            'trends': [7, 7, -1, -1, -1]}}, 17400: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 302, 'changeinoi': 292, 'ltp': 61.95, 'trendschangeoi': [292, 275, 276],
                            'trends': [-17, -16, -1, -1, -1]}}, 17500: {
                     'CE': {'oi': 5, 'changeinoi': 2, 'ltp': 2350.35, 'trendschangeoi': [2, 2, 2],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 10525, 'changeinoi': 8935, 'ltp': 66.8, 'trendschangeoi': [8935, 9009, 8928],
                            'trends': [74, -7, -1, -1, -1]}}, 17600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 277, 'changeinoi': 277, 'ltp': 73.4, 'trendschangeoi': [277, 285, 295],
                            'trends': [8, 18, -1, -1, -1]}}, 17700: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 2266.3, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 721, 'changeinoi': 669, 'ltp': 80.6, 'trendschangeoi': [669, 662, 674],
                            'trends': [-7, 5, -1, -1, -1]}}, 17800: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1748, 'changeinoi': 1645, 'ltp': 89.65, 'trendschangeoi': [1645, 1646, 1607],
                            'trends': [1, -38, -1, -1, -1]}}, 17900: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 323, 'changeinoi': 323, 'ltp': 98, 'trendschangeoi': [323, 297, 310],
                            'trends': [-26, -13, -1, -1, -1]}}, 18000: {
                     'CE': {'oi': 79, 'changeinoi': 22, 'ltp': 2150, 'trendschangeoi': [22, 22, 21],
                            'trends': [0, -1, -1, -1, -1]},
                     'PE': {'oi': 17309, 'changeinoi': 11386, 'ltp': 108.9, 'trendschangeoi': [11386, 11393, 11320],
                            'trends': [7, -66, -1, -1, -1]}}, 18100: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 2217.05, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1425, 'changeinoi': 1224, 'ltp': 118.35, 'trendschangeoi': [1224, 1139, 1128],
                            'trends': [-85, -96, -1, -1, -1]}}, 18200: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1824, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1981, 'changeinoi': 1884, 'ltp': 131.5, 'trendschangeoi': [1884, 1876, 1794],
                            'trends': [-8, -90, -1, -1, -1]}}, 18300: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1620.9, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 852, 'changeinoi': 838, 'ltp': 144.4, 'trendschangeoi': [838, 851, 882],
                            'trends': [13, 44, -1, -1, -1]}}, 18400: {
                     'CE': {'oi': 11, 'changeinoi': 11, 'ltp': 1779.75, 'trendschangeoi': [11, 11, 11],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1717, 'changeinoi': 1643, 'ltp': 156.9, 'trendschangeoi': [1643, 1615, 1618],
                            'trends': [-28, -25, -1, -1, -1]}}, 18500: {
                     'CE': {'oi': 154, 'changeinoi': 67, 'ltp': 1636.25, 'trendschangeoi': [67, 67, 67],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 15930, 'changeinoi': 10129, 'ltp': 171.15, 'trendschangeoi': [10129, 10018, 9688],
                            'trends': [-111, -441, -1, -1, -1]}}, 18600: {
                     'CE': {'oi': 0, 'changeinoi': 0, 'ltp': 1663.4, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1370, 'changeinoi': 1280, 'ltp': 190.1, 'trendschangeoi': [1280, 1242, 1233],
                            'trends': [-38, -47, -1, -1, -1]}}, 18700: {
                     'CE': {'oi': 2, 'changeinoi': 2, 'ltp': 1534.45, 'trendschangeoi': [2, 2, 2],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1353, 'changeinoi': 1117, 'ltp': 208.3, 'trendschangeoi': [1117, 1109, 1110],
                            'trends': [-8, -7, -1, -1, -1]}}, 18800: {
                     'CE': {'oi': 5, 'changeinoi': 5, 'ltp': 1558.95, 'trendschangeoi': [5, 5, 5],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 2294, 'changeinoi': 1837, 'ltp': 228.9, 'trendschangeoi': [1837, 1906, 1868],
                            'trends': [69, 31, -1, -1, -1]}}, 18900: {
                     'CE': {'oi': 1, 'changeinoi': 1, 'ltp': 1250, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1638, 'changeinoi': 1358, 'ltp': 250.3, 'trendschangeoi': [1358, 1319, 1301],
                            'trends': [-39, -57, -1, -1, -1]}}, 19000: {
                     'CE': {'oi': 973, 'changeinoi': 731, 'ltp': 1225, 'trendschangeoi': [731, 735, 747],
                            'trends': [4, 16, -1, -1, -1]},
                     'PE': {'oi': 24767, 'changeinoi': 12674, 'ltp': 275, 'trendschangeoi': [12674, 12878, 12026],
                            'trends': [204, -648, -1, -1, -1]}}, 19100: {
                     'CE': {'oi': 9, 'changeinoi': 9, 'ltp': 1355.8, 'trendschangeoi': [9, 9, 9],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 1713, 'changeinoi': 1604, 'ltp': 301, 'trendschangeoi': [1604, 1655, 1615],
                            'trends': [51, 11, -1, -1, -1]}}, 19200: {
                     'CE': {'oi': 34, 'changeinoi': 34, 'ltp': 1140.8, 'trendschangeoi': [34, 34, 34],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 4602, 'changeinoi': 4436, 'ltp': 329.15, 'trendschangeoi': [4436, 4593, 4520],
                            'trends': [157, 84, -1, -1, -1]}}, 19300: {
                     'CE': {'oi': 37, 'changeinoi': 37, 'ltp': 1020, 'trendschangeoi': [37, 38, 38],
                            'trends': [1, 1, -1, -1, -1]},
                     'PE': {'oi': 3670, 'changeinoi': 3302, 'ltp': 358, 'trendschangeoi': [3302, 3278, 3231],
                            'trends': [-24, -71, -1, -1, -1]}}, 19400: {
                     'CE': {'oi': 52, 'changeinoi': 52, 'ltp': 945, 'trendschangeoi': [52, 46, 56],
                            'trends': [-6, 4, -1, -1, -1]},
                     'PE': {'oi': 2174, 'changeinoi': 1666, 'ltp': 391.85, 'trendschangeoi': [1666, 1499, 1468],
                            'trends': [-167, -198, -1, -1, -1]}}, 19500: {
                     'CE': {'oi': 3478, 'changeinoi': 3266, 'ltp': 897.65, 'trendschangeoi': [3266, 3241, 3245],
                            'trends': [-25, -21, -1, -1, -1]},
                     'PE': {'oi': 16422, 'changeinoi': 2624, 'ltp': 425.95, 'trendschangeoi': [2624, 2953, 2830],
                            'trends': [329, 206, -1, -1, -1]}}, 19600: {
                     'CE': {'oi': 465, 'changeinoi': 464, 'ltp': 828.85, 'trendschangeoi': [464, 484, 463],
                            'trends': [20, -1, -1, -1, -1]},
                     'PE': {'oi': 2281, 'changeinoi': 2093, 'ltp': 463.55, 'trendschangeoi': [2093, 2099, 2103],
                            'trends': [6, 10, -1, -1, -1]}}, 19700: {
                     'CE': {'oi': 1278, 'changeinoi': 1278, 'ltp': 771.4, 'trendschangeoi': [1278, 1303, 1320],
                            'trends': [25, 42, -1, -1, -1]},
                     'PE': {'oi': 4306, 'changeinoi': 3712, 'ltp': 500, 'trendschangeoi': [3712, 3680, 3603],
                            'trends': [-32, -109, -1, -1, -1]}}, 19800: {
                     'CE': {'oi': 2142, 'changeinoi': 2141, 'ltp': 713.05, 'trendschangeoi': [2141, 2151, 2250],
                            'trends': [10, 109, -1, -1, -1]},
                     'PE': {'oi': 4233, 'changeinoi': 3760, 'ltp': 545.1, 'trendschangeoi': [3760, 3784, 3618],
                            'trends': [24, -142, -1, -1, -1]}}, 19900: {
                     'CE': {'oi': 1712, 'changeinoi': 1710, 'ltp': 660, 'trendschangeoi': [1710, 1654, 1730],
                            'trends': [-56, 20, -1, -1, -1]},
                     'PE': {'oi': 3094, 'changeinoi': 2769, 'ltp': 590.75, 'trendschangeoi': [2769, 3261, 3188],
                            'trends': [492, 419, -1, -1, -1]}}, 20000: {
                     'CE': {'oi': 10939, 'changeinoi': 9374, 'ltp': 605, 'trendschangeoi': [9374, 9278, 9218],
                            'trends': [-96, -156, -1, -1, -1]},
                     'PE': {'oi': 12011, 'changeinoi': 1890, 'ltp': 634.6, 'trendschangeoi': [1890, 2022, 1652],
                            'trends': [132, -238, -1, -1, -1]}}, 20100: {
                     'CE': {'oi': 1551, 'changeinoi': 1551, 'ltp': 557.95, 'trendschangeoi': [1551, 1696, 1596],
                            'trends': [145, 45, -1, -1, -1]},
                     'PE': {'oi': 1181, 'changeinoi': 760, 'ltp': 684.9, 'trendschangeoi': [760, 708, 637],
                            'trends': [-52, -123, -1, -1, -1]}}, 20200: {
                     'CE': {'oi': 2535, 'changeinoi': 2503, 'ltp': 513.35, 'trendschangeoi': [2503, 2566, 2543],
                            'trends': [63, 40, -1, -1, -1]},
                     'PE': {'oi': 888, 'changeinoi': -24, 'ltp': 739.65, 'trendschangeoi': [-24, -11, -8],
                            'trends': [13, 16, -1, -1, -1]}}, 20300: {
                     'CE': {'oi': 1819, 'changeinoi': 1744, 'ltp': 467.6, 'trendschangeoi': [1744, 1722, 1584],
                            'trends': [-22, -160, -1, -1, -1]},
                     'PE': {'oi': 581, 'changeinoi': -393, 'ltp': 804.1, 'trendschangeoi': [-393, -393, -379],
                            'trends': [0, 14, -1, -1, -1]}}, 20400: {
                     'CE': {'oi': 2021, 'changeinoi': 1895, 'ltp': 425.8, 'trendschangeoi': [1895, 1907, 2044],
                            'trends': [12, 149, -1, -1, -1]},
                     'PE': {'oi': 728, 'changeinoi': -11, 'ltp': 841.55, 'trendschangeoi': [-11, -12, -12],
                            'trends': [-1, -1, -1, -1, -1]}}, 20500: {
                     'CE': {'oi': 10817, 'changeinoi': 6714, 'ltp': 384.3, 'trendschangeoi': [6714, 6925, 6640],
                            'trends': [211, -74, -1, -1, -1]},
                     'PE': {'oi': 4355, 'changeinoi': -1509, 'ltp': 912, 'trendschangeoi': [-1509, -1491, -1548],
                            'trends': [18, -39, -1, -1, -1]}}, 20600: {
                     'CE': {'oi': 2188, 'changeinoi': 1244, 'ltp': 346.9, 'trendschangeoi': [1244, 1197, 1281],
                            'trends': [-47, 37, -1, -1, -1]},
                     'PE': {'oi': 427, 'changeinoi': -86, 'ltp': 999.7, 'trendschangeoi': [-86, -89, -162],
                            'trends': [-3, -76, -1, -1, -1]}}, 20700: {
                     'CE': {'oi': 2235, 'changeinoi': 1382, 'ltp': 315.25, 'trendschangeoi': [1382, 1374, 1334],
                            'trends': [-8, -48, -1, -1, -1]},
                     'PE': {'oi': 368, 'changeinoi': -42, 'ltp': 1036.25, 'trendschangeoi': [-42, -40, -40],
                            'trends': [2, 2, -1, -1, -1]}}, 20800: {
                     'CE': {'oi': 3650, 'changeinoi': 2352, 'ltp': 284.25, 'trendschangeoi': [2352, 2350, 2308],
                            'trends': [-2, -44, -1, -1, -1]},
                     'PE': {'oi': 360, 'changeinoi': -120, 'ltp': 1126.05, 'trendschangeoi': [-120, -115, -109],
                            'trends': [5, 11, -1, -1, -1]}}, 20900: {
                     'CE': {'oi': 1930, 'changeinoi': 1418, 'ltp': 255.4, 'trendschangeoi': [1418, 1376, 1409],
                            'trends': [-42, -9, -1, -1, -1]},
                     'PE': {'oi': 236, 'changeinoi': -48, 'ltp': 1208.35, 'trendschangeoi': [-48, -47, -45],
                            'trends': [1, 3, -1, -1, -1]}}, 21000: {
                     'CE': {'oi': 20807, 'changeinoi': 9886, 'ltp': 230.6, 'trendschangeoi': [9886, 9973, 10221],
                            'trends': [87, 335, -1, -1, -1]},
                     'PE': {'oi': 3824, 'changeinoi': -359, 'ltp': 1275.05, 'trendschangeoi': [-359, -360, -354],
                            'trends': [-1, 5, -1, -1, -1]}}, 21100: {
                     'CE': {'oi': 2402, 'changeinoi': 1592, 'ltp': 206.2, 'trendschangeoi': [1592, 1558, 1514],
                            'trends': [-34, -78, -1, -1, -1]},
                     'PE': {'oi': 353, 'changeinoi': -20, 'ltp': 1291.2, 'trendschangeoi': [-20, -20, -20],
                            'trends': [0, 0, -1, -1, -1]}}, 21200: {
                     'CE': {'oi': 2708, 'changeinoi': 1211, 'ltp': 185.25, 'trendschangeoi': [1211, 1228, 1453],
                            'trends': [17, 242, -1, -1, -1]},
                     'PE': {'oi': 155, 'changeinoi': -19, 'ltp': 1510.2, 'trendschangeoi': [-19, -19, -19],
                            'trends': [0, 0, -1, -1, -1]}}, 21300: {
                     'CE': {'oi': 2487, 'changeinoi': 1437, 'ltp': 164.5, 'trendschangeoi': [1437, 1475, 1510],
                            'trends': [38, 73, -1, -1, -1]},
                     'PE': {'oi': 87, 'changeinoi': 0, 'ltp': 1498.5, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 21400: {
                     'CE': {'oi': 1575, 'changeinoi': 695, 'ltp': 145.85, 'trendschangeoi': [695, 685, 677],
                            'trends': [-10, -18, -1, -1, -1]},
                     'PE': {'oi': 25, 'changeinoi': -2, 'ltp': 1308.6, 'trendschangeoi': [-2, -2, -2],
                            'trends': [0, 0, -1, -1, -1]}}, 21500: {
                     'CE': {'oi': 17202, 'changeinoi': 5887, 'ltp': 129.95, 'trendschangeoi': [5887, 5697, 5571],
                            'trends': [-190, -316, -1, -1, -1]},
                     'PE': {'oi': 968, 'changeinoi': -478, 'ltp': 1601.15, 'trendschangeoi': [-478, -478, -475],
                            'trends': [0, 3, -1, -1, -1]}}, 21600: {
                     'CE': {'oi': 1951, 'changeinoi': 1257, 'ltp': 115.5, 'trendschangeoi': [1257, 1302, 1375],
                            'trends': [45, 118, -1, -1, -1]},
                     'PE': {'oi': 10, 'changeinoi': 2, 'ltp': 1641.1, 'trendschangeoi': [2, 2, 2],
                            'trends': [0, 0, -1, -1, -1]}}, 21700: {
                     'CE': {'oi': 1964, 'changeinoi': 1461, 'ltp': 101.8, 'trendschangeoi': [1461, 1395, 1402],
                            'trends': [-66, -59, -1, -1, -1]},
                     'PE': {'oi': 13, 'changeinoi': -1, 'ltp': 1959.1, 'trendschangeoi': [-1, -1, -1],
                            'trends': [0, 0, -1, -1, -1]}}, 21800: {
                     'CE': {'oi': 4226, 'changeinoi': 3053, 'ltp': 89.5, 'trendschangeoi': [3053, 3083, 3184],
                            'trends': [30, 131, -1, -1, -1]},
                     'PE': {'oi': 2, 'changeinoi': 1, 'ltp': 2140.85, 'trendschangeoi': [1, 1, 1],
                            'trends': [0, 0, -1, -1, -1]}}, 21900: {
                     'CE': {'oi': 1410, 'changeinoi': 997, 'ltp': 80.05, 'trendschangeoi': [997, 996, 957],
                            'trends': [-1, -40, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22000: {
                     'CE': {'oi': 20172, 'changeinoi': 9144, 'ltp': 71.7, 'trendschangeoi': [9144, 9052, 8904],
                            'trends': [-92, -240, -1, -1, -1]},
                     'PE': {'oi': 355, 'changeinoi': -19, 'ltp': 2110.05, 'trendschangeoi': [-19, -19, -20],
                            'trends': [0, -1, -1, -1, -1]}}, 22100: {
                     'CE': {'oi': 816, 'changeinoi': 548, 'ltp': 63.1, 'trendschangeoi': [548, 588, 639],
                            'trends': [40, 91, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22200: {
                     'CE': {'oi': 1182, 'changeinoi': 682, 'ltp': 56, 'trendschangeoi': [682, 686, 710],
                            'trends': [4, 28, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22300: {
                     'CE': {'oi': 857, 'changeinoi': 667, 'ltp': 49.25, 'trendschangeoi': [667, 615, 634],
                            'trends': [-52, -33, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22400: {
                     'CE': {'oi': 746, 'changeinoi': 435, 'ltp': 43.65, 'trendschangeoi': [435, 484, 473],
                            'trends': [49, 38, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22500: {
                     'CE': {'oi': 12794, 'changeinoi': 4713, 'ltp': 38.3, 'trendschangeoi': [4713, 4756, 4640],
                            'trends': [43, -73, -1, -1, -1]},
                     'PE': {'oi': 3, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22600: {
                     'CE': {'oi': 1100, 'changeinoi': 457, 'ltp': 34.05, 'trendschangeoi': [457, 455, 445],
                            'trends': [-2, -12, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22700: {
                     'CE': {'oi': 704, 'changeinoi': 508, 'ltp': 30, 'trendschangeoi': [508, 493, 485],
                            'trends': [-15, -23, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22800: {
                     'CE': {'oi': 741, 'changeinoi': 450, 'ltp': 26.15, 'trendschangeoi': [450, 437, 435],
                            'trends': [-13, -15, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 22900: {
                     'CE': {'oi': 710, 'changeinoi': 396, 'ltp': 22.65, 'trendschangeoi': [396, 374, 376],
                            'trends': [-22, -20, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23000: {
                     'CE': {'oi': 13058, 'changeinoi': 2264, 'ltp': 19.9, 'trendschangeoi': [2264, 2249, 2525],
                            'trends': [-15, 261, -1, -1, -1]},
                     'PE': {'oi': 33, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23100: {
                     'CE': {'oi': 332, 'changeinoi': 222, 'ltp': 18.1, 'trendschangeoi': [222, 241, 240],
                            'trends': [19, 18, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23200: {
                     'CE': {'oi': 737, 'changeinoi': 140, 'ltp': 15.6, 'trendschangeoi': [140, 159, 157],
                            'trends': [19, 17, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23300: {
                     'CE': {'oi': 39, 'changeinoi': 39, 'ltp': 14.1, 'trendschangeoi': [39, 22, 17],
                            'trends': [-17, -22, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23400: {
                     'CE': {'oi': 198, 'changeinoi': 72, 'ltp': 12.75, 'trendschangeoi': [72, 67, 70],
                            'trends': [-5, -2, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23500: {
                     'CE': {'oi': 8800, 'changeinoi': 2857, 'ltp': 10.7, 'trendschangeoi': [2857, 2870, 2758],
                            'trends': [13, -99, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23600: {
                     'CE': {'oi': 122, 'changeinoi': 107, 'ltp': 11, 'trendschangeoi': [107, 106, 107],
                            'trends': [-1, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23700: {
                     'CE': {'oi': 124, 'changeinoi': 124, 'ltp': 11, 'trendschangeoi': [124, 124, 124],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23800: {
                     'CE': {'oi': 305, 'changeinoi': 174, 'ltp': 8.7, 'trendschangeoi': [174, 176, 171],
                            'trends': [2, -3, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 23900: {
                     'CE': {'oi': 409, 'changeinoi': 213, 'ltp': 9.4, 'trendschangeoi': [213, 213, 206],
                            'trends': [0, -7, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24000: {
                     'CE': {'oi': 5678, 'changeinoi': 1311, 'ltp': 7, 'trendschangeoi': [1311, 1234, 1267],
                            'trends': [-77, -44, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24100: {
                     'CE': {'oi': 47, 'changeinoi': 38, 'ltp': 6.3, 'trendschangeoi': [38, 38, 38],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24200: {
                     'CE': {'oi': 59, 'changeinoi': 34, 'ltp': 6.2, 'trendschangeoi': [34, 34, 34],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24300: {
                     'CE': {'oi': 56, 'changeinoi': 16, 'ltp': 6.65, 'trendschangeoi': [16, 16, 16],
                            'trends': [0, 0, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24400: {
                     'CE': {'oi': 173, 'changeinoi': -60, 'ltp': 6.7, 'trendschangeoi': [-60, -61, -61],
                            'trends': [-1, -1, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}, 24500: {
                     'CE': {'oi': 5384, 'changeinoi': 970, 'ltp': 5.55, 'trendschangeoi': [970, 949, 945],
                            'trends': [-21, -25, -1, -1, -1]},
                     'PE': {'oi': 0, 'changeinoi': 0, 'ltp': 0, 'trendschangeoi': [0, 0, 0],
                            'trends': [0, 0, -1, -1, -1]}}}]]
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
