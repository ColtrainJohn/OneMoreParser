from time import sleep
from numpy import array
from pandas import DataFrame

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# this lib
import config as con

class Bot:
    def __init__(self, win=False):
        if win:
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox(options=Options())
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
        self.declicker = self.getSelector('declicker')
        sleep(1)
        print("Capture buttons : Done")


### Methods
    def getTable(self):
        # get row names
        index = self.getSelector('index').text.split('\n')

        # get column names
        cols = [i.text for i in self.getSelector('columns') if i.text.find('20') > -1]
        cols = [*cols[:2], 'отклонение', 'прирост', *cols[2:], 'отклонение', 'прирост']

        # get table
        try:
            values = '-\n'.join([i.replace('\u202f', '') for i in self.table.text.split(' ') if i != ''])
            values = array(values.split('\n')).reshape(len(index), 8)
            tab = DataFrame(values, index=index, columns=cols)
            tab.to_excel(f'{self.y}_{self.m}_{self.r}.xlsx')
            print('\n')
            print(f'{self.y} {self.m} {self.r}')
            print('\n')
        except Exception as ex:
            print(ex)


    def getSelector(self, name):
        if name == 'columns':
            return self.driver.find_elements(By.XPATH, con.bunchOfButtons[name])[2:]
        return self.driver.find_element(By.XPATH, con.bunchOfButtons[name])


    def getSelectorOptions(self, name, num='return_all'):
        selector = self.getSelector(name)
        selector.click() # open drop down list
        options = [i for i in selector.find_elements(By.XPATH, '//li[text()!=""]') if con.checkOption(i, name)]
        if num == 'return_all':
            self.declicker.click()
            return options
        else:
            print('Options lenght : ', len(options))
            text = options[num].text
            options[num].click() # close drop down list
            return text

    # multiprocces?
    def iterate(self):
        num = len(self.getSelectorOptions('year'))
        for n in range(num)[::-1]:
            self.y = self.getSelectorOptions('year', num=n)
            num1 = len(self.getSelectorOptions('month'))
            for m in range(num1)[::-1]:
                self.m = self.getSelectorOptions('month', num=m)
                num2 = len(self.getSelectorOptions('region'))
                for k in range(num2)[::-1]:
                    self.r = self.getSelectorOptions('region', num=k)
                    sleep(1)
                    self.getTable()


if __name__ == '__main__':
    bot = Bot(win=True)
    try:
        bot.iterate()
    except Exception as ex:
        print(ex)
        bot.driver.quit()
    finally:
       bot.driver.quit()
