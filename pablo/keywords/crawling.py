#%%
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#%%
data_dict = {'Title': [], 'Main Text': [], 'User': []}

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
main_text = driver.find_elements(by=By.TAG_NAME, value='p')
user = driver.find_element(by=By.CLASS_NAME, value='user').text

data_dict['Title'].append(headline)
data_dict['User'].append(user)
for i in range(0, len(main_text)):
    if main_text[i].text != '':
        data_dict['Main Text'].append(main_text[i].text)

print(data_dict)
# %%
driver.quit()
#%%