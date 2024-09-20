from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pickle
import time
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://www.linkedin.com/login')
time.sleep(60)
cookies=driver.get_cookies()
with open("cookies_linkedin.pkl",'wb') as f:
    pickle.dump(obj=cookies,file=f)
driver.close()