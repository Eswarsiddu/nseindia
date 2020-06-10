import os
import time

import requests

def convert(n):
    return time.strftime("%H:%M:%S", time.gmtime(n))

#from market pulse app
host = "157.230.192.232"
# url = f'http://{host}:4000/api/scrips/feed?channel_names=nse_fno_nifty_11062020_9050_ce%20nse_fno_nifty_11062020_9050_pe%20nse_fno_nifty_11062020_9100_ce%20nse_fno_nifty_11062020_9100_pe%20nse_fno_nifty_11062020_9150_ce%20nse_fno_nifty_11062020_9150_pe%20nse_fno_nifty_11062020_9200_ce%20nse_fno_nifty_11062020_9200_pe%20nse_fno_nifty_11062020_9250_ce%20nse_fno_nifty_11062020_9250_pe%20nse_fno_nifty_11062020_9300_ce%20nse_fno_nifty_11062020_9300_pe%20nse_fno_nifty_11062020_9350_ce%20nse_fno_nifty_11062020_9350_pe%20nse_fno_nifty_11062020_9400_ce%20nse_fno_nifty_11062020_9400_pe%20nse_fno_nifty_11062020_9450_ce%20nse_fno_nifty_11062020_9450_pe%20nse_fno_nifty_11062020_9500_ce%20nse_fno_nifty_11062020_9500_pe%20nse_fno_nifty_11062020_9550_ce%20nse_fno_nifty_11062020_9550_pe%20nse_fno_nifty_11062020_9600_ce%20nse_fno_nifty_11062020_9600_pe%20nse_fno_nifty_11062020_9650_ce%20nse_fno_nifty_11062020_9650_pe%20nse_fno_nifty_11062020_9700_ce%20nse_fno_nifty_11062020_9700_pe%20nse_fno_nifty_11062020_9750_ce%20nse_fno_nifty_11062020_9750_pe%20nse_fno_nifty_11062020_9800_ce%20nse_fno_nifty_11062020_9800_pe%20nse_fno_nifty_11062020_9850_ce%20nse_fno_nifty_11062020_9850_pe%20nse_fno_nifty_11062020_9900_ce%20nse_fno_nifty_11062020_9900_pe%20nse_fno_nifty_11062020_9950_ce%20nse_fno_nifty_11062020_9950_pe%20nse_fno_nifty_11062020_10000_ce%20nse_fno_nifty_11062020_10000_pe%20nse_fno_nifty_11062020_10050_ce%20nse_fno_nifty_11062020_10050_pe%20nse_fno_nifty_11062020_10100_ce%20nse_fno_nifty_11062020_10100_pe%20nse_fno_nifty_11062020_10150_ce%20nse_fno_nifty_11062020_10150_pe%20nse_fno_nifty_11062020_10200_ce%20nse_fno_nifty_11062020_10200_pe%20nse_fno_nifty_11062020_10250_ce%20nse_fno_nifty_11062020_10250_pe%20nse_fno_nifty_11062020_10300_ce%20nse_fno_nifty_11062020_10300_pe%20nse_fno_nifty_11062020_10350_ce%20nse_fno_nifty_11062020_10350_pe%20nse_fno_nifty_11062020_10400_ce%20nse_fno_nifty_11062020_10400_pe%20nse_fno_nifty_11062020_10450_ce%20nse_fno_nifty_11062020_10450_pe%20nse_fno_nifty_11062020_10500_ce%20nse_fno_nifty_11062020_10500_pe%20nse_fno_nifty_11062020_10550_ce%20nse_fno_nifty_11062020_10550_pe%20nse_fno_nifty_11062020_10600_ce%20nse_fno_nifty_11062020_10600_pe%20nse_fno_nifty_11062020_10650_ce%20nse_fno_nifty_11062020_10650_pe%20nse_fno_nifty_11062020_10700_ce%20nse_fno_nifty_11062020_10700_pe%20nse_fno_nifty_11062020_10750_ce%20nse_fno_nifty_11062020_10750_pe%20nse_fno_nifty_11062020_10800_ce%20nse_fno_nifty_11062020_10800_pe%20nse_fno_nifty_11062020_10850_ce%20nse_fno_nifty_11062020_10850_pe%20nse_fno_nifty_11062020_10900_ce%20nse_fno_nifty_11062020_10900_pe%20nse_fno_nifty_11062020_10950_ce%20nse_fno_nifty_11062020_10950_pe%20nse_fno_nifty_11062020_11000_ce%20nse_fno_nifty_11062020_11000_pe%20nse_fno_nifty_11062020_11050_ce%20nse_fno_nifty_11062020_11050_pe%20nse_fno_nifty_11062020_8500_ce%20nse_fno_nifty_11062020_8500_pe'
niftyprice = f'http://{host}:4000/api/scrips/feed?channel_names=nse_cm_nifty_50'
#
#
# # ur = url.split("%")
# # for i in ur:
# #     print(i)
# def getdata(data):
#     c = 0
#     ini = 0
#     ltp = 0
#     oi = 0
#     changeinoi = 0
#     for i in range(len(data)):
#         t = False
#         if (data[i] == '|'):
#             c += 1
#             t = True
#         if t:
#             if (c == 1):
#                 ltp = data[:i]
#             elif c == 11:
#                 ini = i + 1
#             elif c == 12:
#                 oi = data[ini:i]
#             elif c == 18:
#                 ini = i + 1
#             elif c == 19:
#                 changeinoi = data[ini:i]
#                 break
#     return (int(oi),int(changeinoi),float(ltp))
r = requests.get(url=niftyprice)
price = r.json()['nse_cm_nifty_50']
for i in range(len(price)):
    if(price[i]=='|'):
        price = float(price[:i])
        break
print(price)
r = requests.get('https://www.timeanddate.com/scripts/ts.php?ut=1591767154328&cb=0.4198837067162553')
p = float(r.text.split(" ")[0])+19800
print(convert(p))
# r = requests.get(url = url)
# data = r.json()
# calls = {}
# puts = {}
# for i in data:
#     t = i[23:]
#     if(t[::-1][:2]=="ec"):
#         calls[t[::-1][3:][::-1]]=data[i]
#     else:
#         puts[t[::-1][3:][::-1]] = data[i]
#
# print("puts of9950:",getdata(puts['8500']))
# print("calls of9950:",getdata(calls['8500']))

url = 'https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY'
niftyprice = 'https://www.nseindia.com/api/marketStatus'
headers = {
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, br',
    'Accept-Language':'en-US,en;q=0.5',
    'Connection':'keep-alive',
    'Host':'www.nseindia.com',
    'If-None-Match':'W/"1047db-ffsRpZgBL7KYhzea10O6o9p87Bk"',
    'TE':'Trailers',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
}
# r = requests.get(url=url,headers=headers)
# data = r.json()
# for i in data['filtered']['data']:
#     strikeprice = i['strikePrice']
#     print(strikeprice)
# r=requests.get(url=niftyprice,headers=headers)
# data = r.json()
# for i in data['marketState']:
#     if i['index'] == 'NIFTY 50':
#         print(i)
#selenium
# from selenium import webdriver
# options = webdriver.FirefoxOptions()
# #options.add_argument("--headless")
# browser = webdriver.Firefox(executable_path=(os.getcwd() + "\\geckodriver.exe"),options=options)
# for i in range(3):
#     browser.get(url="https://www.nseindia.com/option-chain")
#     print("opened")
#     time.sleep(20)
#     print("reloading")
# print("quitting")
# browser.quit()