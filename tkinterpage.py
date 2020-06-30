import time
from tkinter import *
from tkinter import font
from Constants import Constants as Const
import os
from DataRequest import DataRequest
from ExcelData import DataFormatter

url = "https://www.google.com"
iconpath = os.getcwd() + "\\logo.ico"

niftyrequest = DataRequest(index=Const.NIFTY)
niftyformatter = DataFormatter(up=Const.UP, down=Const.DOWN,index=Const.NIFTY)

up = Const.UP
down = Const.DOWN
timer = 0
timeframe = 5
Const.REFRESH_TIME = timeframe
Const.TESTING = False
starting = True
stopped = False
x = 10
root = Tk(className="Option-Chain Data")
root.iconbitmap(iconpath)
root.geometry("1071x483")

frames = {}

Table = LabelFrame(root, text="OPTION CHAIN DATA", bg=None)
Table.pack()
Headingvar = StringVar()
Headingvar.set("PLEASE WAIT FOR FEW SECONDS, RELOADING AWM 😁😁")
Headinglabel = Label(Table, text=Headingvar.get(), padx=100, pady=5)
CALLS = LabelFrame(Table, text="CALLS")
Strikeprice = LabelFrame(Table, text="STRIKE PRICE")
PUTS = LabelFrame(Table, text="PUTS")
Headinglabel.grid(row=0, column=0, columnspan=3)
CALLS.grid(row=1, column=0)
Strikeprice.grid(row=1, column=1)
PUTS.grid(row=1, column=2)
frames["heading"] = Headinglabel
frames["body"] = []

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
    frames["body"].append(t)


def setheading(time, date, price, marketstatus):
    optionname = Const.NIFTY_NAME
    s = optionname + " : " + str(price) + " as of " + time + " on " + date + (
        ", Market has been closed" if marketstatus == False else "")
    frames["heading"].config(text=s)


def setattribute(data, label):
    label.config(
        text=data[Const.TEXT],
        bg=data[Const.CELL_FILL_COLOR],
        fg=data[Const.FONT_COLOR],
        font=font.Font(weight=data[Const.FONT_STYLE],size=data[Const.FONT_SIZE]))


def setrowvalue(data, frame):
    setattribute(data=data[Const.OI], label=frame[Const.OI])
    setattribute(data=data[Const.LTP], label=frame[Const.LTP])
    setattribute(data=data[Const.CHANGE_IN_OI], label=frame[Const.CHANGE_IN_OI])
    setattribute(data=data[Const.TRENDS1], label=frame[Const.TRENDS1])
    setattribute(data=data[Const.TRENDS2], label=frame[Const.TRENDS2])
    setattribute(data=data[Const.TRENDS3], label=frame[Const.TRENDS3])


def updatedata():
    global stopped
    data = niftyformatter.update_data(niftyrequest.request_data)
    if data[Const.ERROR] != None:
        print("No network")
        return
    if data[Const.MARKET_STATUS] == False:
        stopped = True
    setheading(price=data[Const.PRICE],
               time=data[Const.TIME],
               date=data[Const.DATE],
               marketstatus=data[Const.MARKET_STATUS])
    strikeprices = data[Const.STRIKES_LIST]
    for i in range(len(strikeprices)):
        Data = data[strikeprices[i]]
        setattribute(data=Data[Const.STRIKE_PRICE], label=frames["body"][i][Const.STRIKE_PRICE])
        setrowvalue(data=Data[Const.CALLS], frame=frames["body"][i][Const.CALLS])
        setrowvalue(data=Data[Const.PUTS], frame=frames["body"][i][Const.PUTS])


def start():
    global timer, starting, stopped
    hr = time.strftime("%H")
    min = time.strftime("%M")
    sec = time.strftime("%S")
    Timer.config(text=hr + " : " + min + " : " + sec)
    if stopped == False:
        timer += 1
        if starting == True and timer == 5:
            updatedata()
            starting = False
        if (timer >= timeframe * 60):
            updatedata()
            timer = 0
        Timer.after(ms=1000, func=start)


# Extras
options = LabelFrame(root, text="Extras", padx=100)
options.pack(side=BOTTOM)
Timer = Label(options, text="Strarting", width=15)
Timer.pack(side=LEFT)
start()
root.mainloop()
