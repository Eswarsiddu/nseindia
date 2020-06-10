from DataFromSite import DataRequest
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



