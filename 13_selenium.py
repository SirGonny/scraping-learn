import time
from selenium import webdriver

browser = webdriver.Chrome()
#. 이동
browser.get("http://www.naver.com")

# 로그인 
elem = browser.find_element_by_class_name("link_login")
elem.click()

browser.find_element_by_id("id").send_keys("great_milk")
browser.find_element_by_id("pw").send_keys("facup")

browser.find_element_by_id("log.login").click()

time.sleep(3)

browser.find_element_by_id("id").clear()
browser.find_element_by_id("id").send_keys("adamant_")

print(browser.page_source)

browser.quit()