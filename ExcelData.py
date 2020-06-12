from Constants import Constants as Const

rgbToInt = lambda rgb: (rgb[0] + (rgb[1] * 256) + (rgb[2] * 256 * 256))

TEXT = 'text'
CELL_FILL_COLOR = 'fillcolor'
FONT_STYLE = 'fontstyle'
FONT_COLOR = 'fontcolor'
FONT_SIZE = 'fontsize'

RED = rgbToInt((230, 0, 0))
GREEN = rgbToInt((0, 230, 0))
YELLOW = rgbToInt((204, 204, 0))
BLACK = rgbToInt((0, 0, 0))


strikesdiff = [50,100]
def getStrikeRange(turnoverprice, up, down,index):
    low, high = (turnoverprice - (up * strikesdiff[index])), (turnoverprice + ((down + 1) * strikesdiff[index]))
    l = []
    for i in range(low, high, strikesdiff[index]):
        l.append(i)
    return l


def get_cell_attributes(text, fontcolor=BLACK, cellcolor=None, fontstyle="Regular", fontsize=11):
    return {TEXT: text, FONT_SIZE: fontsize, FONT_STYLE: fontstyle, FONT_COLOR: fontcolor, CELL_FILL_COLOR: cellcolor}

def modify_data(data,calls_changeoi,puts_changeoi):
    options = {}

    return options

def getcalloptions(data,strikeprice,turnoverprice):
    option = {}
    option[Const.OI] = get_cell_attributes(
        text=data[Const.OI],
        cellcolor=YELLOW if strikeprice <= turnoverprice else None
    )
    option[Const.CHANGE_IN_OI] = get_cell_attributes(
        text=data[Const.CHANGE_IN_OI],
        cellcolor=YELLOW if strikeprice <= turnoverprice else None
    )
    option[Const.LTP] = get_cell_attributes(
        text=data[Const.LTP],
        cellcolor=YELLOW if strikeprice <= turnoverprice else None
    )
    return option

def getputoptions(data,strikeprice,turnoverprice):
    option = {}
    option[Const.OI] = get_cell_attributes(
        text=data[Const.OI],
        cellcolor=YELLOW if strikeprice > turnoverprice else None
    )
    option[Const.CHANGE_IN_OI] = get_cell_attributes(
        text=data[Const.CHANGE_IN_OI],
        cellcolor=YELLOW if strikeprice > turnoverprice else None
    )
    option[Const.LTP]=get_cell_attributes(
        text=data[Const.LTP],
        cellcolor=YELLOW if strikeprice > turnoverprice else None
    )
    return option

def analyse_data(data,up,down,index):
    options = {}
    turnoverprice = data[Const.TURNOVER_PRICE]
    Strikeprices = getStrikeRange(turnoverprice=turnoverprice, up=up, down=down,index=index)
    for strikeprice in Strikeprices:
        options[strikeprice] = {Const.CALLS: {}, Const.PUTS: {}}
        options[strikeprice][Const.STRIKE_PRICE] = get_cell_attributes(text=strikeprice)
        calls = getcalloptions(data=data[strikeprice][Const.CALLS],strikeprice=strikeprice,turnoverprice=data[Const.TURNOVER_PRICE])
        puts = getputoptions(data=data[strikeprice][Const.PUTS],strikeprice=strikeprice,turnoverprice=data[Const.TURNOVER_PRICE])
        options[strikeprice][Const.CALLS] = calls
        options[strikeprice][Const.PUTS] = puts
        #print(strikeprice, options)
    return options


class ExcelDataFormatter:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def update_data(self, data):
        niftydata = analyse_data(data=data[Const.NIFTY],up=self.up,down=self.down,index=Const.NIFTY)
        bankniftydata = analyse_data(data=data[Const.BANK_NIFTY],up=self.up,down=self.down,index=Const.BANK_NIFTY)
        return [niftydata, bankniftydata]
