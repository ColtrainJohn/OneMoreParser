from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def getDriver():
    opts = Options()
    opts.binary_location = '/home/selezov_su/anaconda3/bin/chrome'
    opts.add_argument('--no-sandbox')
    opts.add_argument("--headless")
    opts.add_argument('--disable-dev-shm-usage')
    opts.add_argument("--disable-gpu") 
    opts.add_argument("--disable-extensions") 
    opts.add_argument("--disable-setuid-sandbox")
    opts.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome(options=opts)
    return driver

