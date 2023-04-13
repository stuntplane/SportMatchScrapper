import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
from bs4 import BeautifulSoup

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.aiscore.com')
h1 = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div[2]/div[1]/div[2]/div[2]/ul/li[4]').click()
h2 = driver.find_elements_by_xpath('//*[@id="app"]/div[4]/div[2]/div[1]/div[2]/div[3]/div/div[1]/div[8]/div/div[2]/a[1]')
h2inner = h2.__getattribute__('innerHTML')
#sourceCode = h2.__getattribute__('outerHTML')
file=open('D:/Bet Predictor/output.txt', 'w')

javaScript = "window.scrollBy(0,2000);"
time.sleep(2)
javaScript = "window.scrollBy(0,2000);"
time.sleep(2)

driver.execute_script(javaScript)
html = driver.getPageSource()
with open('D:/Bet Predictor//aiscore/matches.txt', 'w') as f:
    #f.write(sourceCode.encode('utf-8'))
    f.write(h2inner.encode('utf-8'))

    #soup = BeautifulSoup(html, 'lxml')
    #match = soup.find_all('href=')
#mecze = soup.find_all('href="/match', class_='match-container')

