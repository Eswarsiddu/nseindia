import os
from Constants import Constants as Const

while True:
    try:
        import xlwings as xw
        break
    except:
        os.system("pip install xlwings")

def getrange(column, row,coloumn2='-1',row2=-1):
    if coloumn2 == '-1' and row2 == -1:
        return column + str(row)
    return column + str(row) + ":" + coloumn2 + str(row2)


class Excel:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.wb = xw.Book(self.filepath)
        except:
            self.wb = xw.Book()
            self.save_file()

        self.sheet = [None,None]
        try:
            self.sheet[Const.BANK_NIFTY] = self.wb.sheets[Const.BANK_NIFTY_NAME]
        except:
            self.wb.sheets.add(name=Const.BANK_NIFTY_NAME)
            self.sheet[Const.BANK_NIFTY] = self.wb.sheets[Const.BANK_NIFTY_NAME]
        try:
            self.sheet[Const.NIFTY] = self.wb.sheets[Const.NIFTY_NAME]
        except:
            self.wb.sheets.add(name=Const.NIFTY_NAME,before=Const.BANK_NIFTY_NAME)
            self.sheet[Const.NIFTY] = self.wb.sheets[Const.NIFTY_NAME]
        self.save_file()
        self.setcolumnnames(index=Const.NIFTY)
        self.setcolumnnames(index=Const.BANK_NIFTY)
        self.save_file()

    def mergecells(self, index, left, right, top, bottom, value):
        t = self.sheet[index].range(getrange(column=top, coloumn2=left,
                                             row=bottom, row2=right))
        t.api.MergeCells = True
        t.value = value

    def setcolumnnames(self, index):

        self.mergecells(index=index, top=1, bottom=1, left='A', right='M',
                        value="PLEASE WAIT FOR FEW SECONDS, RELOADING AWM 😁😁")

        # CALLS
        self.mergecells(index=index, value='CALLS', top=2, bottom=2, left='A', right='F')
        # PUTS
        self.mergecells(index=index, value='PUTS', top=2, bottom=2, left='H', right='M')

        # LTP
        self.sheet[index].range(getrange(column=Const.CALLS_LTP, row=3)).value = Const.LTP
        self.sheet[index].range(getrange(column=Const.PUTS_LTP, row=3)).value = Const.LTP

        # OI
        self.sheet[index].range(getrange(column=Const.CALLS_OI, row=3)).value = Const.OI
        self.sheet[index].range(getrange(column=Const.PUTS_OI, row=3)).value = Const.OI

        # CHANGE OF OI
        self.sheet[index].range(getrange(column=Const.CALLS_CHANGE_IN_OI, row=3)).value = Const.CHANGE_IN_OI
        self.sheet[index].range(getrange(column=Const.PUTS_CHANGE_IN_OI, row=3)).value = Const.CHANGE_IN_OI

        # TREND 1
        self.sheet[index].range(getrange(column=Const.CALLS_TREND1, row=3)).value = Const.getTrends(1)
        self.sheet[index].range(getrange(column=Const.PUTS_TREND1, row=3)).value = Const.getTrends(1)

        # TREND 2
        self.sheet[index].range(getrange(column=Const.CALLS_TREND2, row=3)).value = Const.getTrends(2)
        self.sheet[index].range(getrange(column=Const.PUTS_TREND2, row=3)).value = Const.getTrends(2)

        # TREND 3
        self.sheet[index].range(getrange(column=Const.CALLS_TREND3, row=3)).value = Const.getTrends(3)
        self.sheet[index].range(getrange(column=Const.PUTS_TREND3, row=3)).value = Const.getTrends(3)

        # STRIKE PRICE
        self.sheet[index].range(getrange(column=Const.EXCEL_STRIKE_PRICE_COLUMN, row=3)).value = Const.STRIKE_PRICE

        # SET BORDER
        t = self.sheet[index].range(getrange(column='A', coloumn2='M', row=1, row2=3))
        t.api.Borders = "output"
        t.api.Font.FontStyle = Const.BOLD
        t.api.Font.Size = Const.HEADING_SIZE

    def settimestamp(self, index, price, time, prevtime, date, prevprice, error):
        if (error != None):
            self.sheet[index].range('A1').value = str(
                prevprice) + " as of " + prevtime + " on " + date + " ,Error: " + error
            return False
        else:
            self.sheet[index].range('A1').value = str(price) + " as of " + time + " on " + date
            return True

    def postdatainexcel(self, index, data):
        strikes = data[Const.EXCEL_STRIKES]
        # TODO: POST DATA IN EXCEL
        for i in range(len(strikes)):
            row = i+4
            strikeprice = strikes[i]
            value = data[strikeprice]



    def postinexcel(self, data, prevtime, prevprice):
        # self.wb.app.screen_updating = False

        for index in (Const.NIFTY, Const.BANK_NIFTY):
            optiondata = data[index]
            if self.settimestamp(index=index,
                                 price=optiondata[Const.PRICE],
                                 time=optiondata[Const.TIME],
                                 prevprice=prevprice,
                                 prevtime=prevtime,
                                 date=data,
                                 error=optiondata[Const.ERROR]):
                self.postdatainexcel(index=index, data=optiondata)
        # self.wb.app.screen_updating = True
        self.save_file()

    def save_file(self):
        print("saving file")
        self.wb.save(self.filepath)
