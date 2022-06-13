#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#%%
driver = webdriver.Chrome('C:/Users/segre/Desktop/project/pablo/chromedriver_win32/chromedriver.exe')
base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=27842958&search.menuid=148&search.boardtype=L'
driver.get(base_url)

main_area = driver.find_element(by=By.ID, value='main-area')
iframe = driver.find_element(by=By.ID, value='cafe_main')
driver.switch_to.frame(iframe)
sub_area = driver.find_element(by=By.XPATH, value='//*[@id="main-area"]/div[4]')
post = driver.find_element(by=By.XPATH, value='//*[@id="main-area"]/div[4]/table/tbody/tr[15]/td[1]/div[2]/div/a[1]').click()
# %%
driver.quit()
#%%