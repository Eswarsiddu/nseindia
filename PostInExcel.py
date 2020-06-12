import os
from Constants import Constants as Const
while True:
    try:
        import xlwings as xw
        print("imported xlwings")
        break
    except:
        print("xlwings not installed")
        os.system("pip install xlwings")


def getrange(column,row):
    return column+str(row)

class Excel:
    def __init__(self,filepath):
        self.filepath = filepath
        self.wb = xw.Book(self.filepath)
        print("file opened")
        self.nifty = self.wb.sheets[0]
        print("got nifty")
        self.banknifty = self.wb.sheets[1]
        print("bank nifty")

    def setcolumnnames(self):
        self.nifty.range(getrange(column=Const.CALLS_LTP),3).value = Const.LTP


    def postinexcel(self,data):
        # TODO: pOST DATA IN excel
        pass

    def save_file(self):
        print("saving file")
        self.wb.save(self.filepath)
