from DataFromSite import Getting_data_from_site as DataFromSite
from PostInExcel import Excel
from Excelpostingdata import Excelformat
from time import sleep, time
from datetime import datetime, date
import os
try:
    from selenium.common.exceptions import WebDriverException
except:
    os.system('python -m pip install selenium')
    from selenium.common.exceptions import WebDriverException




NiftyUrl = 'https://www1.nseindia.com/live_market/dynaContent/live_watch/option_chain/optionKeys.jsp?symbolCode=-10003&symbol=NIFTY&symbol=NIFTY&instrument=OPTIDX&date=-&segmentLink=17&segmentLink=17'
BankNiftyUrl = ""
base_table_xpath = '//*[@id="octable"]/tbody/tr'

excel_file_path = os.getcwd() + "\\nse_test.xlsx"

driver_path = os.getcwd() + "\\geckodriver.exe"

hide_browser = True

low = 8500
high = 10000
gap_between_data = 2
refresh_minutes = 5

data = DataFromSite(
    lowrange=low,
    highrange=high,
    Nifty_url=NiftyUrl,
    BankNifty_url=BankNiftyUrl,
    basexpath=base_table_xpath,
    driverpath=driver_path,
)

excel = Excel(
    filepath=excel_file_path,
)

formdata = Excelformat()

starting = True
dataprev = None
datanow = None
presenttime = None
presentdate = None

past_calls_change_in_oi = []
past_puts_change_in_oi = []

for j in range(2):
    try:
        if starting:
            starting = False
        else:
            print("Waiting for next update")
            #sleep(refresh_minutes * 60)
        starttime = time()
        presenttime = datetime.now().strftime("%H:%M:%S")
        datanow = data.readdata()
        endtime = time()
        presentdate = str(date.today())
    except WebDriverException as wbe:
        print("Web driver exception found:", wbe)
        continue

    print("data retrieve time", str(endtime - starttime))

    formdata.update(
        datanow=datanow,
        past_calls=past_calls_change_in_oi,
        past_puts=past_puts_change_in_oi
    )

    excel.postdata(
        presentdate=presentdate,
        presenttime=presenttime,
        data=formdata.postdata(),
        gap=gap_between_data
    )

    past_calls_change_in_oi.insert(0, [i.calls_change_in_oi for i in datanow])
    if len(past_calls_change_in_oi) > 3:
        past_calls_change_in_oi.pop()

    past_puts_change_in_oi.insert(0, [i.puts_change_in_oi for i in datanow])
    if len(past_puts_change_in_oi) > 3:
        past_puts_change_in_oi.pop()

    presentdate = None
    dataprev = datanow
