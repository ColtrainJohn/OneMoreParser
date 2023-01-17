from time import sleep
from numpy import array
from pandas import DataFrame

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options


# this lib
import config as con
from args import parseArguments
from getDriver import getDriver


class Bot:
    def __init__(self):
        self.driver = getDriver()
        self.driver.get(con.url)
        sleep(3)
        # Year selector
        self.year = self.getSelector('year')
        # Month selector
        self.month = self.getSelector('month')
        # Region selector
        self.region = self.getSelector('region')
        # Main table
        self.table = self.getSelector('table')
        

        # Button to declick
        #self.declicker = self.getSelector('declicker')
        self.declicker = self.driver.find_element(By.XPATH, "//div[@id='ext-element-4']"
                    ).find_element(By.XPATH, '//span[@class="x-btn-wrap x-btn-wrap-default-small x-btn-arrow x-btn-arrow-right"]')

        sleep(1)
        print("Capture buttons : Done")


### Methods
    def getTable(self):
        # get row names
        index = self.getSelector('index').text.split('\n')
        # get column names
        #cols = [i.text for i in self.getSelector('columns') if i.text.find('20') > -1]
        #cols = [*cols[:2], 'отклонение', 'прирост', *cols[2:], 'отклонение', 'прирост']
        cols = ['this_year', 'last_year', 'отклонение', 'прирост', 'this_year', 'last_year', 'отклонение', 'прирост']

        # get table
        try:
            values = '-\n'.join([i.replace('\u202f', '') for i in self.table.text.split(' ') if i != ''])
            values = array(values.split('\n')).reshape(len(index), 8)
            tab = DataFrame(values, index=index, columns=cols)
            tab.to_excel(f'./out/{self.y}_{self.m}_{self.r}.xlsx')
            print(f'{self.y} {self.m} {self.r}')
        except Exception as ex:
            print(ex)


    def getSelector(self, name):
        if name == 'columns':
            return self.driver.find_elements(By.XPATH, con.bunchOfButtons[name])[2:]
        return self.driver.find_element(By.XPATH, con.bunchOfButtons[name])


    def getSelectorOptions(self, name, num='return_all'):
        selector = self.getSelector(name)
        selector.click() # open drop down list
        options = [i for i in selector.find_elements(By.XPATH, '//li[text()!=""]')]# if con.checkOption(i, name)]
        if num == 'return_all':
            self.declicker.click()
            return options
        else:
            print('Options lenght : ', len(options))
            text = options[num].text
            options[num].click() # close drop down list
            return text


    # multiprocces?
    def iterate(self, lastYears=False):
        num = len(self.getSelectorOptions('year'))
        for n in range(lastYears) if lastYears else range(num)[::-1]:
            self.y = self.getSelectorOptions('year', num=n)
            num1 = len(self.getSelectorOptions('month'))
            for m in range(num1)[::-1]:
                self.m = self.getSelectorOptions('month', num=m)
                num2 = len(self.getSelectorOptions('region'))
                for k in range(num2)[::-1]:
                    self.r = self.getSelectorOptions('region', num=k)
                    self.declicker.click()
                    self.getTable()



def main():
    bot = Bot()
    try:
        bot.iterate(lastYears=2)
    except Exception as ex:
        print(ex)
        bot.driver.quit()
    finally:
       bot.driver.quit()



if __name__ == '__main__':
    main()
