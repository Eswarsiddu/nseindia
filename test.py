from Constants import Constants as Const
import requests

Data = [{Const.INDEX: "NIFTY"}, {Const.INDEX: "BANK NIFTY"}]


def calculate_price(n):
    n = int(n)
    n -= (n % 50)
    return n


def get_data(body, options):
    for data in body:
        strike_price: int = data['strikePrice']
        options[strike_price]: dict = {}
        for j in ('CE', 'PE'):
            temp = data[j]
            options[strike_price][j] = {Const.OI: temp['openInterest'],
                                        Const.CHANGE_IN_OI: temp['changeinOpenInterest'],
                                        Const.LTP: temp['lastPrice']
                                        }


def market_status(timestamp):
    if timestamp.split(" ")[1] == '15:30:00':
        return False
    return True


def get_options(options, request, previous_time_stamp):
    body = requests.get(url=request,
                        headers=Const.HEADERS
                        ).json()
    timestamp = body['records']['timestamp']

    # checking market status
    if market_status(timestamp=timestamp):
        options[Const.MARKET_STATUS] = True
    else:
        options[Const.MARKET_STATUS] = False

    if previous_time_stamp != timestamp:
        options[Const.TIME] = timestamp.split(" ")[1]
        options[Const.DATE] = timestamp.split(" ")[0]
        price = body['records']['underlyingValue']
        turnover_price = calculate_price(price)
        options[Const.PRICE] = price
        options[Const.TURNOVER_PRICE] = turnover_price
        get_data(body=body['filtered']['data'], options=options)
        return timestamp
    return "Notchanged"


if __name__ == "__main__":
    prevtimestamp = ['', '']
    # TODO:change for to while
    for i in range(1):
        # Nifty data
        t = get_options(options=Data[Const.NIFTY],
                        request=Const.URLS[Const.NIFTY],
                        previous_time_stamp=prevtimestamp[Const.NIFTY])
        if (t != "Notchanged"):
            prevtimestamp[Const.NIFTY] = t

        # Bank Nifty data
        t = get_options(options=Data[Const.BANK_NIFTY],
                        request=Const.URLS[Const.BANK_NIFTY],
                        previous_time_stamp=prevtimestamp[Const.BANK_NIFTY]
                        )
        if t != "Notchanged":
            prevtimestamp[Const.BANK_NIFTY] = t

        print("prev:", prevtimestamp)
        for i in Data:
            print(i.keys())
