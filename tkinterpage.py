import time
from tkinter import *
from tkinter import font,ttk
from Constants import Constants as Const
import os
from DataRequest import DataRequest
from ExcelData import DataFormatter

url = "https://www.google.com"
iconpath = os.getcwd() + "\\logo.ico"

padyvalue=7
entrywidth = 10
timeframe = 5
Const.REFRESH_TIME = timeframe
Const.TESTING = False
x = 10
main = Tk(className="Option-Chain Data")
main.iconbitmap(iconpath)
main.geometry("1071x510+100+100")

Pack = lambda obj : obj.pack(fill="both",expand=1)

class optionsextra:
    def __init__(self,root,update):
        self.root = root

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
        up = Const.UP[index]
        down = Const.DOWN[index]
        Table = LabelFrame(self.root, text="OPTION CHAIN DATA", bg=None)
        Table.pack()
        Headinglabel = Label(Table, text="PLEASE WAIT FOR FEW SECONDS, RELOADING AWM 😁😁")
        CALLS = LabelFrame(Table, text="CALLS")
        Strikeprice = LabelFrame(Table, text="STRIKE PRICE")
        PUTS = LabelFrame(Table, text="PUTS")
        Headinglabel.grid(row=0, column=0, columnspan=3)
        CALLS.grid(row=1, column=Const.CALLS_POS[index])
        Strikeprice.grid(row=1, column=Const.STRIKEPRICE_POS[index])
        PUTS.grid(row=1, column=Const.PUTS_POS[index])
        self.frames["heading"] = Headinglabel
        self.frames["body"] = []

        CALLSOI = LabelFrame(CALLS, text=Const.OI)
        CALLSOI.grid(row=0, column=Const.CALLS_OI[index])
        CALLSLTP = LabelFrame(CALLS, text=Const.LTP)
        CALLSLTP.grid(row=0, column=Const.CALLS_LTP[index])
        CALLSCOI = LabelFrame(CALLS, text=Const.CHANGE_IN_OI)
        CALLSCOI.grid(row=0, column=Const.CALLS_CHANGE_IN_OI[index])
        CALLSTREND1 = LabelFrame(CALLS, text=Const.getTrends(1))
        CALLSTREND1.grid(row=0, column=Const.CALLS_TREND1[index])
        CALLSTREND2 = LabelFrame(CALLS, text=Const.getTrends(2))
        CALLSTREND2.grid(row=0, column=Const.CALLS_TREND2[index])
        CALLSTREND3 = LabelFrame(CALLS, text=Const.getTrends(3))
        CALLSTREND3.grid(row=0, column=Const.CALLS_TREND3[index])

        PUTSOI = LabelFrame(PUTS, text=Const.OI)
        PUTSOI.grid(row=0, column=Const.PUTS_OI[index])
        PUTSLTP = LabelFrame(PUTS, text=Const.LTP)
        PUTSLTP.grid(row=0, column=Const.PUTS_LTP[index])
        PUTSCOI = LabelFrame(PUTS, text=Const.CHANGE_IN_OI)
        PUTSCOI.grid(row=0, column=Const.PUTS_CHANGE_IN_OI[index])
        PUTSTREND1 = LabelFrame(PUTS, text=Const.getTrends(1))
        PUTSTREND1.grid(row=0, column=Const.PUTS_TREND1[index])
        PUTSTREND2 = LabelFrame(PUTS, text=Const.getTrends(2))
        PUTSTREND2.grid(row=0, column=Const.PUTS_TREND2[index])
        PUTSTREND3 = LabelFrame(PUTS, text=Const.getTrends(3))
        PUTSTREND3.grid(row=0, column=Const.PUTS_TREND3[index])

        STrike = LabelFrame(Strikeprice, text=Const.STRIKE_PRICE)
        STrike.grid(row=0, column=0)

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
        options = LabelFrame(self.root, text="Controller", padx=100)
        self.Timer = Label(options, text="Strarting", width=15)
        self.Timer.pack(side=LEFT)
        options.pack(side=BOTTOM)
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
                self.starting = False
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
        data = self.Dataformatter.update_data(self.request.request_data)
        if data[Const.ERROR] != None:
            print("No network")
            return
        if data[Const.MARKET_STATUS] == False:
            self.stopped = True
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
        name=Const.NIFTY_NAME if self.__index == Const.NIFTY else Const.BANK_NIFTY_NAME
        frame = LabelFrame(master=root, text=name, width=535, height=483)
        self.upperframe = Frame(master=frame)
        self.setupupperframe(root=self.upperframe)
        lowerframe = Frame(master=frame)
        self.setuplowerframe(root=lowerframe)
        self.upperframe.pack(side=TOP)
        lowerframe.pack(side=BOTTOM)
        frame.pack(side=packside, expand=1, fill="both")

    def butpressed(self):
        pass

    def setvalues(self):
        pass

    def setuplowerframe(self,root):
        # TODO: RESET values
        Button(master=root,text="RESET").pack(side = LEFT,pady=40,padx=25)
        # TODO: SAVE values
        Button(master=root, text="SAVE").pack(side=LEFT, pady=40, padx=25)
        # TODO: RESTORE values
        Button(master=root, text="RESTORE").pack(side=LEFT, pady=40, padx=25)
        # TODO: START
        Button(master=root, text="START").pack(side=LEFT, pady=40, padx=25)

    def setupupperframe(self,root):
        timeframelabel=Label(master=root,text="TIME FRAME")
        self.timeframeentry = Entry(master=root,width=entrywidth)
        callslabel = Label(master=root,text="CALLS")
        self.callsentry = Entry(master=root,width=entrywidth)
        strikepricelabel = Label(master=root,text="STRIKE PRICE")
        self.strikepriceentry = Entry(master=root,width=entrywidth)
        putslabel = Label(master=root,text="PUTS")
        self.putsentry = Entry(master=root,width=entrywidth)

        callsoilabel = Label(master=root,text=Const.OI)
        self.callsoientry = Entry(master=root,width=entrywidth)
        callsltplabel = Label(master=root,text=Const.LTP)
        self.callsltpentry = Entry(master=root,width=entrywidth)
        callscoilabel = Label(master=root,text=Const.CHANGE_IN_OI)
        self.callscoientry = Entry(master=root,width=entrywidth)
        callstrend1label = Label(master=root,text=Const.TRENDS1)
        self.callstrend1entry = Entry(master=root,width=entrywidth)
        callstrend2label = Label(master=root, text=Const.TRENDS2)
        self.callstrend2entry = Entry(master=root,width=entrywidth)
        callstrend3label = Label(master=root, text=Const.TRENDS2)
        self.callstrend3entry = Entry(master=root,width=entrywidth)

        putsoilabel = Label(master=root, text=Const.OI)
        self.putsoientry = Entry(master=root,width=entrywidth)
        putsltplabel = Label(master=root, text=Const.LTP)
        self.putsltpentry = Entry(master=root,width=entrywidth)
        putscoilabel = Label(master=root, text=Const.CHANGE_IN_OI)
        self.putscoientry = Entry(master=root,width=entrywidth)
        putstrend1label = Label(master=root, text=Const.TRENDS1)
        self.putstrend1entry = Entry(master=root,width=entrywidth)
        putstrend2label = Label(master=root, text=Const.TRENDS2)
        self.putstrend2entry = Entry(master=root,width=entrywidth)
        putstrend3label = Label(master=root, text=Const.TRENDS2)
        self.putstrend3entry = Entry(master=root,width=entrywidth)

        upvalueslabel = Label(master=root,text="UP VALUES")
        self.upvaluesentry = Entry(master=root,width=entrywidth)
        downvalueslabel = Label(master=root,text="DOWN VALUES")
        self.downvaluesentry = Entry(master=root,width=entrywidth)

        timeframelabel.grid(row=0,column=0,pady=padyvalue)
        callslabel.grid(row=1,column=0,pady=padyvalue)
        strikepricelabel.grid(row=1,column=2,pady=padyvalue)
        putslabel.grid(row=1,column=4,pady=padyvalue)
        callsoilabel.grid(row=2,column=0,pady=padyvalue)
        callscoilabel.grid(row=4,column=0,pady=padyvalue)
        callsltplabel.grid(row=3,column=0,pady=padyvalue)
        callstrend1label.grid(row=5,column=0,pady=padyvalue)
        callstrend2label.grid(row=6,column=0,pady=padyvalue)
        callstrend3label.grid(row=7,column=0,pady=padyvalue)
        putsoilabel.grid(row=2,column=4,pady=padyvalue)
        putscoilabel.grid(row=4,column=4,pady=padyvalue)
        putsltplabel.grid(row=3,column=4,pady=padyvalue)
        putstrend1label.grid(row=5,column=4,pady=padyvalue)
        putstrend2label.grid(row=6,column=4,pady=padyvalue)
        putstrend3label.grid(row=7,column=4,pady=padyvalue)
        upvalueslabel.grid(row=8,column=0,pady=padyvalue)
        downvalueslabel.grid(row=8,column=3,pady=padyvalue)

        self.timeframeentry.grid(row=0,column=1,pady=padyvalue)
        self.callsentry.grid(row=1,column=1,pady=padyvalue)
        self.putsentry.grid(row=1,column=5,pady=padyvalue)
        self.strikepriceentry.grid(row=1,column=3,pady=padyvalue)
        self.callsoientry.grid(row=2,column=1,pady=padyvalue)
        self.callscoientry.grid(row=4,column=1,pady=padyvalue)
        self.callsltpentry.grid(row=3,column=1,pady=padyvalue)
        self.callstrend1entry.grid(row=5,column=1,pady=padyvalue)
        self.callstrend2entry.grid(row=6,column=1,pady=padyvalue)
        self.callstrend3entry.grid(row=7,column=1,pady=padyvalue)
        self.putsoientry.grid(row=2,column=5,pady=padyvalue)
        self.putscoientry.grid(row=4,column=5,pady=padyvalue)
        self.putsltpentry.grid(row=3,column=5,pady=padyvalue)
        self.putstrend1entry.grid(row=5,column=5,pady=padyvalue)
        self.putstrend2entry.grid(row=6,column=5,pady=padyvalue)
        self.putstrend3entry.grid(row=7,column=5,pady=padyvalue)
        self.upvaluesentry.grid(row=8,column=1,pady=padyvalue)
        self.downvaluesentry.grid(row=8,column=4,pady=padyvalue)


class Homemiddlepage:
    def __init__(self,t,root):
        self.__root = root
        self.__t = t
        self.__enabled=True
        frame = Frame(root)
        but = Checkbutton(master=frame, text="Same as Nifty",command=self.butpressed)
        but.pack(side=TOP,padx=10,pady=10)
        # TODO: save both
        Button(master=frame, text="SAVE BOTH").pack(side=TOP, padx=10, pady=10)
        # TODO: reset both
        Button(master=frame, text="RESET BOTH").pack(side=TOP, padx=10, pady=10)
        # TODO: start both
        Button(master=frame, text="START BOTH").pack(side=TOP, padx=10, pady=10)
        Button(master=frame,text="QUIT",command=main.quit).pack(side=TOP,padx=10,pady=10)
        frame.pack(side = LEFT,expand=1,fill="both")

    def butpressed(self):
        self.__enabled = not self.__enabled
        enabler = 'normal'
        if self.__enabled != True:
            enabler = 'disabled'
        print(enabler)
        for child in self.__t.upperframe.winfo_children():
            child.configure(state=enabler)

class HomePage:
    def __init__(self,root):
        self.__root=root
        Homepage = Frame(root, width=1071, height=483)
        nifty = Optionchaindataset(root=Homepage,index=Const.NIFTY,packside=LEFT)
        banknifty = Optionchaindataset(root=Homepage, index=Const.BANK_NIFTY, packside=RIGHT)
        Homemiddlepage(root=Homepage,t=banknifty)
        Pack(Homepage)

my_notebook = ttk.Notebook(main)
my_notebook.pack()

Homepage = Frame(my_notebook,width=1071,height=483)
Homepageobject = HomePage(root=Homepage)
Pack(Homepage)
my_notebook.add(Homepage,text="HOME PAGE")

NiftyPage = Frame(my_notebook,width=1071,height=483)
niftypageobject = optionindex(root=NiftyPage,index=Const.NIFTY)
Pack(NiftyPage)
my_notebook.add(NiftyPage,text="NIFTY")

BankNiftyPage = Frame(my_notebook,width=1071,height=483)
bankniftypageobject = optionindex(root=BankNiftyPage,index=Const.BANK_NIFTY)
Pack(BankNiftyPage)
my_notebook.add(BankNiftyPage,text="BANK NIFTY")

main.mainloop()
