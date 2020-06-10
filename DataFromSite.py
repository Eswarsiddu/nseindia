from Constants import Constants as Const
import requests


class DataRequest:
    def __init__(self, Data):
        self.Data = Data

    def calculate_price(self, n):
        n = int(n)
        n -= (n % 50)
        return n

    def get_data(self, body, options):
        for data in body:
            strike_price: int = data['strikePrice']
            options[strike_price]: dict = {}
            for j in ('CE', 'PE'):
                temp = data[j]
                options[strike_price][j] = {Const.OI: temp['openInterest'],
                                            Const.CHANGE_IN_OI: temp['changeinOpenInterest'],
                                            Const.LTP: temp['lastPrice']
                                            }

    def market_status(self, time):
        if time == '15:30:00':
            return False
        return True

    def get_options(self, options, request, previous_time_stamp):
        body = requests.get(url=request,
                            headers=Const.HEADERS
                            ).json()
        timestamp = body['records']['timestamp'].split(" ")

        # checking market status
        if self.market_status(time=timestamp[1]):
            options[Const.MARKET_STATUS] = True
        else:
            options[Const.MARKET_STATUS] = False

        options[Const.TIME] = timestamp[1]
        options[Const.DATE] = timestamp[0]
        price = body['records']['underlyingValue']
        turnover_price = self.calculate_price(price)
        options[Const.PRICE] = price
        options[Const.TURNOVER_PRICE] = turnover_price
        self.get_data(body=body['filtered']['data'], options=options)

    def request_data(self):
        self.get_options(options=self.Data[Const.NIFTY], request=Const.URLS[Const.NIFTY])
        self.get_options(options=self.Data[Const.BANK_NIFTY], request=Const.URLS[Const.BANK_NIFTY])
