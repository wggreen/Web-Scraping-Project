from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import subprocess
import smtplib, ssl
from logins import *

driver = webdriver.Chrome(executable_path='C:/Webdrivers/chromedriver.exe')

driver.get("http://www.toasttab.com/login")
driver.maximize_window()

driver.implicitly_wait(5)
email = driver.find_element_by_name('username')
password_element = driver.find_element_by_name('password')
email.send_keys(username)
password_element.send_keys(password)
submit = driver.find_element_by_name('action').click()

driver.implicitly_wait(5)

menu = driver.find_element_by_link_text('Edit menus').click()

advanced_properties = driver.find_element_by_link_text('Advanced Properties').click()

dropdown = driver.find_element_by_css_selector('.pull-right button').click()
dropdown = driver.find_element_by_css_selector('li:nth-of-type(13) a.opt').click()
dropdown = driver.find_element_by_css_selector('li:nth-of-type(14) a.opt').click()
dropdown = driver.find_element_by_css_selector('li:nth-of-type(11) a.opt').click()

list_of_buttons = driver.find_elements_by_css_selector('#bulk-edit-table tbody tr td div div button')
button = list_of_buttons[0].click()

def smalls():
    
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "tr.MenuGroup:nth-child(4) > td:nth-child(1) > div:nth-child(1) > div:nth-child(1) > button:nth-child(1)")))
    button.click()


    def small_whole_toppings():

        small_whole_ids_doc = open("small_whole_ids.txt", 'w')
        small_whole_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232292405"]/td/div/div/button').click()
        driver.implicitly_wait(1)

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=1]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            small_whole_ids_doc.write("\n" + data_entity_id)

        small_whole_ids_doc.close()

        small_whole_ids_doc = open("small_whole_ids.txt", 'r')
        small_whole_ids_doc.close()

    small_whole_toppings()


    def small_left_toppings():

        small_left_ids_doc = open("small_left_ids.txt", 'w')
        small_left_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232292695"]/td/div/div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=2]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            small_left_ids_doc.write("\n" + data_entity_id)

        small_left_ids_doc.close()

    small_left_toppings()


    def small_right_toppings():
        
        small_right_ids_doc = open("small_right_ids.txt", 'w')
        small_right_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232293195"]/td/div/div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=3]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            small_right_ids_doc.write("\n" + data_entity_id)

        small_right_ids_doc.close()

    small_right_toppings()

smalls()

def mediums():
    
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232297878"]/td/div/div/button')))
    button.click()
    

    def medium_whole_toppings():

        medium_whole_ids_doc = open("medium_whole_ids.txt", 'w')
        medium_whole_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232297895"]/td/div/div/button')
        button.click()
        driver.implicitly_wait(1)

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=4]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            medium_whole_ids_doc.write("\n" + data_entity_id)

        medium_whole_ids_doc.close()

    medium_whole_toppings()

    def medium_left_toppings():

        medium_left_ids_doc = open("medium_left_ids.txt", 'w')
        medium_left_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232298501"]//td//div//div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=5]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            medium_left_ids_doc.write("\n" + data_entity_id)

        medium_left_ids_doc.close()

    medium_left_toppings()

    
    def medium_right_toppings():

        medium_right_ids_doc = open("medium_right_ids.txt", 'w')
        medium_right_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232298835"]//td//div//div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=6]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            medium_right_ids_doc.write("\n" + data_entity_id)

        medium_right_ids_doc.close()

    medium_right_toppings()
    
mediums()


def larges():
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232302668"]/td/div/div/button')))
    button.click()

    def large_whole_toppings():

        large_whole_ids_doc = open("large_whole_ids.txt", 'w')
        large_whole_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232302672"]/td/div/div/button')
        button.click()
        driver.implicitly_wait(1)

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=7]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            large_whole_ids_doc.write("\n" + data_entity_id)

        large_whole_ids_doc.close()

    large_whole_toppings()

    def large_left_toppings():
        
        large_left_ids_doc = open("large_left_ids.txt", 'w')
        large_left_ids_doc.truncate()
        
        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232303347"]//td//div//div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=8]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            large_left_ids_doc.write("\n" + data_entity_id)

        large_left_ids_doc.close()

    large_left_toppings()

    
    def large_right_toppings():

        large_right_ids_doc = open("large_right_ids.txt", 'w')
        large_right_ids_doc.truncate()

        button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232303746"]//td//div//div/button')
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=9]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            large_right_ids_doc.write("\n" + data_entity_id)

        large_right_ids_doc.close()

    large_right_toppings()

larges()


def half_specialties():
    
    def left_half_specialties():

        left_half_ids_doc = open("left_half_ids.txt", 'w')
        left_half_ids_doc.truncate()       
        
        wait = WebDriverWait(driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000007232953180"][3]//td//div//div/button')))
        action = ActionChains(driver)
        action.move_to_element(button).click().perform() 

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=10]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            left_half_ids_doc.write("\n" + data_entity_id)

        left_half_ids_doc.close()

    left_half_specialties()

                
    def right_half_specialties():

        right_half_ids_doc = open("right_half_ids.txt", 'w')
        right_half_ids_doc.truncate()

        wait = WebDriverWait(driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000007233285110"][3]//td//div//div/button')))
        action = ActionChains(driver)
        action.move_to_element(button).click().perform() 

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=11]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            right_half_ids_doc.write("\n" + data_entity_id)

        right_half_ids_doc.close()
                
    right_half_specialties()

half_specialties()


def calzones():
    wait = WebDriverWait(driver, 20)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232307736"]/td/div/div/button')))
    action = ActionChains(driver)
    action.move_to_element(button).click().perform()

    def calzone_whole_toppings():
        
        calzone_toppings_ids_doc = open("calzone_toppings_ids.txt", 'w')
        calzone_toppings_ids_doc.truncate()

        wait = WebDriverWait(driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232307740"]//td//div//div/button')))
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=12]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            calzone_toppings_ids_doc.write("\n" + data_entity_id)

        calzone_toppings_ids_doc.close()
                
    calzone_whole_toppings()

calzones()


def salads():
    
    wait = WebDriverWait(driver, 5)
    button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232308750"]/td/div/div/button')))
    action = ActionChains(driver)
    action.move_to_element(button).click().perform() 

    def dressings():
        
        dressings_ids_doc = open("dressings_ids.txt", 'w')
        dressings_ids_doc.truncate()

        wait = WebDriverWait(driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232308771"]/td/div/div/button')))
        button.click()

        parent_id_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=12]')
        parent_ids = []
        for element in parent_id_elements:
            data_entity_id = element.get_attribute("data-entity-id")
            dressings_ids_doc.write("\n" + data_entity_id)

        dressings_ids_doc.close()

    dressings()

salads()

driver.close()
driver.quit()
