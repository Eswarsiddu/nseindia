from typing import List
from dependencies.Constants import Constants as Const

sortingkey = lambda x: x[1]




def textformat(value, catogery):
    if catogery == Const.OI:
        return str(value)
    if catogery == Const.CHANGE_IN_OI:
        return str(value)
    if catogery == Const.LTP:
        return str(value)
    if catogery == Const.TRENDS:
        val = str(value)
        return '-' if val == '0' or val == '0.0' else val
    if catogery == Const.STRIKE_PRICE:
        return str(value)


def getStrikeRange(turnoverprice, up, down, index):
    low, high = (turnoverprice - (up * Const.strikesdiff[index])), (
            turnoverprice + ((down + 1) * Const.strikesdiff[index]))
    l: List[int] = []
    for i in range(low, high, Const.strikesdiff[index]):
        l.append(i)
    return l


def get_cell_attributes(text, fontcolor=Const.BLACK, cellcolor=None, fontstyle=Const.REGULAR, fontsize=10):
    return {Const.TEXT: text, Const.FONT_SIZE: fontsize, Const.FONT_STYLE: fontstyle, Const.FONT_COLOR: fontcolor,
            Const.CELL_FILL_COLOR: cellcolor}


def modify_maxdata(options):
    if options[Const.TEXT] not in ('-','0.0'):
        options[Const.CELL_FILL_COLOR] = Const.BLUE
        if options[Const.FONT_COLOR] == Const.BLACK:
            options[Const.FONT_COLOR] = Const.WHITE
    return options


def modify_data(options, maxvalues, type):
    for catogery in (Const.OI, Const.LTP, Const.CHANGE_IN_OI, Const.TRENDS1, Const.TRENDS2, Const.TRENDS3):
        options[maxvalues[catogery][Const.STRIKE_PRICE]][type][catogery] = modify_maxdata(
            options=options[maxvalues[catogery][Const.STRIKE_PRICE]][type][catogery])
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
    return Const.WHITE

# TODO: FONT COLOR BASED ON CATOGERY
def getfontcolor(text, catogery):
    if catogery == Const.CHANGE_IN_OI:
        if text[0] == '-' and len(text) > 1:
            return Const.RED
    return Const.BLACK


def findmaxvalue(presentdata, prevdata, strikeprice):
    if presentdata > prevdata[Const.VALUE]:
        prevdata[Const.STRIKE_PRICE] = strikeprice
        prevdata[Const.VALUE] = presentdata
    return prevdata


def getoptions(data, strikeprice, turnoverprice, optiontype, maxvalues):
    option = {}
    option[Const.OI] = get_cell_attributes(
        text=textformat(value=data[Const.OI], catogery=Const.OI),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.OI)
    )
    option[Const.CHANGE_IN_OI] = get_cell_attributes(
        text=textformat(value=data[Const.CHANGE_IN_OI], catogery=Const.CHANGE_IN_OI),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.CHANGE_IN_OI),
        fontcolor=getfontcolor(text=textformat(value=data[Const.CHANGE_IN_OI], catogery=Const.CHANGE_IN_OI),
                               catogery=Const.CHANGE_IN_OI)
    )
    option[Const.LTP] = get_cell_attributes(
        text=textformat(value=data[Const.LTP], catogery=Const.LTP),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.LTP),
        fontcolor=getfontcolor(text=textformat(value=data[Const.LTP], catogery=Const.LTP),
                               catogery=Const.LTP)
    )

    option[Const.TRENDS1] = get_cell_attributes(text=textformat(value=data[Const.TRENDS][0],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][0]),
                                                fontcolor=getfontcolor(text=textformat(value=data[Const.TRENDS][0],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS)
                                                )

    option[Const.TRENDS2] = get_cell_attributes(text=textformat(value=data[Const.TRENDS][1],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][1]),
                                                fontcolor=getfontcolor(text=textformat(value=data[Const.TRENDS][1],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS))

    option[Const.TRENDS3] = get_cell_attributes(text=textformat(value=data[Const.TRENDS][2],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS,
                                                                       obj=data[Const.TRENDS][2]),
                                                fontcolor=getfontcolor(text=textformat(value=data[Const.TRENDS][2],
                                                                                       catogery=Const.TRENDS),
                                                                       catogery=Const.TRENDS)
                                                )
    for i in (Const.OI, Const.CHANGE_IN_OI, Const.LTP):
        maxvalues[i] = findmaxvalue(presentdata=data[i],
                                    prevdata=maxvalues[i],
                                    strikeprice=strikeprice)
    return (option, maxvalues)


def analyse_data(data, index):
    up = Const.UP_VALUE[index]
    down = Const.DOWN_VALUE[index]
    options = {}
    if (data[Const.ERROR] != None):
        options[Const.ERROR] = data[Const.ERROR]
        return options

    options[Const.TIME] = data[Const.TIME]
    options[Const.DATE] = data[Const.DATE]
    options[Const.PRICE] = data[Const.PRICE]
    options[Const.MARKET_STATUS] = data[Const.MARKET_STATUS]
    options[Const.ERROR] = data[Const.ERROR]
    turnoverprice = data[Const.TURNOVER_PRICE]
    Strikeprices: List[int] = getStrikeRange(turnoverprice=turnoverprice, up=up, down=down, index=index)
    options[Const.STRIKES_LIST] = Strikeprices

    highestvalues = {
        Const.CALLS: {
            Const.OI: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.LTP: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.CHANGE_IN_OI: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS1: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS2: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS3: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            }
        },
        Const.PUTS: {
            Const.OI: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.LTP: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.CHANGE_IN_OI: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS1: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS2: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            },
            Const.TRENDS3: {
                Const.VALUE: float('-inf'),
                Const.STRIKE_PRICE: float('-inf')
            }
        }
    }
    for strikeprice in Strikeprices:
        options[strikeprice] = {Const.CALLS: {}, Const.PUTS: {}}
        options[strikeprice][Const.STRIKE_PRICE] = get_cell_attributes(
            text=textformat(value=strikeprice, catogery=Const.STRIKE_PRICE))
        calls, highestvalues[Const.CALLS] = getoptions(data=data[strikeprice][Const.CALLS],
                                                       strikeprice=strikeprice,
                                                       turnoverprice=data[Const.TURNOVER_PRICE],
                                                       optiontype=Const.CALLS,
                                                       maxvalues=highestvalues[Const.CALLS])

        puts, highestvalues[Const.PUTS] = getoptions(data=data[strikeprice][Const.PUTS],
                                                     strikeprice=strikeprice,
                                                     turnoverprice=data[Const.TURNOVER_PRICE],
                                                     optiontype=Const.PUTS,
                                                     maxvalues=highestvalues[Const.PUTS])

        options[strikeprice][Const.CALLS] = calls
        options[strikeprice][Const.PUTS] = puts
    turnoverlist = getStrikeRange(turnoverprice=turnoverprice,up=1,down=1,index=index)
    for es in turnoverlist:
        for ji in (Const.CALLS,Const.PUTS):
            highestvalues[ji][Const.TRENDS1] = findmaxvalue(presentdata=data[es][ji][Const.TRENDS][0],
                                                                     prevdata=highestvalues[ji][Const.TRENDS1],
                                                                     strikeprice=es)
            highestvalues[ji][Const.TRENDS2] = findmaxvalue(presentdata=data[es][ji][Const.TRENDS][1],
                                                        prevdata=highestvalues[ji][Const.TRENDS2],
                                                        strikeprice=es)
            highestvalues[ji][Const.TRENDS3] = findmaxvalue(presentdata=data[es][ji][Const.TRENDS][2],
                                                        prevdata=highestvalues[ji][Const.TRENDS3],
                                                        strikeprice=es)
    options = modify_data(options=options,maxvalues=highestvalues[Const.CALLS],type=Const.CALLS)
    options = modify_data(options=options, maxvalues=highestvalues[Const.PUTS], type=Const.PUTS)
    return options


class DataFormatter:
    def __init__(self, index):
        self.__index = index

    def update_data(self, data):
        return analyse_data(data=data, index=self.__index)
