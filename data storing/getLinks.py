#coding: utf8

import json

f = open("Links.txt", 'r')

categories = dict()
def add_caps(item):
	return item.capitalize()

def from_link_to_cat(link):
	link = link[link.rfind('/'): -1]
	if (':' in link):
		link = link[:-1]
	path = link[::]
	link = link[1:]
	link = link.split('-') if ('-' in link) else link.split('_')
	link = map(add_caps, link)
	cat = " ".join(link)
	result = {"name": cat, "link": path}
	return result

test1 = 0
test2 = 0
grand_parent_cat = ''
parent_cat = ''

for link in f:
	if link.startswith('\t\t'):
		result = from_link_to_cat(link)
		categories[grand_parent_cat][parent_cat].append(result)
	elif link.startswith('\t'):
		parent_cat = from_link_to_cat(link)["name"]
		categories[grand_parent_cat][parent_cat] = []
	else:
		grand_parent_cat = from_link_to_cat(link)["name"]
		categories[grand_parent_cat] = {}

with open('data.txt', 'w') as outfile:
    json.dump(categories, outfile)
    
f.close()