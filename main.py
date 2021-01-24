from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

browser = webdriver.Chrome(ChromeDriverManager().install())

user_input = input("Put the ISBN: ")

browser.get("https://google.com")

input = browser.find_element_by_class_name("gLFyf")
input.send_keys(f"isbn {user_input}")
input.send_keys(Keys.ENTER)

tag = browser.find_element_by_class_name("g")

tag.click()
