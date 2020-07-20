import threading,ctypes
c=0
getname = lambda index: Const.NIFTY_NAME if index == Const.NIFTY else Const.BANK_NIFTY_NAME


def getsizeandpos(height, width):
    screenheight = main.winfo_screenheight()
    screenwidth = main.winfo_screenwidth()
    posy = int(screenheight / 2 - height / 2)
    posx = int(screenwidth / 2 - width / 2)
    return str(width) + "x" + str(height) + "+" + str(posx) + "+" + str(posy)

def on_closing():
    quit(0)
    exit(1)

class updatethread(threading.Thread):
    def __init__(self, updatefunc):
        threading.Thread.__init__(self)
        self.updatefunc = updatefunc
        self.started=None

    def run(self):
        self.started=True
        self.updatefunc()
        time.sleep(1)
        self.started=False

    def get_id(self):
        if hasattr(self,'_thread_id'):
            return self._thread_id
        for id,thread in threading._active.items():
            if thread is self:
                return id

    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)

class optionscontroller:
    def __init__(self, root, update, index, datareset):
        self.__stopmiddlepagefunc = None
        self.__startmiddlepagefunc = None
        self.__homepageerrorlabel = None
        self.__updatedata = update
        self.__datareset = datareset
        self.root = root
        self.stopped = None
        self.starting = True
        self.index = index
        self.__startfun = None
        self.__stopfun = None
        self.createupdatethread()
        controller = LabelFrame(self.root, text="Controller", padx=100)
        self.__setcontroller(root=controller)
        controller.pack(side=BOTTOM)

    def createupdatethread(self):
        self.updatethr = updatethread(updatefunc=self.__updatedata)

    def __setcontroller(self, root):
        self.Timer = Label(root, text="Press start", width=15)
        self.startbut = Button(root, text="START", state=NORMAL, command=self.startpressed)
        self.stopbut = Button(root, text="STOP", state=DISABLED, command=self.stoppressed)
        self.errorlabel = Label(root, text="")
        self.Timer.pack(sid=LEFT, padx=10)
        self.startbut.pack(side=LEFT, padx=10)
        self.stopbut.pack(side=LEFT, padx=10)
        self.errorlabel.pack(side=LEFT, padx=10)

    def stoppressed(self):
        self.__stopfun()
        self.__stopmiddlepagefunc(index=self.index)
        self.stopbut.config(state=DISABLED)
        self.startbut.config(state=NORMAL)
        self.updatethr.raise_exception()
        self.stopped = True
        self.__homepageerrorlabel.config(text="")
        my_notebook.tab(self.index + 1, text=getname(index=self.index))

    def startpressed(self):
        self.__startfun()
        self.__startmiddlepagefunc(index=self.index)
        self.startbut.config(state=DISABLED)
        self.stopbut.config(state=NORMAL)
        self.starting = True
        self.stopped = False
        self.__datareset()
        self.__start()

    def linkedtomiddlepage(self, startmiddlepagefunc, stopmiddlepagefunc):
        self.__startmiddlepagefunc = startmiddlepagefunc
        self.__stopmiddlepagefunc = stopmiddlepagefunc

    def linkedtohomepage(self, startfun, stopfunc, homepageerrorlabel):
        self.__startfun = startfun
        self.__stopfun = stopfunc
        self.__homepageerrorlabel = homepageerrorlabel

    def __start(self):
        self.Timer.config(text=time.strftime("%H : %M: %S"))
        if self.stopped == False:
            self.__updatedata()
            # try:
            #     if self.updatethr.started == None:
            #         self.updatethr.start()
            #     elif self.updatethr.started == False:
            #         del self.updatethr
            # except:
            #     self.createupdatethread()
            self.Timer.after(ms=1000, func=self.__start)


class optionindex:
    def __init__(self, root, index):
        self.__homepageerrorlabel = None
        self.__index = index
        self.__request = DataRequest(index=index)
        self.__Dataformatter = DataFormatter(index=index)
        self.__root = root
        self.__statfun = None
        self.__stopfun = None
        Table = LabelFrame(self.__root, text="OPTION CHAIN DATA", bg=None)
        Headinglabel = Label(Table, text="NOT YET STARTED")
        Headinglabel.grid(row=0, column=0, columnspan=3)
        self.__CALLS = LabelFrame(Table, text="CALLS")
        self.__Strikeprice = LabelFrame(Table, text="STRIKE PRICE")
        self.__PUTS = LabelFrame(Table, text="PUTS")
        self.__frames = {}
        self.__frames[Const.HEADING] = Headinglabel
        self.__frames[Const.BODY] = []

        self.__CALLSOI = LabelFrame(self.__CALLS, text=Const.OI)
        self.__CALLSLTP = LabelFrame(self.__CALLS, text=Const.LTP)
        self.__CALLSCOI = LabelFrame(self.__CALLS, text=Const.CHANGE_IN_OI)
        self.__CALLSTREND1 = LabelFrame(self.__CALLS, text=Const.getTrends(i=1))
        self.__CALLSTREND2 = LabelFrame(self.__CALLS, text=Const.getTrends(i=2))
        self.__CALLSTREND3 = LabelFrame(self.__CALLS, text=Const.getTrends(i=3))

        self.__PUTSOI = LabelFrame(self.__PUTS, text=Const.OI)
        self.__PUTSLTP = LabelFrame(self.__PUTS, text=Const.LTP)
        self.__PUTSCOI = LabelFrame(self.__PUTS, text=Const.CHANGE_IN_OI)
        self.__PUTSTREND1 = LabelFrame(self.__PUTS, text=Const.getTrends(i=1))
        self.__PUTSTREND2 = LabelFrame(self.__PUTS, text=Const.getTrends(i=2))
        self.__PUTSTREND3 = LabelFrame(self.__PUTS, text=Const.getTrends(i=3))

        self.__Strike = LabelFrame(self.__Strikeprice, text=Const.STRIKE_PRICE)
        self.__Strike.grid(row=0, column=0)

        self.Controller = optionscontroller(root=self.__root, update=self.__updatedata, index=index,
                                            datareset=self.__request.reset_data)
        self.Controller.stopped = False
        self.__frames[Const.ERROR] = self.Controller.errorlabel
        self.settablestructure()
        Table.pack()

    def linkedtohomepage(self, startfun, stopfunc, homepageerrorlabel):
        self.__homepageerrorlabel = homepageerrorlabel
        self.Controller.linkedtohomepage(startfun=startfun, stopfunc=stopfunc, homepageerrorlabel=homepageerrorlabel)

    def linkedtomiddlepage(self, startmiddlepagefunc, stopmiddlepagefunc):
        self.Controller.linkedtomiddlepage(startmiddlepagefunc=startmiddlepagefunc,
                                           stopmiddlepagefunc=stopmiddlepagefunc)

    def settablestructure(self):
        self.__setcolumnpositions()
        self.__loadrows()


    def __setcolumnpositions(self):
        self.__CALLS.grid(row=1, column=Const.CALLS_POS[self.__index] - 1)
        self.__Strikeprice.grid(row=1, column=Const.STRIKEPRICE_POS[self.__index] - 1)
        self.__PUTS.grid(row=1, column=Const.PUTS_POS[self.__index] - 1)

        self.__CALLSOI.grid(row=0, column=Const.CALLS_OI[self.__index] - 1)
        self.__CALLSLTP.grid(row=0, column=Const.CALLS_LTP[self.__index] - 1)
        self.__CALLSCOI.grid(row=0, column=Const.CALLS_CHANGE_IN_OI[self.__index] - 1)
        self.__CALLSTREND1.grid(row=0, column=Const.CALLS_TREND1[self.__index] - 1)
        self.__CALLSTREND2.grid(row=0, column=Const.CALLS_TREND2[self.__index] - 1)
        self.__CALLSTREND3.grid(row=0, column=Const.CALLS_TREND3[self.__index] - 1)

        self.__PUTSOI.grid(row=0, column=Const.PUTS_OI[self.__index] - 1)
        self.__PUTSLTP.grid(row=0, column=Const.PUTS_LTP[self.__index] - 1)
        self.__PUTSCOI.grid(row=0, column=Const.PUTS_CHANGE_IN_OI[self.__index] - 1)
        self.__PUTSTREND1.grid(row=0, column=Const.PUTS_TREND1[self.__index] - 1)
        self.__PUTSTREND2.grid(row=0, column=Const.PUTS_TREND2[self.__index] - 1)
        self.__PUTSTREND3.grid(row=0, column=Const.PUTS_TREND3[self.__index] - 1)

    def __loadrows(self):
        # TODO: changing the geometry
        # print("screenheight:", main.winfo_screenheight(), main.winfo_screenwidth())
        # main.geometry("1253x600+100+100")
        presentcount = len(self.__frames[Const.BODY])
        requestedcount = Const.UP_VALUE[self.__index] + Const.DOWN_VALUE[self.__index] + 1
        requiredrows = requestedcount - presentcount
        if requiredrows < 0:
            self.__removerows(rows=abs(requiredrows))
        elif requiredrows > 0:
            self.__addrows(rows=abs(requiredrows))

    def __addrows(self, rows):
        labelwidth = 10
        for _ in range(rows):
            t = {Const.STRIKE_PRICE: Label(self.__Strike, text="-", width=labelwidth, height=1),
                 Const.CALLS: {Const.OI: Label(self.__CALLSOI, text="-", width=labelwidth, height=1),
                               Const.LTP: Label(self.__CALLSLTP, text="-", width=labelwidth, height=1),
                               Const.CHANGE_IN_OI: Label(self.__CALLSCOI, text="-", width=labelwidth, height=1),
                               Const.TRENDS1: Label(self.__CALLSTREND1, text="-", width=labelwidth, height=1),
                               Const.TRENDS2: Label(self.__CALLSTREND2, text="-", width=labelwidth, height=1),
                               Const.TRENDS3: Label(self.__CALLSTREND3, text="-", width=labelwidth, height=1)},
                 Const.PUTS: {Const.OI: Label(self.__PUTSOI, text="-", width=labelwidth, height=1),
                              Const.LTP: Label(self.__PUTSLTP, text="-", width=labelwidth, height=1),
                              Const.CHANGE_IN_OI: Label(self.__PUTSCOI, text="-", width=labelwidth, height=1),
                              Const.TRENDS1: Label(self.__PUTSTREND1, text="-", width=labelwidth, height=1),
                              Const.TRENDS2: Label(self.__PUTSTREND2, text="-", width=labelwidth, height=1),
                              Const.TRENDS3: Label(self.__PUTSTREND3, text="-", width=labelwidth, height=1)}}
            for i in t:
                if i == Const.STRIKE_PRICE:
                    t[i].pack(side=TOP)
                else:
                    for j in t[i]:
                        t[i][j].pack(side=TOP)
            self.__frames[Const.BODY].append(t)

    def __removerows(self, rows):
        for _ in range(rows):
            t = self.__frames[Const.BODY][-1]
            for i in t:
                if i == Const.STRIKE_PRICE:
                    t[i].pack_forget()
                    t[i].destroy()
                else:
                    for j in t[i]:
                        t[i][j].pack_forget()
                        t[i][j].destroy()
            self.__frames[Const.BODY].pop(-1)

    def __setheading(self, Time, date, price, marketstatus):
        optionname = getname(index=self.__index)
        s = optionname + " " + str(price)
        my_notebook.tab(self.__index + 1, text=s)
        s = optionname + " : " + str(price) + " as of " + Time + " on " + date + (
            ", Market has been closed" if marketstatus == False else "")
        self.__frames[Const.HEADING].config(text=s)

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

    def __updatedata(self):
        data = self.__Dataformatter.update_data(self.__request.request_data)
        if data[Const.ERROR] != None:
            if data[Const.ERROR] == Const.NO_INTERNET:
                self.__frames[Const.ERROR].config(text="NO INTERNET, CHECK YOUR CONNECTION", width=50)
                # self.__homepageerrorlabel.config(text="NO INTERNET, CHECK YOUR CONNECTION")
            else:
                self.__frames[Const.ERROR].config(text="Site is Not Working", width=30)
                self.__homepageerrorlabel.config(text="Site is Not Working")
            return
        else:
            self.__homepageerrorlabel.config(text="")
            self.__frames[Const.ERROR].config(text="", width=0)

        self.__setheading(price=data[Const.PRICE],
                          Time=data[Const.TIME],
                          date=data[Const.DATE],
                          marketstatus=data[Const.MARKET_STATUS])
        strikeprices = data[Const.STRIKES_LIST]
        for i in range(len(strikeprices)):
            Data = data[strikeprices[i]]
            self.__setattribute(data=Data[Const.STRIKE_PRICE], label=self.__frames[Const.BODY][i][Const.STRIKE_PRICE])
            self.__setrowvalue(data=Data[Const.CALLS], frame=self.__frames[Const.BODY][i][Const.CALLS])
            self.__setrowvalue(data=Data[Const.PUTS], frame=self.__frames[Const.BODY][i][Const.PUTS])

        if not data[Const.MARKET_STATUS]:
            self.__homepageerrorlabel.config(text="market closed")
            self.Controller.stoppressed()


class Optionchaindataset:
    def __init__(self, index, root, packside, option):
        self.__option = option
        self.entrylist = []
        name = getname(index=index)
        frame = LabelFrame(master=root, text=name, width=535, height=483)
        self.__index = index
        self.__upperframe = Frame(master=frame)
        self.__lowerframe = Frame(master=frame)
        self.__setupupperframe(root=self.__upperframe)
        self.__setuplowerframe(root=self.__lowerframe)
        self.__setentrylist()
        self.__setvalues()
        option.linkedtohomepage(startfun=self.Disableall, stopfunc=self.Enableall, homepageerrorlabel=self.__errorLabel)
        self.__upperframe.pack(side=TOP)
        self.__lowerframe.pack(side=BOTTOM)
        frame.pack(side=packside, expand=1, fill="both")

    def linkedtomiddlepage(self, startmiddlepagefunc, stopmiddlepagefunc):
        self.__option.linkedtomiddlepage(stopmiddlepagefunc=stopmiddlepagefunc, startmiddlepagefunc=startmiddlepagefunc)

    def __setentrylist(self):
        self.entrylist.append(self.__callsentry)
        self.entrylist.append(self.__putsentry)
        self.entrylist.append(self.__strikepriceentry)
        self.entrylist.append(self.__callsoientry)
        self.entrylist.append(self.__callscoientry)
        self.entrylist.append(self.__callsltpentry)
        self.entrylist.append(self.__callstrend1entry)
        self.entrylist.append(self.__callstrend2entry)
        self.entrylist.append(self.__callstrend3entry)
        self.entrylist.append(self.__putsoientry)
        self.entrylist.append(self.__putscoientry)
        self.entrylist.append(self.__putsltpentry)
        self.entrylist.append(self.__putstrend1entry)
        self.entrylist.append(self.__putstrend2entry)
        self.entrylist.append(self.__putstrend3entry)
        self.entrylist.append(self.__upvaluesentry)
        self.entrylist.append(self.__downvaluesentry)

    def Disableupperframe(self):
        for child in self.__upperframe.winfo_children():
            if child != self.__errorLabel:
                child.configure(state=DISABLED)

    def Enableupperframe(self):
        for child in self.__upperframe.winfo_children():
            child.configure(state=NORMAL)

    def Disableall(self):
        self.Disableupperframe()
        self.resetbut.config(state=DISABLED)
        self.restorebut.config(state=DISABLED)
        self.savebut.config(state=DISABLED)
        self.loadbut.config(state=DISABLED)
        self.startbut.config(state=DISABLED)
        self.stopbut.config(state=NORMAL)

    def Enableall(self):
        self.Enableupperframe()
        self.resetbut.config(state=NORMAL)
        self.restorebut.config(state=NORMAL)
        self.savebut.config(state=NORMAL)
        self.loadbut.config(state=NORMAL)
        self.startbut.config(state=NORMAL)
        self.stopbut.config(state=DISABLED)

    def __setvalues(self):
        self.__callsentry.delete(0, END)
        self.__putsentry.delete(0, END)
        self.__strikepriceentry.delete(0, END)
        self.__callsoientry.delete(0, END)
        self.__callscoientry.delete(0, END)
        self.__callsltpentry.delete(0, END)
        self.__callstrend1entry.delete(0, END)
        self.__callstrend2entry.delete(0, END)
        self.__callstrend3entry.delete(0, END)
        self.__putsoientry.delete(0, END)
        self.__putscoientry.delete(0, END)
        self.__putsltpentry.delete(0, END)
        self.__putstrend1entry.delete(0, END)
        self.__putstrend2entry.delete(0, END)
        self.__putstrend3entry.delete(0, END)
        self.__upvaluesentry.delete(0, END)
        self.__downvaluesentry.delete(0, END)

        self.__callsentry.insert(0, Const.CALLS_POS[self.__index])
        self.__putsentry.insert(0, Const.PUTS_POS[self.__index])
        self.__strikepriceentry.insert(0, Const.STRIKEPRICE_POS[self.__index])
        self.__callsoientry.insert(0, Const.CALLS_OI[self.__index])
        self.__callscoientry.insert(0, Const.CALLS_CHANGE_IN_OI[self.__index])
        self.__callsltpentry.insert(0, Const.CALLS_LTP[self.__index])
        self.__callstrend1entry.insert(0, Const.CALLS_TREND1[self.__index])
        self.__callstrend2entry.insert(0, Const.CALLS_TREND2[self.__index])
        self.__callstrend3entry.insert(0, Const.CALLS_TREND3[self.__index])
        self.__putsoientry.insert(0, Const.PUTS_OI[self.__index])
        self.__putscoientry.insert(0, Const.PUTS_CHANGE_IN_OI[self.__index])
        self.__putsltpentry.insert(0, Const.PUTS_LTP[self.__index])
        self.__putstrend1entry.insert(0, Const.PUTS_TREND1[self.__index])
        self.__putstrend2entry.insert(0, Const.PUTS_TREND2[self.__index])
        self.__putstrend3entry.insert(0, Const.PUTS_TREND3[self.__index])
        self.__upvaluesentry.insert(0, Const.UP_VALUE[self.__index])
        self.__downvaluesentry.insert(0, Const.DOWN_VALUE[self.__index])

    def __setuplowerframe(self, root):
        lowerpady = 40
        lowerpadx = 1
        self.resetbut = Button(master=root, text="RESET", command=self.resetpressed)
        self.resetbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.savebut = Button(master=root, text="SAVE", command=self.savepressed)
        self.savebut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.restorebut = Button(master=root, text="RESTORE", command=self.restorepressed)
        self.restorebut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.loadbut = Button(master=root, text="LOAD", command=self.loadpressed)
        self.loadbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.startbut = Button(master=root, text="START", command=self.startpressed, state=NORMAL)
        self.startbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)
        self.stopbut = Button(master=root, text="STOP", command=self.stoppressed, state=DISABLED)
        self.stopbut.pack(side=LEFT, pady=lowerpady, padx=lowerpadx)

    def resetpressed(self):
        Const.resetvalues(index=self.__index, mode="reset")
        self.__setvalues()

    def savepressed(self):
        self.__errorLabel.config(text=self.__checkvalues(mode="saving"))

    def restorepressed(self):
        Const.resetvalues(index=self.__index, mode="restore")
        self.__setvalues()

    def loadpressed(self):
        t = self.__checkvalues(mode="loading")
        self.__errorLabel.config(text=t)
        if t == "":
            self.__option.settablestructure()

    def __checkvalues(self, mode):
        return Const.checkvalues(calls=self.__callsentry.get(),
                                 calls_oi=self.__callsoientry.get(),
                                 calls_ltp=self.__callsltpentry.get(),
                                 calls_changeinoi=self.__callscoientry.get(),
                                 calls_trend1=self.__callstrend1entry.get(),
                                 calls_trend2=self.__callstrend2entry.get(),
                                 calls_trend3=self.__callstrend3entry.get(),
                                 strikeprice=self.__strikepriceentry.get(),
                                 puts=self.__putsentry.get(),
                                 puts_oi=self.__putsoientry.get(),
                                 puts_ltp=self.__putsltpentry.get(),
                                 puts_changeinoi=self.__putscoientry.get(),
                                 puts_trend1=self.__putstrend1entry.get(),
                                 puts_trend2=self.__putstrend2entry.get(),
                                 puts_trend3=self.__putstrend3entry.get(),
                                 index=self.__index,
                                 up=self.__upvaluesentry.get(),
                                 down=self.__downvaluesentry.get(),
                                 mode=mode)

    def startpressed(self):
        self.__option.Controller.startpressed()

    def stoppressed(self):
        self.__option.Controller.stoppressed()

    def __setupupperframe(self, root):
        padyvalue = 7
        entrywidth = 10
        callslabel = Label(master=root, text="CALLS")
        self.__callsentry = Entry(master=root, width=entrywidth)
        strikepricelabel = Label(master=root, text="STRIKE PRICE")
        self.__strikepriceentry = Entry(master=root, width=entrywidth)
        putslabel = Label(master=root, text="PUTS")
        self.__putsentry = Entry(master=root, width=entrywidth)

        callsoilabel = Label(master=root, text=Const.OI)
        self.__callsoientry = Entry(master=root, width=entrywidth)
        callsltplabel = Label(master=root, text=Const.LTP)
        self.__callsltpentry = Entry(master=root, width=entrywidth)
        callscoilabel = Label(master=root, text=Const.CHANGE_IN_OI)
        self.__callscoientry = Entry(master=root, width=entrywidth)
        callstrend1label = Label(master=root, text=Const.TRENDS1)
        self.__callstrend1entry = Entry(master=root, width=entrywidth)
        callstrend2label = Label(master=root, text=Const.TRENDS2)
        self.__callstrend2entry = Entry(master=root, width=entrywidth)
        callstrend3label = Label(master=root, text=Const.TRENDS3)
        self.__callstrend3entry = Entry(master=root, width=entrywidth)

        putsoilabel = Label(master=root, text=Const.OI)
        self.__putsoientry = Entry(master=root, width=entrywidth)
        putsltplabel = Label(master=root, text=Const.LTP)
        self.__putsltpentry = Entry(master=root, width=entrywidth)
        putscoilabel = Label(master=root, text=Const.CHANGE_IN_OI)
        self.__putscoientry = Entry(master=root, width=entrywidth)
        putstrend1label = Label(master=root, text=Const.TRENDS1)
        self.__putstrend1entry = Entry(master=root, width=entrywidth)
        putstrend2label = Label(master=root, text=Const.TRENDS2)
        self.__putstrend2entry = Entry(master=root, width=entrywidth)
        putstrend3label = Label(master=root, text=Const.TRENDS2)
        self.__putstrend3entry = Entry(master=root, width=entrywidth)

        upvalueslabel = Label(master=root, text="UP VALUES")
        self.__upvaluesentry = Entry(master=root, width=entrywidth)
        downvalueslabel = Label(master=root, text="DOWN VALUES")
        self.__downvaluesentry = Entry(master=root, width=entrywidth)

        self.__errorLabel = Label(master=root, text="")

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

        self.__callsentry.grid(row=1, column=1, pady=padyvalue)
        self.__putsentry.grid(row=1, column=5, pady=padyvalue)
        self.__strikepriceentry.grid(row=1, column=3, pady=padyvalue)
        self.__callsoientry.grid(row=2, column=1, pady=padyvalue)
        self.__callscoientry.grid(row=4, column=1, pady=padyvalue)
        self.__callsltpentry.grid(row=3, column=1, pady=padyvalue)
        self.__callstrend1entry.grid(row=5, column=1, pady=padyvalue)
        self.__callstrend2entry.grid(row=6, column=1, pady=padyvalue)
        self.__callstrend3entry.grid(row=7, column=1, pady=padyvalue)
        self.__putsoientry.grid(row=2, column=5, pady=padyvalue)
        self.__putscoientry.grid(row=4, column=5, pady=padyvalue)
        self.__putsltpentry.grid(row=3, column=5, pady=padyvalue)
        self.__putstrend1entry.grid(row=5, column=5, pady=padyvalue)
        self.__putstrend2entry.grid(row=6, column=5, pady=padyvalue)
        self.__putstrend3entry.grid(row=7, column=5, pady=padyvalue)
        self.__upvaluesentry.grid(row=8, column=1, pady=padyvalue)
        self.__downvaluesentry.grid(row=8, column=4, pady=padyvalue)
        self.__errorLabel.grid(row=9, column=0, columnspan=6, pady=padyvalue)


class Homemiddlepage:
    def __init__(self, banknifty, nifty, root):
        self.__banknifty = banknifty
        self.__nifty = nifty
        self.__niftystarted = False
        self.__bankniftystarted = False
        padx = 10
        pady = 10
        frame = Frame(root)
        self.__sameasnifty = IntVar()
        self.__checkbut = Checkbutton(master=frame, text="Same as Nifty", variable=self.__sameasnifty,
                                      command=self.sameasniftypressed)
        self.__checkbut.pack(side=TOP, padx=padx, pady=pady)
        self.__resetbut = Button(master=frame, text="RESET BOTH", command=self.resetpressed)
        self.__resetbut.pack(side=TOP, padx=padx, pady=pady)
        self.__savebut = Button(master=frame, text="SAVE BOTH", command=self.savepressed)
        self.__savebut.pack(side=TOP, padx=padx, pady=pady)
        self.__restorebut = Button(master=frame, text="RESTORE BOTH", command=self.restorepressed)
        self.__restorebut.pack(side=TOP, padx=padx, pady=pady)
        self.__loadbut = Button(master=frame, text="LOAD BOTH", command=self.loadpressed)
        self.__loadbut.pack(side=TOP, padx=padx, pady=pady)
        self.__stopbut = Button(master=frame, text="STOP BOTH", command=self.stoppressed, state=DISABLED)
        self.__stopbut.pack(side=TOP, padx=padx, pady=pady)
        self.__startbut = Button(master=frame, text="START BOTH", command=self.startpressed)
        self.__startbut.pack(side=TOP, padx=padx, pady=pady)
        self.__nifty.linkedtomiddlepage(startmiddlepagefunc=self.startfunc, stopmiddlepagefunc=self.stopfunc)
        self.__banknifty.linkedtomiddlepage(startmiddlepagefunc=self.startfunc, stopmiddlepagefunc=self.stopfunc)
        Button(master=frame, text="QUIT", command=self.quitpressed).pack(side=TOP, padx=padx, pady=pady)
        frame.pack(side=LEFT, expand=1, fill="both")

    def quitpressed(self):
        main.quit()
        exit(0)

    def Disableall(self):
        self.__stopbut.config(state=NORMAL)
        self.__startbut.config(state=DISABLED)
        self.__resetbut.config(state=DISABLED)
        self.__restorebut.config(state=DISABLED)
        self.__loadbut.config(state=DISABLED)
        self.__savebut.config(state=DISABLED)

    def Enableall(self):
        self.__stopbut.config(state=DISABLED)
        self.__startbut.config(state=NORMAL)
        self.__resetbut.config(state=NORMAL)
        self.__restorebut.config(state=NORMAL)
        self.__loadbut.config(state=NORMAL)
        self.__savebut.config(state=NORMAL)

    def startfunc(self, index):
        # print(index, "prev nifty started in start func:", self.__niftystarted)
        if index == Const.NIFTY:
            # print("nifty started")
            self.__niftystarted = True
            self.__nifty.Disableall()
        if index == Const.BANK_NIFTY:
            # print("bank nifty started")
            self.__bankniftystarted = True
            self.__banknifty.Disableall()

        if self.__niftystarted and self.__bankniftystarted:
            self.Disableall()
        else:
            self.Enableall()
        # print(index,"nifty started in start func:", self.__niftystarted)
        # print(index,"bank nifty started in start func:", self.__bankniftystarted)
        # print("")

    def stopfunc(self, index):
        if index == Const.NIFTY:
            self.__niftystarted = False
            self.__nifty.Enableall()
        if index == Const.BANK_NIFTY:
            self.__bankniftystarted = False
            self.__banknifty.Enableall()

        if self.__niftystarted and self.__bankniftystarted:
            self.Disableall()
        else:
            self.Enableall()
        # print(index,"nifty started in stopfunc:", self.__niftystarted)
        # print(index,"bank nifty started in stopfunc:", self.__bankniftystarted)
        # print("")

    def restorepressed(self):
        self.__nifty.restorepressed()
        self.__banknifty.restorepressed()

    def startpressed(self):
        if not self.__niftystarted:
            # print("nifty start pressed")
            self.__nifty.startpressed()
            self.__niftystarted = True
        if not self.__bankniftystarted:
            # print("bank nifty start pressed")
            self.__banknifty.startpressed()
            self.__bankniftystarted = True

    def stoppressed(self):
        self.Enableall()
        if self.__niftystarted:
            self.__nifty.stoppressed()
            self.__niftystarted = False
        if self.__bankniftystarted:
            self.__banknifty.stoppressed()
            self.__bankniftystarted = False
        # print("nifty started in stop:", self.__niftystarted)
        # print("bank nifty started in stop:", self.__bankniftystarted)

    def loadpressed(self):
        self.__nifty.loadpressed()
        self.__banknifty.loadpressed()

    def resetpressed(self):
        self.__nifty.resetpressed()
        self.__banknifty.resetpressed()

    def savepressed(self):
        self.__nifty.savepressed()
        self.__banknifty.savepressed()

    def sameasniftypressed(self):
        if self.__sameasnifty.get() == 1:
            self.__loadvaluestoother()
            self.__banknifty.Disableupperframe()
        else:
            self.__banknifty.Enableupperframe()

    def __loadvaluestoother(self):
        for i in range(18):
            self.__banknifty.entrylist[i].delete(0, END)
            self.__banknifty.entrylist[i].insert(0, self.__nifty.entrylist[i].get())


class HomePage:
    def __init__(self, root, niftypage, bankniftypage):
        self.__root = root
        Homepage = Frame(root, width=1071, height=483)
        nifty = Optionchaindataset(root=Homepage, index=Const.NIFTY, packside=LEFT, option=niftypage)
        banknifty = Optionchaindataset(root=Homepage, index=Const.BANK_NIFTY, packside=RIGHT, option=bankniftypage)
        Homemiddlepage(root=Homepage, banknifty=banknifty, nifty=nifty)
        Homepage.pack(fill="both", expand=1)


if __name__ == "__main__":
    import time
    from tkinter import *
    from tkinter import font, ttk
    import os
    from dependencies.DataRequest import DataRequest
    from dependencies.DataFormatter import DataFormatter
    from dependencies.Constants import Constants as Const

    main = Tk(className="Option-Chain Data")
    try:
        main.iconbitmap(os.getcwd() + "dependencies/logo.ico")
    except:
        pass  # do nothing with logo
    main.geometry(getsizeandpos(width=Const.WINDOW_WIDTH, height=Const.WINDOW_HEIGHT))
    my_notebook = ttk.Notebook(main)

    NiftyPage = Frame(my_notebook, width=1, height=483)
    niftypageobject = optionindex(root=NiftyPage, index=Const.NIFTY)
    NiftyPage.pack(fill="both", expand=1)

    BankNiftyPage = Frame(my_notebook, width=1071, height=483)
    bankniftypageobject = optionindex(root=BankNiftyPage, index=Const.BANK_NIFTY)
    BankNiftyPage.pack(fill="both", expand=1)

    Homepage = Frame(my_notebook, width=1071, height=483)
    Homepageobject = HomePage(root=Homepage, niftypage=niftypageobject, bankniftypage=bankniftypageobject)
    Homepage.pack(fill="both", expand=1)

    my_notebook.add(Homepage, text="HOME PAGE")
    my_notebook.add(NiftyPage, text=getname(index=Const.NIFTY))
    my_notebook.add(BankNiftyPage, text=getname(index=Const.BANK_NIFTY))
    my_notebook.pack()
    main.protocol("WM_DELETE_WINDOW", on_closing)
    main.mainloop()
