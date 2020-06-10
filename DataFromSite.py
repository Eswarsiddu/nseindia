import os
from time import time

from Data import data

try:
    from selenium import webdriver
except:
    print("selenium not installed")
    os.system("python -m pip install selenium")
    from selenium import webdriver

class Getting_data_from_site:
    def __init__(self, lowrange, highrange, Nifty_url, BankNifty_url, basexpath,driverpath):
        self.Nifty_url = Nifty_url
        self.BankNifty_url = BankNifty_url
        self.lowrange = lowrange
        self.highrange = highrange
        self.starting = True
        self.basexpath = basexpath
        self.driverpath = driverpath
        self.options = webdriver.FirefoxOptions()
        self.options.add_argument("--headless")
        # self.options.set_headless(True)

    def readdata(self):
        data_now = []
        browser = None
        try:
            browser = webdriver.Firefox(
                executable_path=self.driverpath,
                firefox_options=self.options
            )

            print("link opening", end="")
            browser.get(self.Nifty_url)
            print(", opened", end="")
            niftyprice = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/table[1]/tbody/tr/td[2]/div/span[1]/b')

            date_time = browser.find_element_by_xpath('/html/body/div[2]/div[3]/div[2]/table[1]/tbody/tr/td[2]/div/span[2]')
            print("nifty[rice:",niftyprice)
            print("datetimne:",date_time)
            rows = browser.find_elements_by_xpath(self.basexpath)
            for i in range(1, len(rows)):
                row = browser.find_elements_by_xpath(self.basexpath + '[' + str(i) + ']/td')
                strikeprice = float(row[11].text)
                if self.lowrange <= strikeprice <= self.highrange:
                    data_now.append(data())
                    data_now[-1].getdata(row)
        except Exception as e:
            print("error:"+str(e))
        finally:
            try:
                browser.close()
            except:
                print("browser already closed")
            browser.quit()
            print("quiting browser")
        print("and closed")
        return data_now

