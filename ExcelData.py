from typing import List, Dict

from Constants import Constants as Const

strikesdiff = [50, 100]

sortingkey = lambda x:x[1]

def textformat(text,catogery):
    if text == 0:
        return '-'
    # TODO: textformater for excel
    return str(text)

def getStrikeRange(turnoverprice, up, down, index):
    low, high = (turnoverprice - (up * strikesdiff[index])), (turnoverprice + ((down + 1) * strikesdiff[index]))
    l: List[int] = []
    for i in range(low, high, strikesdiff[index]):
        l.append(i)
    return l


def get_cell_attributes(text, fontcolor=Const.BLACK, cellcolor=None, fontstyle=Const.REGULAR, fontsize=11):
    return {Const.TEXT: text, Const.FONT_SIZE: fontsize, Const.FONT_STYLE: fontstyle, Const.FONT_COLOR: fontcolor,
            Const.CELL_FILL_COLOR: cellcolor}


def modify_data(options,calls_changeinoi,puts_changeinoi,turmoverprice):
    strikes = [i[1] for i in calls_changeinoi] + [i[1] for i in puts_changeinoi]
    strikes = sorted(set(strikes))
    for strike in strikes:
        options[strike][Const.STRIKE_PRICE][Const.CELL_FILL_COLOR] = Const.BLUE
        options[strike][Const.STRIKE_PRICE][Const.FONT_SIZE] = 14
        options[strike][Const.STRIKE_PRICE][Const.FONT_STYLE] = Const.BOLD
    # TODO: Modify data based on turnoverprice
    return options

def getcellcolor(turnoverprice, strikeprice, optiontype, catogery, obj=None):
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


def getoptions(data, strikeprice, turnoverprice, optiontype):
    option = {}
    option[Const.OI] = get_cell_attributes(
        text=textformat(text=data[Const.OI],catogery=Const.OI),
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
                               catogery=Const.CHANGE_IN_OI)
    )
    option[Const.LTP] = get_cell_attributes(
        text=textformat(text=data[Const.LTP],catogery=Const.LTP),
        cellcolor=getcellcolor(turnoverprice=turnoverprice,
                               strikeprice=strikeprice,
                               optiontype=optiontype,
                               catogery=Const.LTP)
    )

    option[Const.TRENDS1] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][0],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS))

    option[Const.TRENDS2] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][1],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS))

    option[Const.TRENDS3] = get_cell_attributes(text=textformat(text=data[Const.TRENDS][2],
                                                                catogery=Const.TRENDS),
                                                cellcolor=getcellcolor(turnoverprice=turnoverprice,
                                                                       strikeprice=strikeprice,
                                                                       optiontype=optiontype,
                                                                       catogery=Const.TRENDS))
    return option

def insertionsort(val,strikeprice,arr):
    temp = [val,strikeprice]
    if len(arr) == 0:
        arr.append(temp)
    elif len(arr==1):
        if arr[0] <= val:
            arr.append(temp)
        else:
            arr.insert(0,temp)
    elif len(arr==2):
        if arr[1] <= val:
            arr.append(temp)
        elif arr[0] <= val:
            arr.insert(1,temp)
        else:
            arr.insert(0,temp)
    else:
        if arr[2] <= val:
            arr.append(temp)
        elif arr[1] <= val:
            arr.insert(2,temp)
        elif arr[0] <= val:
            arr.insert(1,temp)
    if(len(arr)>=4):
        arr = arr[1:]
    return arr

def analyse_data(data, up, down, index):
    options = {}
    turnoverprice = data[Const.TURNOVER_PRICE]
    Strikeprices: List[int] = getStrikeRange(turnoverprice=turnoverprice, up=up, down=down, index=index)
    options[Const.EXCEL_STRIKES] = Strikeprices
    calls_changeinoi,puts_changeinoi = [],[]
    for strikeprice in Strikeprices:
        options[strikeprice] = {Const.CALLS: {}, Const.PUTS: {}}
        options[strikeprice][Const.STRIKE_PRICE] = get_cell_attributes(text=strikeprice)
        calls = getoptions(data=data[strikeprice][Const.CALLS],
                           strikeprice=strikeprice,
                           turnoverprice=data[Const.TURNOVER_PRICE],
                           optiontype=Const.CALLS)

        puts = getoptions(data=data[strikeprice][Const.PUTS],
                          strikeprice=strikeprice,
                          turnoverprice=data[Const.TURNOVER_PRICE],
                          optiontype=Const.PUTS)

        calls_changeinoi=insertionsort(val=calls,strikeprice=strikeprice,arr=calls_changeinoi)
        puts_changeinoi=insertionsort(val=puts,strikeprice=strikeprice,arr=puts_changeinoi)

        options[strikeprice][Const.CALLS] = calls
        options[strikeprice][Const.PUTS] = puts
        # print(strikeprice, options)
    options = modify_data(options=options,
                          calls_changeinoi=calls_changeinoi,
                          puts_changeinoi=puts_changeinoi,
                          turmoverprice=turnoverprice)
    return options


class ExcelDataFormatter:
    def __init__(self, up, down):
        self.up = up
        self.down = down

    def update_data(self, data):
        niftydata = analyse_data(data=data[Const.NIFTY], up=self.up, down=self.down, index=Const.NIFTY)
        bankniftydata = analyse_data(data=data[Const.BANK_NIFTY], up=self.up, down=self.down, index=Const.BANK_NIFTY)
        return [niftydata, bankniftydata]
