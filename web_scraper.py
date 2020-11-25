from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import subprocess

def main():
    file = open("stock.txt", 'w')
    file.truncate()

    driver = webdriver.Chrome(executable_path='C:/Webdrivers/chromedriver.exe')

    driver.get("https://auth.toasttab.com/login?state=g6Fo2SBtaTJqRHNma1hZaHVWa0pETENzSi05ZEx5TnZKNTlvMaN0aWTZIFBNZ2RxVFJ1cjRwekl1UVIzbC13MU5fUkMxa3QzNmJ5o2NpZNkgcFZJdGJCWldrcHd1OEg5RGRtMG9QY1NmYWd4cmtydEI&client=pVItbBZWkpwu8H9Ddm0oPcSfagxrkrtB&protocol=oauth2&force_mfa=false&redirect_uri=https%3A%2F%2Fwww.toasttab.com%2Fauthentication%2Fcallback&response_type=code&scope=openid%20profile&audience=https%3A%2F%2Ftoast-users-api%2F")
    driver.maximize_window()

    driver.implicitly_wait(5)
    email = driver.find_element_by_name('email')
    password = driver.find_element_by_name('password')
    email.send_keys("tktktk")
    password.send_keys("tktktk")
    submit = driver.find_element_by_class_name('auth0-lock-submit').click()

    driver.implicitly_wait(5)
    dropdown = driver.find_element_by_id('switch-toggle').click()
    correct_restaurant = driver.find_element_by_link_text('Two Boots Pizza - Nashville (Broadway)').click()

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

        file.write("SMALLS:")

        def small_whole_pies():
            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][2] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=0]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][2] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=0]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def small_whole_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232292405"]/td/div/div/button').click()
            driver.implicitly_wait(1)

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=1]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=1]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=1]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def small_left_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232292695"]/td/div/div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=2]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=2]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)
                
            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=2]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))
        
        def small_right_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232293195"]/td/div/div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=3]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=3]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=3]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

            
        small_whole_pies()
        small_whole_toppings()
        small_left_toppings()
        small_right_toppings()


    def mediums():
        wait = WebDriverWait(driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232297878"]/td/div/div/button')))
        button.click()

        file.write('\n' + 'MEDIUMS:')

        def medium_whole_pies():
            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][3] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=2]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][3] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=1]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def medium_whole_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232297895"]/td/div/div/button')
            button.click()
            driver.implicitly_wait(1)

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=4]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=4]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=4]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def medium_left_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232298501"]//td//div//div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=5]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=5]/td/div/a')
            titles = []
            for element in title_elements:
                titles.append(element.text)


            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=5]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def medium_right_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232298835"]//td//div//div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=6]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=6]/td/div/a')
            titles = []
            for element in title_elements:
                titles.append(element.text)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=6]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))
                    
            medium_whole_pies()
            medium_whole_toppings()
            medium_left_toppings()
            medium_right_toppings()
    
    def larges():
        wait = WebDriverWait(driver, 5)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232302668"]/td/div/div/button')))
        button.click()

        file.write('\n' + 'LARGES:')

        def large_whole_pies():
            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][4] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=2]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"][4] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=2]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def large_whole_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232302672"]/td/div/div/button')
            button.click()
            driver.implicitly_wait(1)

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=7]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=7]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOptionGroup"])=3]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def large_left_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232303347"]//td//div//div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=8]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=8]/td/div/a')
            titles = []
            for element in title_elements:
                titles.append(element.text)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=8]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def large_right_toppings():
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232303746"]//td//div//div/button')
            button.click()

            buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=9]/td/div/div/button')
            for button in buttons:
                button.click()

            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=9]/td/div/a')
            titles = []
            for element in title_elements:
                titles.append(element.text)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=9]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))
                    
        large_whole_pies()
        large_whole_toppings()          
        large_left_toppings()
        large_right_toppings()

    def half_specialties():
        wait = WebDriverWait(driver, 15)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232293581" and preceding-sibling::tr[@data-entity-id="100000005232293581"]][2]/td[@data-item-id="100000005232293581"]/div/div/button')))
        action = ActionChains(driver)
        action.move_to_element(button).click().perform() 

        file.write('\n' + 'HALF SPECIALTIES:')

        buttons = driver.find_elements_by_xpath('//table//tr[@class="MenuOption closed indent3 picker-parent" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=10]/td/div/div/button')
        for button in buttons:
            button.click()

        title_elements = []
        title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuOption indent3 picker-parent open" and preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=10]/td/div/a')
        titles = []
        for element in title_elements:
            title = element.text
            titles.append(title)

        stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuOption"] and count(preceding-sibling::tr[@class="divider MenuOption"])=10]//td[@class="inventory td-input right"]/input')
        stock_statuses = []
        for element in stock_elements:
            stock_status = element.get_attribute("value")
            stock_statuses.append(stock_status)

        for x in range(0, len(titles)):
            if stock_statuses[x] == "0":
                file.write('\n' + str(titles[x]))

    def salads():
        wait = WebDriverWait(driver, 20)
        button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232308750"]/td/div/div/button')))
        action = ActionChains(driver)
        action.move_to_element(button).click().perform() 

        file.write('\n' + 'SALADS:')

        def whole_salads():
            title_elements = []
            title_elements = driver.find_elements_by_xpath('//table//tr[@class="MenuItem closed indent2 picker-parent" and preceding-sibling::tr[@class="divider MenuGroup"] and count(preceding-sibling::tr[@class="divider MenuGroup"])=5]/td/div/a')
            titles = []
            for element in title_elements:
                title = element.text
                titles.append(title)

            stock_elements = driver.find_elements_by_xpath('//table//tr[preceding-sibling::tr[@class="divider MenuGroup"] and count(preceding-sibling::tr[@class="divider MenuGroup"])=5]//td[@class="inventory td-input right"]/input')
            stock_statuses = []
            for element in stock_elements:
                stock_status = element.get_attribute("value")
                stock_statuses.append(stock_status)

            print(titles)
            print(stock_statuses)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

        def dressings():
            wait = WebDriverWait(driver, 5)
            button = wait.until(EC.element_to_be_clickable((By.XPATH, '//table//tr[@data-entity-id="100000005232308771"]/td/div/div/button')))
            button.click()
            
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308784"]/td/div/div/button')
            button.click()
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308788"]/td/div/div/button')
            button.click()
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308792"]/td/div/div/button')
            button.click()
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308796"]/td/div/div/button')
            button.click()
            button = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308900"]/td/div/div/button')
            button.click()

            titles = []

            title = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308784"]/td/div/a')
            title = title.text
            titles.append(title)
            title = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308788"]/td/div/a')
            title = title.text
            titles.append(title)
            title = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308792"]/td/div/a')
            title = title.text
            titles.append(title)
            title = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308796"]/td/div/a')
            title = title.text
            titles.append(title)
            title = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308900"]/td/div/a')
            title = title.text
            titles.append(title)

            stock_statuses = []

            stock_status = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308781"]/td[@class="inventory td-input right"]/input')
            stock_status = stock_status.get_attribute("value")
            stock_statuses.append(stock_status)
            stock_status = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308786"]/td[@class="inventory td-input right"]/input')
            stock_status = stock_status.get_attribute("value")
            stock_statuses.append(stock_status)
            stock_status = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308790"]/td[@class="inventory td-input right"]/input')
            stock_status = stock_status.get_attribute("value")
            stock_statuses.append(stock_status)
            stock_status = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308794"]/td[@class="inventory td-input right"]/input')
            stock_status = stock_status.get_attribute("value")
            stock_statuses.append(stock_status)
            stock_status = driver.find_element_by_xpath('//table//tr[@data-entity-id="100000005232308798"]/td[@class="inventory td-input right"]/input')
            stock_status = stock_status.get_attribute("value")
            stock_statuses.append(stock_status)

            for x in range(0, len(titles)):
                if stock_statuses[x] == "0":
                    file.write('\n' + str(titles[x]))

            print(titles)
            print(stock_statuses)

        whole_salads()
        dressings()

    
    smalls()
    mediums()
    larges()
    half_specialties()
    salads()

    
main()
