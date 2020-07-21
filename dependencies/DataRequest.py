from dependencies.Constants import Constants as Const
from dependencies import Sampledata
import requests,json,threading,ctypes,time

requesting = False

def calculate_price(n, index):
    n = int(n)
    n -= (n % Const.strikesdiff[index])
    return n

def convertolakhs(n):
    n = n / 1000
    return convertodecimals(n)

def convertodecimals(n):
    s = '{0:.2f}'.format(n)
    if s == '-0.00' or s == '0.00':
        s = '0'
    return float(s)

c=0

def get_data(body, options):
    global c
    c+=1
    for data in body:
        strike_price: int = data['strikePrice']
        try:
            t = options[strike_price]
        except:
            options[strike_price]: dict = {}
        for j in (Const.CALLS, Const.PUTS):
            try:
                temp = data[j]
            except:
                temp = {'openInterest': 0, 'changeinOpenInterest': 0, 'lastPrice': 0}
            try:
                options[strike_price][j]
            except:
                options[strike_price][j] = {}
            options[strike_price][j][Const.OI] = temp['openInterest']
            options[strike_price][j][Const.CHANGE_IN_OI] = convertolakhs(temp['changeinOpenInterest'])
            options[strike_price][j][Const.LTP] = temp['lastPrice']
            try:
                trend_change_oi = options[strike_price][j][Const.TREND_CHANGE_OF_OI]
                trend_change_oi.insert(0, convertolakhs(temp['changeinOpenInterest']))
                if len(trend_change_oi) > 6:
                    trend_change_oi.pop()
                if len(trend_change_oi) == 1:
                    options[strike_price][j][Const.TRENDS][0] = convertodecimals(trend_change_oi[0] - trend_change_oi[1])
                for i in range(1, len(trend_change_oi)):
                    options[strike_price][j][Const.TRENDS][i - 1] = convertodecimals(trend_change_oi[0] - trend_change_oi[i])
                options[strike_price][j][Const.TREND_CHANGE_OF_OI] = trend_change_oi
                print("strk",strike_price,trend_change_oi)
            except:
                options[strike_price][j][Const.TREND_CHANGE_OF_OI] = [convertolakhs(temp['changeinOpenInterest'])]
                options[strike_price][j][Const.TRENDS] = [0, 0, 0, 0, 0]
    return options


def market_status(time):
    if time == '15:30:00':
        return False
    return True

def get_options(options, request, index):
    body = None
    timestamp = ""

    try:
        presenttime = options[Const.TIME]
    except:
        presenttime = ""

    try:
        if Const.TESTING == True:
            Sampledata.testindex += 1
            body = Sampledata.modniftydata[Sampledata.testindex]
        else:
            strtime = time.time()
            request_json = requests.get(url=request, headers=Const.HEADERS)
            if 'json' in request_json.headers.get('Content-Type'):
                body = request_json.json()
            endtime = time.time()
            print("requesting time",str(endtime-strtime))
    except requests.ConnectionError:
        options[Const.ERROR] = Const.NO_INTERNET
        return options
    except Exception as e:
        print("error:", str(e))
    try:
        timestamp = body['records']['timestamp'].split(" ")
    except:
        options[Const.ERROR] = Const.NO_DATA_FROM_SITE
        return options
    if presenttime == timestamp[1]:
        return None

    if market_status(time=timestamp[1]):
        options[Const.MARKET_STATUS] = True
    else:
        options[Const.MARKET_STATUS] = False

    options[Const.TIME] = timestamp[1]
    options[Const.DATE] = timestamp[0]
    price = body['records']['underlyingValue']
    turnover_price = calculate_price(price, index)
    options[Const.PRICE] = price
    options[Const.TURNOVER_PRICE] = turnover_price
    options[Const.ERROR] = None
    return get_data(body=body['filtered']['data'], options=options)


class DataRequest:
    def __init__(self, index):
        self.Data = None
        self.__index = index
        self.__url = Const.URLS[index]
        self.reset_data()

    def reset_data(self):
        self.Data = {}

    @property
    def request_data(self):
        # if Const.TESTING:
        #     Sampledata.testindex += 1
        #     data = Sampledata.niftydata[Sampledata.testindex]
        #     return data
        opt = get_options(options=self.Data, request=self.__url, index=self.__index)
        if opt != None:
            self.Data = opt
        else:
            return opt
        if opt[Const.ERROR]!=None:
            self.reset_data()
            self.Data[Const.ERROR] = opt[Const.ERROR]
            opt = self.Data
        #print(opt)
        return opt
