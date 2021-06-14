#coding: utf_8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json


PATH = "D:\Program Files\chromedriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get("https://stackshare.io/companies")
time.sleep(5)
data = []
f = open("companies_data1.txt", "w+")
f2 = open("companies_data1.csv", "w+")

def get_names(element):
	return element.get_attribute("title")

def get_small_data(element):
	tool_path = element.find_element_by_class_name("css-nl6q8a")
	tool_path = tool_path.find_element_by_tag_name("a").get_attribute("href")
	top_tools = []
	try:
		top_tools = element.find_element_by_class_name("css-18mxefy")
		top_tools = list(map(get_names , top_tools.find_elements_by_tag_name("a")))
	except Exception as e:
		print(e)
		top_tools = []
	return {"path": tool_path, "top_tools": top_tools}

i = 1

while True:
	try:
		print(i)
		button = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".css-1usn6s5")))
		button.click()
		i += 1
		
	except Exception as e:
		print(e)
		break
	

tool_divs = driver.find_elements_by_class_name("css-sy5l9v")
for div in tool_divs:
	f.write(str(get_small_data(div)) + '\n')

time.sleep(1)
# driver.quit()

f2.close()
f.close()