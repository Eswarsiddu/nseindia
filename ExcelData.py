from typing import List
from Constants import Constants as Const

sortingkey = lambda x: x[1]

def convertolakhs(n):
    n = n/100000
    s = '{0:.2f}'.format(n)
    if s == '-0.00' or s == '0.00':
        s = '0'
    return s

def textformat(text, catogery):
    if catogery == Const.OI:
        return convertolakhs(text)
    if catogery == Const.CHANGE_IN_OI:
        return convertolakhs(text)
    if catogery == Const.LTP:
        return str(text)
    if catogery == Const.TRENDS:
        val = convertolakhs(text)
        return '-' if val == '0' else val
    if catogery == Const.STRIKE_PRICE:
        return str(text)


def getStrikeRange(turnoverprice, up, down, index):
    low, high = (turnoverprice - (up * Const.strikesdiff[index])), (
                turnoverprice + ((down + 1) * Const.strikesdiff[index]))
    l: List[int] = []
    for i in range(low, high, Const.strikesdiff[index]):
        l.append(i)
    return l


def get_cell_attributes(text, fontcolor=Const.BLACK, cellcolor=None, fontstyle=Const.REGULAR, fontsize=11):
    return {Const.TEXT: text, Const.FONT_SIZE: fontsize, Const.FONT_STYLE: fontstyle, Const.FONT_COLOR: fontcolor,
            Const.CELL_FILL_COLOR: cellcolor}


def modify_data(options, calls_changeinoi, puts_changeinoi, turnoverprice):
    strikes = [i[1] for i in calls_changeinoi] + [i[1] for i in puts_changeinoi]
    strikes = sorted(set(strikes))
    upstrikes = [i for i in strikes if i<=turnoverprice]
    downstrikes = [i for i in strikes if i>turnoverprice]

    for i in range(len(upstrikes)):
        options[upstrikes[len(upstrikes)-1-i]][Const.STRIKE_PRICE][Const.CELL_FILL_COLOR] = Const.BLUE
        options[upstrikes[len(upstrikes)-1-i]][Const.STRIKE_PRICE][Const.FONT_SIZE] = Const.FONTSIZE(i+1)
        options[upstrikes[len(upstrikes)-1-i]][Const.STRIKE_PRICE][Const.FONT_STYLE] = Const.BOLD
        options[upstrikes[len(upstrikes)-1-i]][Const.STRIKE_PRICE][Const.FONT_COLOR] = Const.WHITE

    for i in range(len(downstrikes)):
        options[downstrikes[i]][Const.STRIKE_PRICE][Const.CELL_FILL_COLOR] = Const.BLUE
        options[downstrikes[i]][Const.STRIKE_PRICE][Const.FONT_SIZE] = Const.FONTSIZE(i+1)
        options[downstrikes[i]][Const.STRIKE_PRICE][Const.FONT_STYLE] = Const.BOLD
        options[downstrikes[i]][Const.STRIKE_PRICE][Const.FONT_COLOR] = Const.WHITE
    return options


def getcellcolor(turnoverprice, strikeprice, optiontype, catogery, obj=0):
    if catogery == Const.TRENDS:
        if obj >= 30000:
            return Const.GREEN
    if optiontype == Const.CALLS:
        if strikeprice <= turnoverprice:
            return Const.YELLOW
    else:
        if strikeprice > turnoverprice:
            return Const.YELLOW
    return None


def getfontcolor(text,catogery):
    if text[0]=='-' and len(text)>1:
        return Const.RED
    return Const.BLACK


def getoptions(data, strikeprice, turnoverprice, optiontype):
    option = {}
    option[Const.OI] = get_cell_attributes(
        text=textformat(text=data[Const.OI], catogery=Const.OI),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.OI)
    )
    option[Const.CHANGE_IN_OI] = get_cell_attributes(
        text=textformat(text=data[Const.CHANGE_IN_OI], catogery=Const.CHANGE_IN_OI),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.CHANGE_IN_OI),
        fontcolor=getfontcolor(text=textformat(text=data[Const.CHANGE_IN_OI], catogery=Const.CHANGE_IN_OI),
                               catogery=Const.CHANGE_IN_OI)
    )
    option[Const.LTP] = get_cell_attributes(
        text=textformat(text=data[Const.LTP], catogery=Const.LTP),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.LTP),
        fontcolor=getfontcolor(text=textformat(text=data[Const.LTP], catogery=Const.LTP),
                               catogery=Const.LTP)
    )

    option[Const.TRENDS1] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][0],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][0]),
                                                fontcolor=getfontcolor(text=textformat(text=data[Const.TRENDS][0],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS)
                                                )

    option[Const.TRENDS2] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][1],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][1]),
                                                fontcolor=getfontcolor(text=textformat(text=data[Const.TRENDS][1],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS))

    option[Const.TRENDS3] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][2],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][2]),
                                                fontcolor=getfontcolor(text=textformat(text=data[Const.TRENDS][2],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS)
                                                )
    return option


def insertionsort(val, strikeprice, arr):
    temp = [val, strikeprice]
    if len(arr) == 0:
        arr.append(temp)
    elif len(arr) == 1:
        if arr[0][0] <= val:
            arr.append(temp)
        else:
            arr.insert(0, temp)
    elif len(arr) == 2:
        if arr[1][0] <= val:
            arr.append(temp)
        elif arr[0][0] <= val:
            arr.insert(1, temp)
        else:
            arr.insert(0, temp)
    else:
        if arr[2][0] <= val:
            arr.append(temp)
        elif arr[1][0] <= val:
            arr.insert(2, temp)
        elif arr[0][0] <= val:
            arr.insert(1, temp)
    if (len(arr) >= 4):
        arr = arr[1:]
    return arr


def analyse_data(data, up, down, index):
    options = {}
    if(data[Const.ERROR]!=None):
        options[Const.ERROR] = data[Const.ERROR]
        return options

    options[Const.TIME] = data[Const.TIME]
    options[Const.DATE] = data[Const.DATE]
    options[Const.PRICE] = data[Const.PRICE]
    options[Const.MARKET_STATUS] = data[Const.MARKET_STATUS]
    options[Const.ERROR] = data[Const.ERROR]
    turnoverprice = data[Const.TURNOVER_PRICE]
    Strikeprices: List[int] = getStrikeRange(turnoverprice=turnoverprice, up=up, down=down, index=index)
    options[Const.EXCEL_STRIKES] = Strikeprices
    calls_changeinoi, puts_changeinoi = [], []

    for strikeprice in Strikeprices:
        options[strikeprice] = {Const.CALLS: {}, Const.PUTS: {}}
        options[strikeprice][Const.STRIKE_PRICE] = get_cell_attributes(text=textformat(text=strikeprice,catogery=Const.STRIKE_PRICE))
        calls = getoptions(data=data[strikeprice][Const.CALLS],
                           strikeprice=strikeprice,
                           turnoverprice=data[Const.TURNOVER_PRICE],
                           optiontype=Const.CALLS)

        puts = getoptions(data=data[strikeprice][Const.PUTS],
                          strikeprice=strikeprice,
                          turnoverprice=data[Const.TURNOVER_PRICE],
                          optiontype=Const.PUTS)

        calls_changeinoi = insertionsort(val=data[strikeprice][Const.CALLS][Const.CHANGE_IN_OI],
                                         strikeprice=strikeprice, arr=calls_changeinoi)
        puts_changeinoi = insertionsort(val=data[strikeprice][Const.PUTS][Const.CHANGE_IN_OI], strikeprice=strikeprice,
                                        arr=puts_changeinoi)

        options[strikeprice][Const.CALLS] = calls
        options[strikeprice][Const.PUTS] = puts
    options = modify_data(options=options,
                          calls_changeinoi=calls_changeinoi,
                          puts_changeinoi=puts_changeinoi,
                          turnoverprice=turnoverprice)

    return options


class ExcelDataFormatter:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def update_data(self, data):
        l = [None,None]
        l[Const.NIFTY] = analyse_data(data=data[Const.NIFTY], up=self.up, down=self.down, index=Const.NIFTY)
        l[Const.BANK_NIFTY] = analyse_data(data=data[Const.BANK_NIFTY], up=self.up, down=self.down, index=Const.BANK_NIFTY)
        return l
