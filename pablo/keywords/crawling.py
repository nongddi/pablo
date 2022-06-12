#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

#%%
driver = webdriver.Chrome('C:/Users/segre/Desktop/project/pablo/chromedriver_win32/chromedriver.exe')
base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=29890867&search.menuid=1&search.boardtype=L&search.totalCount=151&search.cafeId=29890867&search.page=1'
driver.get(base_url)

post_list = driver.find_elements(by=By.TAG_NAME, value='tbody')
print(post_list)

for post in post_list:
    href = post.get_attribute('href')
    print(href)
# %%