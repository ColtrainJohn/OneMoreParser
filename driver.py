from pathlib import Path
from time import sleep
from numpy import array
from pandas import DataFrame

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select

# this lib
import config as con
from args import parseArguments
from getDriver import getDriver


class Bot:
    # init
    def __init__(self):

        self.driver = getDriver(con.driverOptions)
        self.driver.implicitly_wait(5)
        self.driver.get(con.url)

        self.selectorHandlers = dict(
            (one, self.getSelector(one)) for one in con.selectorHandlers.keys()
        )
        
        print(f'Capture {len(self.selectorHandlers)} buttons : Done')


    ### Methods
    def getSelector(self, name):
        return self.driver.find_element(By.XPATH, con.selectorHandlers[name])

    def declick(self):
        self.selectorHandlers['declicker'].click()


    def getTable(self):

        # get row names
        index = self.selectorHandlers["tableIndex"].text.split('\n')

        # get table
        try:
            values = '-\n'.join([i.replace('\u202f', '') for i in self.selectorHandlers["table"].text.split(' ') if i != ''])
            values = array(values.split('\n')).reshape(len(index), 8)
            tab = DataFrame(values[:, [0, 4]], index=index, columns=['Adults', 'Children'])
            #tab.to_excel(f'./out/{self.y}_{self.m}_{self.r}.xlsx')
            #print(f'{self.y} {self.m} {self.r}')
            print(tab)
            
        except Exception as ex:
            print(ex)


    def getSelectorOptions(self, name, num='return_all'):
        print(1)
        selector = Select(self.selectorHandlers[name].find_element(By))
        #selector.click() # open drop down list
        #options = [i for i in selector.find_elements(By.XPATH, '//li[text()!=""]')]
        #print(self.driver.execute_script(f'arguments[0].click();return arguments[0].getElementsByTagName("li");', selector))
        #print(self.driver.execute_script(f'arguments[0].click();return arguments[0].options', selector))
        #print(dir(selector))
        print(selector.options)
        if num == 'return_all':
            self.declick() # close drop down list
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
                    self.declick()
                    print(f'{self.y} {self.m} {self.r}')
                    #self.getTable()


def main():

    bot = Bot()
    try:
        #bot.getTable()
        bot.iterate()

    except Exception as ex:
        print(ex)

    finally:
        bot.driver.close()
        bot.driver.quit()


if __name__ == '__main__':
    main()
