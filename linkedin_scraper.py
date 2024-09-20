from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.linkedin.com/in/jayesh-mhaske-9aa7b921b/")
with open("cookies_linkedin.pkl",'rb') as f:
    cookies=pickle.load(file=f)
    for i,cookie in enumerate(cookies):
        driver.add_cookie(cookie)

driver.refresh()
time.sleep(5)
driver.close()

#TODO
#  The whole project is pending




