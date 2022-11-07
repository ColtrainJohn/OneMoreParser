from time import sleep
import numpy as np
import pandas as pd

# selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

# this lib
import config as con

class Bot:
    def __init__(self):
        self.driver = webdriver.Firefox(options=Options())
        self.driver.get(con.url)
        sleep(3)
        # Year selector
        self.year = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-7']"
                )
        # Month selector
        self.month = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-8']"
                )
        # Region selector
        self.region = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-5']"
                )
        # Main table
        self.table = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-15']"
                )
        # Index names
        self.row_names_container = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-14']"
                )
        # Column names
        self.col_names_container = self.driver.find_elements(
                    By.XPATH, "//div[@data-ref='titleEl']"
                )[2:]
        # Button to declick
        self.fixer = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-6']"
                ).find_element(
                        By.XPATH, "//a[@role='button']"
                    )
        sleep(1)


### Working functions
    def getTable(self):
        # get index
        index = self.row_names_container.text.split('\n')

        # get column names
        col_names = self.driver.find_elements(By.XPATH, "//div[@data-ref='titleEl']")[2:]
        cols = [i.text for i in col_names if i.text.find('20') > -1]
        cols = [*cols[:2], 'отклонение', 'прирост', *cols[2:], 'отклонение', 'прирост']

        # get table data
        try:
            values = '-\n'.join([i.replace('\u202f', '') for i in self.table.text.split(' ') if i != ''])
            values = np.array(values.split('\n')).reshape(len(index), 8)
            tab = pd.DataFrame(values, index=index, columns=cols)
            print(f'{self.y} {self.m} {self.r} table size: ', tab.shape)
            tab.to_excel(f'{self.y}_{self.m}_{self.r}.xlsx')
        except Exception as ex:
            print(ex)
    

    # ! Uncertain function !
    def getSelector(self, name):
        if name == 'region':
            out = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-5']"
                )
        elif name == 'year':
            out = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-7']"
                )
        elif name == 'month':
            out = self.driver.find_element(
                    By.XPATH, "//div[@id='ext-element-8']"
                )
        return out


    def iterateThroughtSelector(self, name):
        num1 = self.getSelectorOptions(name)
        for n in range(len(num1))[::-1]:
            self.r = self.chooseOptionByNum(self.getSelector(name), n, 'region')
            self.fixer.click()
            self.getTable()
            print('\n\n')


    def iterate(self):
        num = len(self.getSelectorOptions('year'))
        for n in range(num)[::-1]:
            self.y = self.chooseOptionByNum(self.getSelector('year'), n, 'year')
            self.fixer.click()
            num1 = len(self.getSelectorOptions('month'))
            for m in range(num1)[::-1]:
                self.m = self.chooseOptionByNum(self.getSelector('month'), m, 'month')
                self.fixer.click()
                num2 = len(self.getSelectorOptions('region'))
                for k in range(num2)[::-1]:
                    print("Current options number: ", f'Year: {num} Month: {num1} Region: {num2}')
                    self.r = self.chooseOptionByNum(self.getSelector('region'), k, 'region')
                    self.fixer.click()
                    self.getTable()
                    print('\n')


    def getSelectorOptions(self, name):
        selector = self.getSelector(name)
        selector.click() # open drop down list
        options = [i for i in selector.find_elements(By.XPATH, '//li[@role="option"]') if con.checkOption(i, name)]
        self.fixer.click() # close drop down list
        return options


    def chooseOptionByNum(self, selector, num, name):
        selector.click() # open drop down list
        options = [i for i in selector.find_elements(By.XPATH, '//li[@role="option"]') if con.checkOption(i, name)]
        print('Options lenght : ', len(options))
        text = options[num].text
        if not options[num].is_selected():
                print(text)
                options[num].click() #
        else:
            print(text, ' : ERROR')
        return text



if __name__ == '__main__':
    bot = Bot()
    try:
        bot.iterate()
    except Exception as ex:
        print(ex)
        bot.driver.quit()
    finally:
        bot.driver.quit()
