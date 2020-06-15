from Constants import Constants as Const
import requests
import Sampledata


def calculate_price(n,index):
    n = int(n)
    n -= (n % Const.strikesdiff[index])
    return n


def get_data(body, options):
    for data in body:
        strike_price: int = data['strikePrice']
        try:
            t=options[strike_price]
        except:
            options[strike_price]: dict = {}
        for j in (Const.CALLS,Const.PUTS):
            temp = data[j]
            try:
                t = options[strike_price][j]
            except:
                options[strike_price][j] = {}
            options[strike_price][j][Const.OI]= temp['openInterest']
            options[strike_price][j][Const.CHANGE_IN_OI]= temp['changeinOpenInterest']
            options[strike_price][j][Const.LTP]=temp['lastPrice']
            try:
                trend_change_oi = options[strike_price][j][Const.TREND_CHANGE_OF_OI]
                trend_change_oi.insert(0, temp['changeinOpenInterest'])
                if len(trend_change_oi) > 6:
                    trend_change_oi.pop()
                if len(trend_change_oi)==1:
                    options[strike_price][j][Const.TRENDS][0] = trend_change_oi[1] - trend_change_oi[0]
                for i in range(1, len(trend_change_oi)):
                    options[strike_price][j][Const.TRENDS][i - 1] = trend_change_oi[i] - trend_change_oi[0]
                options[strike_price][j][Const.TREND_CHANGE_OF_OI] = trend_change_oi

            except:
                options[strike_price][j][Const.TREND_CHANGE_OF_OI] = [temp['changeinOpenInterest']]
                options[strike_price][j][Const.TRENDS] = [0, 0, 0, 0, 0]
    return options


def market_status(time):
    if time == '15:30:00':
        return False
    return True


def get_options(options, request,index):
    body = None
    timestamp = ""
    try:
        body = requests.get(url=request,
                            headers=Const.HEADERS
                            ).json()
    except:
        options[Const.ERROR] = Const.NO_INTERNET
        return options
    try:
        timestamp = body['records']['timestamp'].split(" ")
    except:
        options[Const.ERROR] = Const.NO_DATA_FROM_SITE
        return options

    if market_status(time=timestamp[1]):
        options[Const.MARKET_STATUS] = True
    else:
        options[Const.MARKET_STATUS] = False

    options[Const.TIME] = timestamp[1]
    options[Const.DATE] = timestamp[0]
    price = body['records']['underlyingValue']
    turnover_price = calculate_price(price,index)
    options[Const.PRICE] = price
    options[Const.TURNOVER_PRICE] = turnover_price
    options[Const.ERROR] = None
    return get_data(body=body['filtered']['data'], options=options)


class DataRequest:

    def __init__(self):
        self.Data = None
        self.reset_data()

    def reset_data(self):
        self.Data = [{},{}]

    @property
    def request_data(self):
        if Const.TESTING:
            Sampledata.testindex+=1
            return Sampledata.testdata[Sampledata.testindex]

        self.Data[Const.NIFTY] = get_options(options=self.Data[Const.NIFTY],
                                             request=Const.URLS[Const.NIFTY],
                                             index=Const.NIFTY)

        self.Data[Const.BANK_NIFTY] = get_options(options=self.Data[Const.BANK_NIFTY],
                                                  request=Const.URLS[Const.BANK_NIFTY],
                                                  index=Const.BANK_NIFTY)
        return self.Data
