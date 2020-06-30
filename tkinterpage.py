import time
from tkinter import *
from tkinter import font,ttk
from Constants import Constants as Const
import os
from DataRequest import DataRequest
from ExcelData import DataFormatter

url = "https://www.google.com"
iconpath = os.getcwd() + "\\logo.ico"


up = Const.UP
down = Const.DOWN
timeframe = 5
Const.REFRESH_TIME = timeframe
Const.TESTING = False
x = 10
main = Tk(className="Option-Chain Data")
main.iconbitmap(iconpath)
main.geometry("1071x510")

class optionindex:
    def __init__(self,root,index):
        self.index = index
        self.timer = 0
        self.starting = True
        self.stopped = False
        self.request = DataRequest(index=index)
        self.Dataformatter = DataFormatter(index=index)
        self.root=root
        self.frames = {}
        Table = LabelFrame(self.root, text="OPTION CHAIN DATA", bg=None)
        Table.pack()
        Headinglabel = Label(Table, text="PLEASE WAIT FOR FEW SECONDS, RELOADING AWM 😁😁")
        CALLS = LabelFrame(Table, text="CALLS")
        Strikeprice = LabelFrame(Table, text="STRIKE PRICE")
        PUTS = LabelFrame(Table, text="PUTS")
        Headinglabel.grid(row=0, column=0, columnspan=3)
        CALLS.grid(row=1, column=0)
        Strikeprice.grid(row=1, column=1)
        PUTS.grid(row=1, column=2)
        self.frames["heading"] = Headinglabel
        self.frames["body"] = []

        CALLSOI = LabelFrame(CALLS, text=Const.OI)
        CALLSOI.grid(row=0, column=Const.CALLS_OI)
        CALLSLTP = LabelFrame(CALLS, text=Const.LTP)
        CALLSLTP.grid(row=0, column=Const.CALLS_LTP)
        CALLSCOI = LabelFrame(CALLS, text=Const.CHANGE_IN_OI)
        CALLSCOI.grid(row=0, column=Const.CALLS_CHANGE_IN_OI)
        CALLSTREND1 = LabelFrame(CALLS, text=Const.getTrends(1))
        CALLSTREND1.grid(row=0, column=Const.CALLS_TREND1)
        CALLSTREND2 = LabelFrame(CALLS, text=Const.getTrends(2))
        CALLSTREND2.grid(row=0, column=Const.CALLS_TREND2)
        CALLSTREND3 = LabelFrame(CALLS, text=Const.getTrends(3))
        CALLSTREND3.grid(row=0, column=Const.CALLS_TREND3)

        PUTSOI = LabelFrame(PUTS, text=Const.OI)
        PUTSOI.grid(row=0, column=Const.PUTS_OI)
        PUTSLTP = LabelFrame(PUTS, text=Const.LTP)
        PUTSLTP.grid(row=0, column=Const.PUTS_LTP)
        PUTSCOI = LabelFrame(PUTS, text=Const.CHANGE_IN_OI)
        PUTSCOI.grid(row=0, column=Const.PUTS_CHANGE_IN_OI)
        PUTSTREND1 = LabelFrame(PUTS, text=Const.getTrends(1))
        PUTSTREND1.grid(row=0, column=Const.PUTS_TREND1)
        PUTSTREND2 = LabelFrame(PUTS, text=Const.getTrends(2))
        PUTSTREND2.grid(row=0, column=Const.PUTS_TREND2)
        PUTSTREND3 = LabelFrame(PUTS, text=Const.getTrends(3))
        PUTSTREND3.grid(row=0, column=Const.PUTS_TREND3)

        STrike = LabelFrame(Strikeprice, text=Const.STRIKE_PRICE)
        STrike.grid(row=0, column=Const.STRIKE_PRICE_COLUMN)

        # ROW
        for _ in range(up + down + 1):
            callsoi = Label(CALLSOI, text="-", width=x, height=1)
            callsltp = Label(CALLSLTP, text="-", width=x, height=1)
            callscoi = Label(CALLSCOI, text="-", width=x, height=1)
            callstrend1 = Label(CALLSTREND1, text="-", width=x, height=1)
            callstrend2 = Label(CALLSTREND2, text="-", width=x, height=1)
            callstrend3 = Label(CALLSTREND3, text="-", width=x, height=1)
            strike = Label(STrike, text="-", width=x, height=1)
            putsoi = Label(PUTSOI, text="-", width=x, height=1)
            putsltp = Label(PUTSLTP, text="-", width=x, height=1)
            putscoi = Label(PUTSCOI, text="-", width=x, height=1)
            putstrend1 = Label(PUTSTREND1, text="-", width=x, height=1)
            putstrend2 = Label(PUTSTREND2, text="-", width=x, height=1)
            putstrend3 = Label(PUTSTREND3, text="-", width=x, height=1)

            calls = {Const.OI: callsoi,
                     Const.LTP: callsltp,
                     Const.CHANGE_IN_OI: callscoi,
                     Const.TRENDS1: callstrend1,
                     Const.TRENDS2: callstrend2,
                     Const.TRENDS3: callstrend3}

            puts = {Const.OI: putsoi,
                    Const.LTP: putsltp,
                    Const.CHANGE_IN_OI: putscoi,
                    Const.TRENDS1: putstrend1,
                    Const.TRENDS2: putstrend2,
                    Const.TRENDS3: putstrend3}

            t = {Const.STRIKE_PRICE: strike, Const.CALLS: calls, Const.PUTS: puts}
            for i in t:
                if i == Const.STRIKE_PRICE:
                    t[i].pack(side=TOP)
                else:
                    for j in t[i]:
                        t[i][j].pack(side=TOP)
            self.frames["body"].append(t)

        # Extras
        options = LabelFrame(self.root, text="Extras", padx=100)
        options.pack(side=BOTTOM)
        self.Timer = Label(options, text="Strarting", width=15)
        self.Timer.pack(side=LEFT)
        self.start()

    def start(self):
        hr = time.strftime("%H")
        min = time.strftime("%M")
        sec = time.strftime("%S")
        self.Timer.config(text=hr + " : " + min + " : " + sec)
        if self.stopped == False:
            self.timer += 1
            if self.starting == True and self.timer == 5:
                self.updatedata()
                starting = False
            if (self.timer >= timeframe * 60):
                self.updatedata()
                self.timer = 0
            self.Timer.after(ms=1000, func=self.start)

    def setheading(self,time, date, price, marketstatus):
        optionname = Const.NIFTY_NAME if self.index == Const.NIFTY else Const.BANK_NIFTY_NAME
        s = optionname + " : " + str(price) + " as of " + time + " on " + date + (
            ", Market has been closed" if marketstatus == False else "")
        self.frames["heading"].config(text=s)

    def setattribute(self,data, label):
        label.config(
            text=data[Const.TEXT],
            bg=data[Const.CELL_FILL_COLOR],
            fg=data[Const.FONT_COLOR],
            font=font.Font(weight=data[Const.FONT_STYLE], size=data[Const.FONT_SIZE]))

    def setrowvalue(self,data, frame):
        self.setattribute(data=data[Const.OI], label=frame[Const.OI])
        self.setattribute(data=data[Const.LTP], label=frame[Const.LTP])
        self.setattribute(data=data[Const.CHANGE_IN_OI], label=frame[Const.CHANGE_IN_OI])
        self.setattribute(data=data[Const.TRENDS1], label=frame[Const.TRENDS1])
        self.setattribute(data=data[Const.TRENDS2], label=frame[Const.TRENDS2])
        self.setattribute(data=data[Const.TRENDS3], label=frame[Const.TRENDS3])

    def updatedata(self):
        global stopped
        data = self.Dataformatter.update_data(self.request.request_data)
        if data[Const.ERROR] != None:
            print("No network")
            return
        if data[Const.MARKET_STATUS] == False:
            stopped = True
        self.setheading(price=data[Const.PRICE],
                   time=data[Const.TIME],
                   date=data[Const.DATE],
                   marketstatus=data[Const.MARKET_STATUS])
        strikeprices = data[Const.STRIKES_LIST]
        for i in range(len(strikeprices)):
            Data = data[strikeprices[i]]
            self.setattribute(data=Data[Const.STRIKE_PRICE], label=self.frames["body"][i][Const.STRIKE_PRICE])
            self.setrowvalue(data=Data[Const.CALLS], frame=self.frames["body"][i][Const.CALLS])
            self.setrowvalue(data=Data[Const.PUTS], frame=self.frames["body"][i][Const.PUTS])

class Optionchaindataset:
    def __init__(self,index,root,packside):
        self.__index = index
        self.__root=root
        self.__name=Const.NIFTY_NAME if self.__index == Const.NIFTY else Const.BANK_NIFTY_NAME
        frame = LabelFrame(master=self.__root, text=self.__name, width=535, height=483)
        frame.pack(side=packside, expand=1, fill="both")


class HomePage:
    def __init__(self,root):
        self.__root=root
        Homepage = Frame(root, width=1071, height=483)
        Optionchaindataset(root=root,index=Const.NIFTY,packside=LEFT)
        Optionchaindataset(root=root,index=Const.BANK_NIFTY,packside=RIGHT)
        Homepage.pack(fill="both", expand=1)

my_notebook = ttk.Notebook(main)
my_notebook.pack()

Homepage = Frame(my_notebook,width=1071,height=483)
Homepageobject = HomePage(root=Homepage)
Homepage.pack(fill="both",expand=1)
my_notebook.add(Homepage,text="HOME PAGE")

NiftyPage = Frame(my_notebook,width=1071,height=483)
niftypageobject = optionindex(root=NiftyPage,index=Const.NIFTY)
NiftyPage.pack(fill="both",expand=1)
my_notebook.add(NiftyPage,text="NIFTY")

BankNiftyPage = Frame(my_notebook,width=1071,height=483)
bankniftypageobject = optionindex(root=BankNiftyPage,index=Const.BANK_NIFTY)
BankNiftyPage.pack(fill="both",expand=1)
my_notebook.add(BankNiftyPage,text="BANK NIFTY")

main.mainloop()
