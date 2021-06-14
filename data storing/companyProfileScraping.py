#coding: utf_8

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
from selenium.webdriver.chrome.options import Options



PATH = "D:\Program Files\chromedriver\chromedriver.exe"
# options = Options()
# options.add_argument("--headless")

url = "https://stackshare.io"
tools = {}

def get_tools(element):
	global tools
	c_name = element.find_element_by_class_name("css-dq491d").text
	c_tools = element.find_elements_by_class_name("css-12fxiad")
	c_tools = [tool.text for tool in c_tools]
	tools[c_name] = c_tools


def get_data(path):
	driver = webdriver.Chrome(PATH) #, options=options)

	driver.get(url+path*2)
	time.sleep(1)
	try:
		logo = driver.find_element_by_class_name("css-1m5j888").get_attribute("src")
	except Exception:
		driver.quit()
		raise Exception
	name = driver.find_element_by_class_name("css-1cylxxa").text
	desc = driver.find_element_by_class_name("css-1x2bey4").text
	tools_div = driver.find_elements_by_class_name("css-180cglb")
	for element in tools_div:
		get_tools(element)
	driver.quit()
	return {
		"name": name,
		"logo": logo,
		"desc": desc,
		"tools": tools
	}

if __name__ == '__main__':
	print(get_data("/pinterest"))