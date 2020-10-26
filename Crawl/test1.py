# test
import re
import time
import schedule
try:
    import urlparse
except ImportError:
    import urllib.parse as urlparse
from listweb import dict_data
from datetime import datetime

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
driver = webdriver.Chrome('chromedriver_linux64/chromedriver', chrome_options=options)
# actions = ActionChains(driver)
options.add_argument('--headless')

keys = [
    "vắc xin cho corona",
    "tình hình covid ở Hà Nội hôm nay"
    ]
print("===START========")
# txt_site = 'or'.join(list_web)
def get_links():
    arr_links_page = []
    try:
        first_link = driver.find_element_by_id('yuRUbf').get_attribute('href')
        arr_links_page.append(first_link)
    except:
        pass
    try:
        arr_links = driver.find_elements_by_xpath('//div[@id="rso"]//div[@class="r"]/a')
        arr_links_page = [elem.get_attribute('href') for elem in arr_links]
    except:
        pass
    return arr_links_page
def main():
    try:
        for url, value in dict_data.items():
            xpath_title, xpath_content, xpath_time, xpath_tag, xpath_outlink, xpath_search, xpath_next = value[0], value[1], value[2], value[3], value[4],value[5],value[6]
            driver.get(url)
            time.sleep(2)
            search = driver.find_element_by_xpath(xpath_search)
            search.send_keys("covid vietnam")
            search.send_keys(Keys.ENTER)
            time.sleep(5)
            
            try:
                print(xpath_next)
                next_page = driver.find_element_by_xpath(xpath_next)
                print(next_page)
                while next_page:
                    next_page.click()
                    time.sleep(5)
                    next_page = driver.find_element_by_xpath(xpath_next)
                    
            except:
                pass

            # while next_page:
                # next_page = driver.find_element_by_xpath(xpath_next)
                # next_page.click()            
    except:
        pass
# 
# schedule.every().hour.do(main)

# while True:
    # schedule.run_pending()
    # time.sleep(1)

if __name__ == "__main__":
    main()
    driver.close()
    driver.quit()
    print(time.time())