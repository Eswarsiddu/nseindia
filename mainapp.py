getname = lambda index: Const.NIFTY_NAME if index == Const.NIFTY else Const.BANK_NIFTY_NAME


def getsizeandpos(height,width):
    screenheight = main.winfo_screenheight()
    screenwidth = main.winfo_screenwidth()
    posy = int(screenheight/2 - height/2)
    posx = int(screenwidth/2 - width/2)
    s = str(width)+"x"+str(height)+"+"+str(posx)+"+"+str(posy)
    print(s)
    return s


class optionscontroller:
    def __init__(self, root, update, index, datareset):
        self.updatedata = update
        self.datareset = datareset
        self.root = root
        self.stopped = None
        self.starting = True
        self.index = index
        self.timeframe = Const.REFRESH_TIME[index] * 60
        self.timer = self.timeframe
        controller = LabelFrame(self.root, text="Controller", padx=100)
        self.__setcontroller(root=controller)
        controller.pack(side=BOTTOM)

    def __setcontroller(self, root):
        self.Timer = Label(root, text="Press start", width=15)
        self.startbut = Button(root, text="START", state=NORMAL, command=self.startpressed)
        self.stopbut = Button(root, text="STOP", state=DISABLED, command=self.stoppressed)
        self.errorlabel = Label(root,text="")
        self.Timer.pack(sid=LEFT, padx=10)
        self.startbut.pack(side=LEFT, padx=10)
        self.stopbut.pack(side=LEFT, padx=10)
        self.errorlabel.pack(side=LEFT,padx=10)

    # TODO: INDEX STOP PRESSED
    def stoppressed(self):
        self.stopbut.config(state=DISABLED)
        self.startbut.config(state=NORMAL)
        self.stopped = True
        my_notebook.tab(self.index+1,text=getname(index=self.index))

    # TODO: INDEX STAT PRESSED
    def startpressed(self):
        self.startbut.config(state=DISABLED)
        self.stopbut.config(state=NORMAL)
        self.starting = True
        self.stopped = False
        self.datareset()
        self.timer=0
        self.__start()

    def __start(self):
        self.Timer.config(text=time.strftime("%H : %M: %S", time.gmtime(self.timer)))
        if self.stopped == False:
            self.timer -= 1
            if (self.timer <= 0):
                self.updatedata()
                self.timer = self.timeframe
            self.Timer.after(ms=1000, func=self.__start)


class optionindex:
    def __init__(self, root, index):
        self.index = index
        self.request = DataRequest(index=index)
        self.Dataformatter = DataFormatter(index=index)
        self.root = root
        self.up = Const.UP[index]
        self.down = Const.DOWN[index]
        Table = LabelFrame(self.root, text="OPTION CHAIN DATA", bg=None)
        Headinglabel = Label(Table, text="NOT YET STARTED")
        Headinglabel.grid(row=0, column=0, columnspan=3)
        self.CALLS = LabelFrame(Table, text="CALLS")
        self.Strikeprice = LabelFrame(Table, text="STRIKE PRICE")
        self.PUTS = LabelFrame(Table, text="PUTS")
        self.frames = {}
        self.frames[Const.HEADING] = Headinglabel
        self.frames[Const.BODY] = []

        self.CALLSOI = LabelFrame(self.CALLS, text=Const.OI)
        self.CALLSLTP = LabelFrame(self.CALLS, text=Const.LTP)
        self.CALLSCOI = LabelFrame(self.CALLS, text=Const.CHANGE_IN_OI)
        self.CALLSTREND1 = LabelFrame(self.CALLS, text=Const.getTrends(i=1, index=index))
        self.CALLSTREND2 = LabelFrame(self.CALLS, text=Const.getTrends(i=2, index=index))
        self.CALLSTREND3 = LabelFrame(self.CALLS, text=Const.getTrends(i=3, index=index))

        self.PUTSOI = LabelFrame(self.PUTS, text=Const.OI)
        self.PUTSLTP = LabelFrame(self.PUTS, text=Const.LTP)
        self.PUTSCOI = LabelFrame(self.PUTS, text=Const.CHANGE_IN_OI)
        self.PUTSTREND1 = LabelFrame(self.PUTS, text=Const.getTrends(i=1, index=index))
        self.PUTSTREND2 = LabelFrame(self.PUTS, text=Const.getTrends(i=2, index=index))
        self.PUTSTREND3 = LabelFrame(self.PUTS, text=Const.getTrends(i=3, index=index))

        self.Strike = LabelFrame(self.Strikeprice, text=Const.STRIKE_PRICE)
        self.Strike.grid(row=0, column=0)


        self.setcolumnpositions()
        self.loadrows()
        Table.pack()
        # TODO: Controller
        self.Controller = optionscontroller(root=self.root, update=self.updatedata, index=index,
                                       datareset=self.request.reset_data)
        self.Controller.stopped = False
        self.frames[Const.ERROR]=self.Controller.errorlabel

    def setcolumnpositions(self):
        self.CALLS.grid(row=1, column=Const.CALLS_POS[self.index])
        self.Strikeprice.grid(row=1, column=Const.STRIKEPRICE_POS[self.index])
        self.PUTS.grid(row=1, column=Const.PUTS_POS[self.index])

        self.CALLSOI.grid(row=0, column=Const.CALLS_OI[self.index])
        self.CALLSLTP.grid(row=0, column=Const.CALLS_LTP[self.index])
        self.CALLSCOI.grid(row=0, column=Const.CALLS_CHANGE_IN_OI[self.index])
        self.CALLSTREND1.grid(row=0, column=Const.CALLS_TREND1[self.index])
        self.CALLSTREND2.grid(row=0, column=Const.CALLS_TREND2[self.index])
        self.CALLSTREND3.grid(row=0, column=Const.CALLS_TREND3[self.index])

        self.PUTSOI.grid(row=0, column=Const.PUTS_OI[self.index])
        self.PUTSLTP.grid(row=0, column=Const.PUTS_LTP[self.index])
        self.PUTSCOI.grid(row=0, column=Const.PUTS_CHANGE_IN_OI[self.index])
        self.PUTSTREND1.grid(row=0, column=Const.PUTS_TREND1[self.index])
        self.PUTSTREND2.grid(row=0, column=Const.PUTS_TREND2[self.index])
        self.PUTSTREND3.grid(row=0, column=Const.PUTS_TREND3[self.index])

    def loadrows(self):
        presentcount = len(self.frames[Const.BODY])
        requestedcount = self.up + self.down + 1
        requiredrows = requestedcount-presentcount
        if requiredrows < 0:
            self.__removerows(rows=abs(requiredrows))
        elif requiredrows > 0:
            self.__addrows(rows=abs(requiredrows))

    def __addrows(self,rows):
        labelwidth = 10
        for _ in range(rows):
            t = {Const.STRIKE_PRICE: Label(self.Strike, text="-", width=labelwidth, height=1),
                 Const.CALLS: {Const.OI: Label(self.CALLSOI, text="-", width=labelwidth, height=1),
                               Const.LTP: Label(self.CALLSLTP, text="-", width=labelwidth, height=1),
                               Const.CHANGE_IN_OI: Label(self.CALLSCOI, text="-", width=labelwidth, height=1),
                               Const.TRENDS1: Label(self.CALLSTREND1, text="-", width=labelwidth, height=1),
                               Const.TRENDS2: Label(self.CALLSTREND2, text="-", width=labelwidth, height=1),
                               Const.TRENDS3: Label(self.CALLSTREND3, text="-", width=labelwidth, height=1)},
                 Const.PUTS: {Const.OI: Label(self.PUTSOI, text="-", width=labelwidth, height=1),
                              Const.LTP: Label(self.PUTSLTP, text="-", width=labelwidth, height=1),
                              Const.CHANGE_IN_OI: Label(self.PUTSCOI, text="-", width=labelwidth, height=1),
                              Const.TRENDS1: Label(self.PUTSTREND1, text="-", width=labelwidth, height=1),
                              Const.TRENDS2: Label(self.PUTSTREND2, text="-", width=labelwidth, height=1),
                              Const.TRENDS3: Label(self.PUTSTREND3, text="-", width=labelwidth, height=1)}}
            for i in t:
                if i == Const.STRIKE_PRICE:
                    t[i].pack(side=TOP)
                else:
                    for j in t[i]:
                        t[i][j].pack(side=TOP)
            self.frames[Const.BODY].append(t)

    def __removerows(self,rows):
        for _ in range(rows):
            t = self.frames[Const.BODY][-1]
            for i in t:
                if i == Const.STRIKE_PRICE:
                    t[i].pack_forget()
                    t[i].destroy()
                else:
                    for j in t[i]:
                        t[i][j].pack_forget()
                        t[i][j].destroy()
            self.frames[Const.BODY].pop(-1)



    def __setheading(self, Time, date, price, marketstatus):
        optionname = getname(index=self.index)
        s = optionname + " " + str(price)
        my_notebook.tab(self.index + 1, text=s)
        s = optionname + " : " + str(price) + " as of " + Time + " on " + date + (
            ", Market has been closed" if marketstatus == False else "")
        self.frames[Const.HEADING].config(text=s)

    def __setattribute(self, data, label):
        label.config(
            text=data[Const.TEXT],
            bg=data[Const.CELL_FILL_COLOR],
            fg=data[Const.FONT_COLOR],
            font=font.Font(weight=data[Const.FONT_STYLE], size=data[Const.FONT_SIZE]))

    def __setrowvalue(self, data, frame):
        self.__setattribute(data=data[Const.OI], label=frame[Const.OI])
        self.__setattribute(data=data[Const.LTP], label=frame[Const.LTP])
        self.__setattribute(data=data[Const.CHANGE_IN_OI], label=frame[Const.CHANGE_IN_OI])
        self.__setattribute(data=data[Const.TRENDS1], label=frame[Const.TRENDS1])
        self.__setattribute(data=data[Const.TRENDS2], label=frame[Const.TRENDS2])
        self.__setattribute(data=data[Const.TRENDS3], label=frame[Const.TRENDS3])

    def updatedata(self):
        data = self.Dataformatter.update_data(self.request.request_data)
        if data[Const.ERROR] != None:
            if data[Const.ERROR] == Const.NO_INTERNET:
                self.frames[Const.ERROR].config(text="NO INTERNET, CHECK YOUR CONNECTION",width = 50)
            else:
                self.frames[Const.ERROR].config(text="Site is Not Working",width = 30)
            return
        else:
            self.frames[Const.ERROR].config(text="", width=0)
        # TODO: ENABLE WHEN MARKET IS CLOSED
        # if data[Const.MARKET_STATUS] == False:
        #     self.Extras.stopped = True
        self.__setheading(price=data[Const.PRICE],
                        Time=data[Const.TIME],
                        date=data[Const.DATE],
                        marketstatus=data[Const.MARKET_STATUS])
        strikeprices = data[Const.STRIKES_LIST]
        for i in range(len(strikeprices)):
            Data = data[strikeprices[i]]
            self.__setattribute(data=Data[Const.STRIKE_PRICE], label=self.frames[Const.BODY][i][Const.STRIKE_PRICE])
            self.__setrowvalue(data=Data[Const.CALLS], frame=self.frames[Const.BODY][i][Const.CALLS])
            self.__setrowvalue(data=Data[Const.PUTS], frame=self.frames[Const.BODY][i][Const.PUTS])


class Optionchaindataset:
    def __init__(self, index, root, packside):
        self.__index = index
        name = getname(index=index)
        frame = LabelFrame(master=root, text=name, width=535, height=483)
        upperframe = Frame(master=frame)
        lowerframe = Frame(master=frame)
        self.__setupupperframe(root=upperframe)
        self.__setuplowerframe(root=lowerframe)
        upperframe.pack(side=TOP)
        lowerframe.pack(side=BOTTOM)
        frame.pack(side=packside, expand=1, fill="both")

    # TODO: SET VALUES
    def __setvalues(self):
        pass

    def __setuplowerframe(self, root):
        lowerpady = 40
        lowerpadx = 1
        self.resetbut = Button(master=root, text="RESET",command=self.resetpressed)
        self.resetbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.savebut = Button(master=root, text="SAVE",command = self.savepressed)
        self.savebut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.restorebut = Button(master=root, text="RESTORE",command = self.restorepressed)
        self.restorebut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.loadbut = Button(master=root, text="LOAD",command = self.loadpressed)
        self.loadbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.startbut = Button(master=root, text="START", command=self.startpressed,state=NORMAL)
        self.startbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.stopbut = Button(master=root, text="STOP", command=self.stoppressed,state=DISABLED)
        self.stopbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)

    # TODO: RESET SINGLE
    def resetpressed(self):
        pass

    # TODO: SAVE SINGLE
    def savepressed(self):
        pass

    # TODO: RESTORE SINGLE
    def restorepressed(self):
        pass

    # TODO: LOAD SINGLE
    def loadpressed(self):
        pass

    # TODO: START SINGLE
    def startpressed(self):
        self.startbut.config(state=DISABLED)
        self.stopbut.config(state=NORMAL)
        print("screenheight:",main.winfo_screenheight(),main.winfo_screenwidth())
        # TODO: changing the geometry
        # main.geometry("1253x600+100+100")

    def stoppressed(self):
        self.startbut.config(state=NORMAL)
        self.stopbut.config(state=DISABLED)


    def __setupupperframe(self, root):
        padyvalue = 7
        entrywidth = 10
        timeframelabel = Label(master=root, text="TIME FRAME")
        self.timeframeentry = Entry(master=root, width=entrywidth)
        callslabel = Label(master=root, text="CALLS")
        self.callsentry = Entry(master=root, width=entrywidth)
        strikepricelabel = Label(master=root, text="STRIKE PRICE")
        self.strikepriceentry = Entry(master=root, width=entrywidth)
        putslabel = Label(master=root, text="PUTS")
        self.putsentry = Entry(master=root, width=entrywidth)

        callsoilabel = Label(master=root, text=Const.OI)
        self.callsoientry = Entry(master=root, width=entrywidth)
        callsltplabel = Label(master=root, text=Const.LTP)
        self.callsltpentry = Entry(master=root, width=entrywidth)
        callscoilabel = Label(master=root, text=Const.CHANGE_IN_OI)
        self.callscoientry = Entry(master=root, width=entrywidth)
        callstrend1label = Label(master=root, text=Const.TRENDS1)
        self.callstrend1entry = Entry(master=root, width=entrywidth)
        callstrend2label = Label(master=root, text=Const.TRENDS2)
        self.callstrend2entry = Entry(master=root, width=entrywidth)
        callstrend3label = Label(master=root, text=Const.TRENDS2)
        self.callstrend3entry = Entry(master=root, width=entrywidth)

        putsoilabel = Label(master=root, text=Const.OI)
        self.putsoientry = Entry(master=root, width=entrywidth)
        putsltplabel = Label(master=root, text=Const.LTP)
        self.putsltpentry = Entry(master=root, width=entrywidth)
        putscoilabel = Label(master=root, text=Const.CHANGE_IN_OI)
        self.putscoientry = Entry(master=root, width=entrywidth)
        putstrend1label = Label(master=root, text=Const.TRENDS1)
        self.putstrend1entry = Entry(master=root, width=entrywidth)
        putstrend2label = Label(master=root, text=Const.TRENDS2)
        self.putstrend2entry = Entry(master=root, width=entrywidth)
        putstrend3label = Label(master=root, text=Const.TRENDS2)
        self.putstrend3entry = Entry(master=root, width=entrywidth)

        upvalueslabel = Label(master=root, text="UP VALUES")
        self.upvaluesentry = Entry(master=root, width=entrywidth)
        downvalueslabel = Label(master=root, text="DOWN VALUES")
        self.downvaluesentry = Entry(master=root, width=entrywidth)

        self.errorLabel = Label(master=root,text="")

        timeframelabel.grid(row=0, column=0, pady=padyvalue)
        callslabel.grid(row=1, column=0, pady=padyvalue)
        strikepricelabel.grid(row=1, column=2, pady=padyvalue)
        putslabel.grid(row=1, column=4, pady=padyvalue)
        callsoilabel.grid(row=2, column=0, pady=padyvalue)
        callscoilabel.grid(row=4, column=0, pady=padyvalue)
        callsltplabel.grid(row=3, column=0, pady=padyvalue)
        callstrend1label.grid(row=5, column=0, pady=padyvalue)
        callstrend2label.grid(row=6, column=0, pady=padyvalue)
        callstrend3label.grid(row=7, column=0, pady=padyvalue)
        putsoilabel.grid(row=2, column=4, pady=padyvalue)
        putscoilabel.grid(row=4, column=4, pady=padyvalue)
        putsltplabel.grid(row=3, column=4, pady=padyvalue)
        putstrend1label.grid(row=5, column=4, pady=padyvalue)
        putstrend2label.grid(row=6, column=4, pady=padyvalue)
        putstrend3label.grid(row=7, column=4, pady=padyvalue)
        upvalueslabel.grid(row=8, column=0, pady=padyvalue)
        downvalueslabel.grid(row=8, column=3, pady=padyvalue)

        self.timeframeentry.grid(row=0, column=1, pady=padyvalue)
        self.callsentry.grid(row=1, column=1, pady=padyvalue)
        self.putsentry.grid(row=1, column=5, pady=padyvalue)
        self.strikepriceentry.grid(row=1, column=3, pady=padyvalue)
        self.callsoientry.grid(row=2, column=1, pady=padyvalue)
        self.callscoientry.grid(row=4, column=1, pady=padyvalue)
        self.callsltpentry.grid(row=3, column=1, pady=padyvalue)
        self.callstrend1entry.grid(row=5, column=1, pady=padyvalue)
        self.callstrend2entry.grid(row=6, column=1, pady=padyvalue)
        self.callstrend3entry.grid(row=7, column=1, pady=padyvalue)
        self.putsoientry.grid(row=2, column=5, pady=padyvalue)
        self.putscoientry.grid(row=4, column=5, pady=padyvalue)
        self.putsltpentry.grid(row=3, column=5, pady=padyvalue)
        self.putstrend1entry.grid(row=5, column=5, pady=padyvalue)
        self.putstrend2entry.grid(row=6, column=5, pady=padyvalue)
        self.putstrend3entry.grid(row=7, column=5, pady=padyvalue)
        self.upvaluesentry.grid(row=8, column=1, pady=padyvalue)
        self.downvaluesentry.grid(row=8, column=4, pady=padyvalue)
        self.errorLabel.grid(row=9,column=0,columnspan=6,pady=padyvalue)


class Homemiddlepage:
    def __init__(self, banknifty, nifty, root):
        self.__banknifty = banknifty
        self.__nifty = nifty
        self.__enabled = True
        padx=10
        pady=10
        frame = Frame(root)
        Checkbutton(master=frame, text="Same as Nifty", command=self.sameasniftypressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="RESET BOTH", command=self.resetpressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="SAVE BOTH",command=self.savepressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="RESTORE BOTH", command=self.restorepressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="LOAD BOTH",command=self.loadpressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="STOP BOTH",command=self.stoppressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="START BOTH",command=self.startpressed).pack(side=TOP, padx=padx, pady=pady)
        Button(master=frame, text="QUIT", command=main.quit).pack(side=TOP, padx=padx, pady=pady)
        frame.pack(side=LEFT, expand=1, fill="both")

    def restorepressed(self):
        self.__nifty.restorepressed()
        self.__banknifty.restorepressed()

    # TODO: start both
    def startpressed(self):
        pass

    # TODO: stop both
    def stoppressed(self):
        pass

    def loadpressed(self):
        self.__nifty.loadpressed()
        self.__banknifty.loadpressed()

    def resetpressed(self):
        self.__nifty.resetpressed()
        self.__banknifty.loadpressed()

    def savepressed(self):
        self.__nifty.savepressed()
        self.__banknifty.savepressed()

    # TODO: SAME AS NIFTY
    def sameasniftypressed(self):
        self.__enabled = not self.__enabled
        enabler = 'normal'
        if self.__enabled != True:
            enabler = 'disabled'
        print(enabler)
        for child in self.__banknifty.upperframe.winfo_children():
            child.configure(state=enabler)


class HomePage:
    def __init__(self, root):
        self.__root = root
        Homepage = Frame(root, width=1071, height=483)
        nifty = Optionchaindataset(root=Homepage, index=Const.NIFTY, packside=LEFT)
        banknifty = Optionchaindataset(root=Homepage, index=Const.BANK_NIFTY, packside=RIGHT)
        Homemiddlepage(root=Homepage, banknifty=banknifty,nifty=nifty)
        Homepage.pack(fill="both", expand=1)

if __name__ == "__main__":
    import time
    from tkinter import *
    from tkinter import font, ttk
    import os, platform
    from DataRequest import DataRequest
    from ExcelData import DataFormatter
    from Constants import Constants as Const

    Const.REFRESH_TIME = [5, 5]
    Const.TESTING = False

    main = Tk(className="Option-Chain Data")
    if platform.system() == "Windows": main.wm_iconbitmap(os.getcwd() + "/logo.ico")
    main.geometry(getsizeandpos(width=1240, height=550))
    my_notebook = ttk.Notebook(main)

    NiftyPage = Frame(my_notebook, width=1071, height=483)
    niftypageobject = optionindex(root=NiftyPage, index=Const.NIFTY)
    NiftyPage.pack(fill="both", expand=1)

    BankNiftyPage = Frame(my_notebook, width=1071, height=483)
    bankniftypageobject = optionindex(root=BankNiftyPage, index=Const.BANK_NIFTY)
    BankNiftyPage.pack(fill="both", expand=1)

    Homepage = Frame(my_notebook, width=1071, height=483)
    Homepageobject = HomePage(root=Homepage)
    Homepage.pack(fill="both", expand=1)

    my_notebook.add(Homepage, text="HOME PAGE")
    my_notebook.add(NiftyPage, text=getname(index=Const.NIFTY))
    my_notebook.add(BankNiftyPage, text=getname(index=Const.BANK_NIFTY))
    my_notebook.pack()
    main.mainloop()
