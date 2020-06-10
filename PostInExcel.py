import os
while True:
    try:
        import xlwings as xw
        print("imported xlwings")
        break
    except:
        print("xlwings not installed")
        os.system("pip install xlwings")

class Excel:
    def __init__(self,filepath):
        self.filepath = filepath
        self.wb = xw.Book(self.filepath)
        print("file opened")
        self.nifty = self.wb.sheets[0]
        print("got nifty")
        self.banknifty = self.wb.sheets[1]
        print("bank nifty")

    def getlastrow(self, row = "F"):
        self.lastrow_nifty = self.nifty.cells(self.nifty.api.rows.count, row).end(-4162).row
        self.lastrow_banknifty = self.nifty.cells(self.banknifty.api.rows.count, row).end(-4162).row

    def mergetime(self, l):
        self.getlastrow()
        ran = "A"+str(self.lastrow_nifty-l+1)+":A"+str(self.lastrow_nifty)
        self.nifty.range(ran).api.merge()


    def postdata(self, presentdate, presenttime, data, gap):
        print("posting in excel")

        #self.getlastrow()
        self.nifty.cells(3, 1).value = presentdate+'\n'+presenttime
        self.nifty.range(("A" + str(3))).api.Font.Bold = True
        self.nifty.cells(3, 2).value = data
        self.mergetime(len(data))
        self.save_file()

    def save_file(self):
        print("saving file")
        self.wb.save(self.filepath)
