import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome(executable_path='usr/bin/chromedriver')

driver.get('https://your.url/here?yes=brilliant')

results = []
content = driver.page_source
soup = BeautifulSoup(content)
