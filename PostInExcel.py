import platform,os
from Constants import Constants as Const
import win32com.client
xw = win32com.client.Dispatch('Excel.Application')
xw.Visible = True


def getrange(column, row, coloumn2='-1', row2=-1):
    if coloumn2 == '-1' and row2 == -1:
        return column + str(row)
    return column + str(row) + ":" + coloumn2 + str(row2)


class Excel:
    def __init__(self, filepath):
        self.__filepath = filepath
        self.setupexcel()
        print("Excel File Opened")


    def setupexcel(self):
        try:
            try:
                print("tying open")
                self.__wb = xw.Workbooks.Open(self.__filepath)
                print("opened")
            except:
                # TODO: create if doesnot exists
                print("creating")
                self.__wb = xw.Workbooks.Add()
                self.__wb.SaveAs(self.__filepath)
                print("created")
                print("opened aftewr creating")
                #self.__wb = xw.Workbooks.Open(self.__filepath)

            self.__sheet = [None, None]
            try:
                self.__sheet[Const.BANK_NIFTY] = self.__wb.Worksheets(Const.BANK_NIFTY_NAME)
            except:
                # TODO: Create bank nifty sheet if not exists
                print("does not exixts")
                self.__wb.Worksheets.Add()
                self.__sheet[Const.BANK_NIFTY] = self.__wb.Worksheets(1)
                self.__sheet[Const.BANK_NIFTY].Name = Const.BANK_NIFTY_NAME
                print("created")

            try:
                self.__sheet[Const.NIFTY] = self.__wb.Worksheets(Const.NIFTY_NAME)
            except:
                # TODO: Create nifty sheet if not exists
                self.__wb.Worksheets.Add(Before=self.__wb.Worksheets(1))
                self.__sheet[Const.NIFTY] = self.__wb.Worksheets(1)
                self.__sheet[Const.NIFTY].Name = Const.NIFTY_NAME

            self.__save_file()
            self.__setcolumnnames(index=Const.NIFTY)
            self.__setcolumnnames(index=Const.BANK_NIFTY)
            self.__save_file()
            self.__conformationcell = self.__getconformationcell()
            self.__errorcell = self.__geterrorsell()
        except Exception as e:
            print("error",str(e))




    def __geterrorsell(self):
        error = [None,None]
        error[Const.NIFTY] = self.__geterrcells(index=Const.NIFTY)
        error[Const.BANK_NIFTY] = self.__geterrcells(index=Const.BANK_NIFTY)
        return error

    def __geterrcells(self,index):
        row = Const.DIALOGUE_BOX_ROW
        t1 = self.__sheet[index].Range(getrange(column='B',coloumn2='L',row=row,row2=row))
        t2 = self.__sheet[index].Range(getrange(column='B',row=row))
        t2.Font.Size = 16
        t2.Font.Color = Const.RED
        return [t1,t2]

    def __getconformationcell(self):
        cells= [None,None]
        cells[Const.NIFTY] = self.__getconfrmcell(index = Const.NIFTY)
        cells[Const.BANK_NIFTY] = self.__getconfrmcell(index=Const.BANK_NIFTY)
        return cells

    def __getconfrmcell(self,index):
        row = Const.DIALOGUE_BOX_ROW
        column = 'A'
        t = self.__sheet[index].Range(getrange(column=column,row=row))
        t.Font.Size = 15
        t.Font.FontStyle = Const.BOLD
        t.Font.Color = Const.GREEN
        return t

    def __setconformationcell(self,text):
        self.__conformationcell[Const.NIFTY].Value = text
        self.__conformationcell[Const.BANK_NIFTY].Value = text

    def __mergecells(self, index, left, right, top, bottom, value,merging = True):
        t = self.__sheet[index].Range(getrange(column=left, coloumn2=right,
                                               row=top, row2=bottom))
        t.MergeCells = merging
        t.Value = value

    def __setcolumnnames(self, index):

        self.__mergecells(index=index, top=1, bottom=1, left='A', right='M',
                          value=Const.WELCOME_TEXT)

        # CALLS
        self.__mergecells(index=index, value='CALLS', top=2, bottom=2, left='A', right='F')
        # PUTS
        self.__mergecells(index=index, value='PUTS', top=2, bottom=2, left='H', right='M')

        # LTP
        self.__sheet[index].Range(getrange(column=Const.CALLS_LTP, row=3)).Value = Const.LTP
        self.__sheet[index].Range(getrange(column=Const.PUTS_LTP, row=3)).Value = Const.LTP

        # OI
        self.__sheet[index].Range(getrange(column=Const.CALLS_OI, row=3)).Value = Const.OI
        self.__sheet[index].Range(getrange(column=Const.PUTS_OI, row=3)).Value = Const.OI

        # CHANGE OF OI
        self.__sheet[index].Range(getrange(column=Const.CALLS_CHANGE_IN_OI, row=3)).Value = Const.CHANGE_IN_OI
        self.__sheet[index].Range(getrange(column=Const.PUTS_CHANGE_IN_OI, row=3)).Value = Const.CHANGE_IN_OI

        # TREND 1
        self.__sheet[index].Range(getrange(column=Const.CALLS_TREND1, row=3)).Value = Const.getTrends(1)
        self.__sheet[index].Range(getrange(column=Const.PUTS_TREND1, row=3)).Value = Const.getTrends(1)

        # TREND 2
        self.__sheet[index].Range(getrange(column=Const.CALLS_TREND2, row=3)).Value = Const.getTrends(2)
        self.__sheet[index].Range(getrange(column=Const.PUTS_TREND2, row=3)).Value = Const.getTrends(2)

        # TREND 3
        self.__sheet[index].Range(getrange(column=Const.CALLS_TREND3, row=3)).Value = Const.getTrends(3)
        self.__sheet[index].Range(getrange(column=Const.PUTS_TREND3, row=3)).Value = Const.getTrends(3)

        # STRIKE PRICE
        self.__sheet[index].Range(getrange(column=Const.EXCEL_STRIKE_PRICE_COLUMN, row=3)).Value = Const.STRIKE_PRICE

        # SET HEADING STYLE
        t = self.__sheet[index].Range(getrange(column='A', coloumn2='M', row=1, row2=3))
        t.Font.FontStyle = Const.BOLD
        t.Font.Size = Const.HEADING_SIZE

    def __settimestamp(self, index, price, time, date,marketstatus):
        optionname = Const.NIFTY_NAME if index == Const.NIFTY else Const.BANK_NIFTY_NAME
        self.__sheet[index].Range('A1').Value = optionname + " : " + str(price) + " as of " + time + " on " + date + (", Market has been closed" if marketstatus == False else "")
        return True

    def __setcellattributes(self,index,colunmname,attribute_data,row):
        t = self.__sheet[index].Range(getrange(column=colunmname,row=row))
        t.Value = attribute_data[Const.TEXT]
        if attribute_data[Const.CELL_FILL_COLOR] != None:
            t.Cells.interior.Color = attribute_data[Const.CELL_FILL_COLOR]
        else:
            t.Cells.interior.ColorIndex = attribute_data[Const.CELL_FILL_COLOR]
        t.Font.Color = attribute_data[Const.FONT_COLOR]
        t.Font.FontStyle = attribute_data[Const.FONT_STYLE]
        t.Font.size = attribute_data[Const.FONT_SIZE]

    def __setcalls(self,index,callsdata,row):
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.OI],
                                 colunmname=Const.CALLS_OI,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.CHANGE_IN_OI],
                                 colunmname=Const.CALLS_CHANGE_IN_OI,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.LTP],
                                 colunmname=Const.CALLS_LTP,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.TRENDS1],
                                 colunmname=Const.CALLS_TREND1,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.TRENDS2],
                                 colunmname=Const.CALLS_TREND2,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=callsdata[Const.TRENDS3],
                                 colunmname=Const.CALLS_TREND3,
                                 row=row)

    def __setputs(self,index,putsdata,row):
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.OI],
                                 colunmname=Const.PUTS_OI,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.CHANGE_IN_OI],
                                 colunmname=Const.PUTS_CHANGE_IN_OI,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.LTP],
                                 colunmname=Const.PUTS_LTP,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.TRENDS1],
                                 colunmname=Const.PUTS_TREND1,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.TRENDS2],
                                 colunmname=Const.PUTS_TREND2,
                                 row=row)
        self.__setcellattributes(index=index,
                                 attribute_data=putsdata[Const.TRENDS3],
                                 colunmname=Const.PUTS_TREND3,
                                 row=row)

    def __postdatainexcel(self, index, Data):
        strikes = Data[Const.EXCEL_STRIKES]
        for i in range(len(strikes)):
            row = i + 4
            data = Data[strikes[i]]
            self.__setcellattributes(index=index,
                                     attribute_data=data[Const.STRIKE_PRICE],
                                     colunmname=Const.EXCEL_STRIKE_PRICE_COLUMN,
                                     row=row)

            self.__setcalls(index=index,
                            row=row,
                            callsdata=data[Const.CALLS])

            self.__setputs(index=index,
                           row=row,
                           putsdata=data[Const.PUTS])

    def __posterror(self,error,index):
        s = ''
        if error == Const.NO_INTERNET:
            s = "Cannot connect to internet, check your connection"
        else:
            s = "Cannot retrieve data from site, site is not working"
        self.__errorcell[index][0].MergeCells = True
        self.__errorcell[index][1].value = s

    def __unposterror(self,index):
        self.__errorcell[index][0].MergeCells = True
        self.__errorcell[index][1].value = ''


    def postinexcel(self, data):
        self.__setconformationcell(text="updating...")
        #self.__wb.screen_updating = Const.VISIBLE_UPDATING
        #print("updating screen",xw.screen_updating)
        for index in (Const.NIFTY, Const.BANK_NIFTY):
            optiondata = data[index]
            if optiondata[Const.ERROR] != None:
                self.__setconformationcell(text="")
                self.__posterror(error=optiondata[Const.ERROR],index=index)
                #xw.screen_updating = True
                self.__save_file()
                return
            else:
                self.__unposterror(index=index)
            if self.__settimestamp(index=index,
                                   price=optiondata[Const.PRICE],
                                   time=optiondata[Const.TIME],
                                   date=optiondata[Const.DATE],
                                   marketstatus=optiondata[Const.MARKET_STATUS]):
                self.__postdatainexcel(index=index, Data=optiondata)
        #xw.screen_updating = True
        self.__setconformationcell(text="")
        self.__save_file()

    def __save_file(self):
        self.__wb.Save()
