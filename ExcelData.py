from Constants import Constants as Const

rgbToInt = lambda rgb: (rgb[0] + (rgb[1] * 256) + (rgb[2] * 256 * 256))

TEXT = 'text'
CELL_FILL_COLOR = 'fillcolor'
FONT_STYLE = 'fontstyle'
FONT_COLOR = 'fontcolor'
FONT_SIZE = 'fontsize'

RED = rgbToInt((230,0,0))
GREEN = rgbToInt((0,230,0))
YELLOW = rgbToInt((204,204,0))
BLACK = rgbToInt((0,0,0))


def getStrikeRange(turnoverprice, up, down):
    low, high = (turnoverprice - (up * 50)), (turnoverprice + ((down + 1) * 50))
    l = []
    for i in range(low, high, 50):
        l.append(i)
    return l


def get_cell_attributes(text, fontcolor=BLACK, cellcolor=None, fontstyle="Regular", fontsize=11):
    return {TEXT:text,FONT_SIZE:fontsize,FONT_STYLE:fontstyle,FONT_COLOR:fontcolor,CELL_FILL_COLOR:cellcolor}


class ExcelDataFormatter:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def analyse_data(self, data):
        options = {}
        turnoverprice = data[Const.TURNOVER_PRICE]
        Strikeprices = getStrikeRange(turnoverprice, self.up, self.down)
        for strikeprice in Strikeprices:
            options[strikeprice] = {Const.CALLS:{},Const.PUTS:{}}
            calls = {}
            calls[Const.OI] = get_cell_attributes(
                text=data[strikeprice][Const.CALLS][Const.OI],
                cellcolor=YELLOW if strikeprice<=data[Const.TURNOVER_PRICE] else None
            )
            print(strikeprice, data[strikeprice][Const.CALLS])

    def update_data(self, data):
        niftydata = data[Const.NIFTY]
        self.analyse_data(niftydata)
        bankniftydata = data[Const.BANK_NIFTY]
