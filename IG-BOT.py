from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.common.exceptions import ElementClickInterceptedException

options = Options()
options.add_argument("--window-size=1200,1000")
driver = webdriver.Chrome(options=options)
driver.get("https://www.instagram.com/")
action = ActionChains(driver)
USER_NAME= 'UR IG Account'
PASSWD = 'UR IG Pass'
ACC_NAME = 'Target Account'
PATH = r"C:\Users\PC\.cache\selenium\chromedriver\win64\126.0.6478.55\chromedriver.exe"
driver.get('https://www.instagram.com/')
time.sleep(5)
usermae = driver.find_element(By.NAME,'username').send_keys(USER_NAME)
passwd = driver.find_element(By.NAME,'password').send_keys(PASSWD,'\n')
print(usermae)
print(passwd)
time.sleep(5)
driver.get(f'https://www.instgram.com/{ACC_NAME}')
time.sleep(5)
follow = driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/div/div[2]/section/main/div/header/section[2]/div/div/div[2]/div/div[1]/button').click()
followers = driver.find_element(By.CSS_SELECTOR,'li a ._ac2a').click()
print(follow)
print(followers)
time.sleep(5)
number = 20
follow_btns = []

for i in range(1,number +1):
    btn =  driver.find_element(By.XPATH,f'/html/body/div[6]/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[2]/div/div[{i}]/div/div/div/div[3]/div/button') 
    follow_btns.append(btn)
for button in follow_btns:
    try:
        button.click()
        time.sleep(5)
    except ElementClickInterceptedException:
        print("Click has been intercepted by a model")
