from typing import Tuple, Dict


class Constants:
    URLS: Tuple[str, str] = ('https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY',
                             'https://www.nseindia.com/api/option-chain-indices?symbol=BANKNIFTY')

    NIFTY: int = 0
    BANK_NIFTY: int = 1
    STRIKE_PRICE:str = 'strikeprice'
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
    TRENDS:str = "trends"
    TREND_CHANGE_OF_OI: str = "trendschangeoi"
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

