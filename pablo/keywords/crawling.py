#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time

#%%
driver = webdriver.Chrome('C:/Users/segre/Desktop/project/pablo/chromedriver_win32/chromedriver.exe')
base_url = 'https://cafe.naver.com/ArticleList.nhn?search.clubid=27842958&search.menuid=148&search.boardtype=L'
driver.get(base_url)

driver.implicitly_wait(3)


main_area = driver.find_element(by=By.ID, value='main-area')
iframe = driver.find_element(by=By.ID, value='cafe_main')
driver.switch_to.frame(iframe)
time.sleep(2)

driver.find_element(by=By.XPATH, value='//*[@id="main-area"]/div[4]/table/tbody/tr[12]/td[1]/div[2]/div/a[1]').click()
headline = driver.find_element(by=By.CLASS_NAME, value='title_text').text

soup = bs(driver.page_source, 'html.parser')
soup_test = soup.select_one('#SE-4028d251-3689-47a0-9f74-a2f59d2a0fea').get_text()
print(headline)
print(soup_test)
# %%
driver.quit()
#%%