from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
import requests
import pickle

def main():
    file = open("cookies.txt", 'w')
    file.truncate()
    file.close()

    driver = webdriver.Chrome(executable_path='C:/Webdrivers/chromedriver.exe')

    session = requests.Session()

    driver.get("http://www.toasttab.com/login")
    driver.maximize_window()

    email = driver.find_element_by_name('username')
    password = driver.find_element_by_name('password')
    email.send_keys("TKTKTK")
    password.send_keys("TKTKTK")
    submit = driver.find_element_by_name('action').click()

    driver.implicitly_wait(2)
    
    cookies = driver.get_cookies()
    c = [session.cookies.set(c['name'], c['value']) for c in cookies]
    driver.close()
    driver.quit()
    with open('cookies.txt', 'wb') as f:
        pickle.dump(session.cookies, f)
    f.close()

main()
