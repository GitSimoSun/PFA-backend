#coding: utf_8


from bs4 import BeautifulSoup
import requests


def get_name(element):
	return element.a.span.text

def get_logo(element):
	return element.img.attrs["src"]

def get_stackup_count(element):
	result = element.text
	if 'K' in result:
		return int(eval(result[:-1]) * 1000)
	return int(result)

data = []
url = "https://stackshare.io"

def set_data(path, id):
	print(url+path)
	result = requests.get(url + path)
	src = result.content
	soup = BeautifulSoup(src, "lxml")
	soup_names = soup.find_all("div", class_="landing-stack-name")
	names = list(map(get_name , soup_names))
	soup_logos = soup.find_all("a", class_="hint--top")
	logos = list(map(get_logo, soup_logos))
	soup_stack_nums = soup.find_all("div", class_="stackup-count")
	stack_nums = list(map(get_stackup_count, soup_stack_nums))
	ids = [id for i in range(len(names))]
	global data
	data += zip(names, ids, stack_nums, logos)
	next_ = soup.find("span", class_="next")
	if next_:
		return get_data(next_.a.attrs['href'], id)

def get_data(path, id):
	set_data(path, id)
	return data
if __name__ == '__main__':
	get_data("/javascript-framework-components", 1)
	print(data)
	print(len(data))