#coding utf_8

from companyProfileScraping import get_data
import json



small_data = open("companies.json")
small_data = json.load(small_data)
bigdata = list()

f1 = open("ct1.txt", "a+")
f2 = open("ct2.txt", "a+")
f3 = open("cerros.txt", "a+")

i = 8569

for data in small_data[8570:]:
	i += 1
	print(i)
	if "-" in data["path"]:
		f3.write(data["path"] + "\n")
		continue
	try:
		bdata = get_data(data["path"])
		bdata["top tools"] = data["top_tools"]
		bdata = json.dumps(bdata)
		bigdata.append(bdata)
		f1.write(bdata + ",\n")
	except Exception:
		f3.write(str(data["path"]) + "\n")

json.dump(bigdata, f2)
f1.close()
f2.close()
f3.close()