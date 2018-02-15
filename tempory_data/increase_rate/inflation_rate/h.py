import urllib.request
import http.cookiejar
from bs4 import BeautifulSoup
from urllib.parse import urlparse
import re
import os
import csv
import decimal

def work(s):
    pos = 0
    pos = s.find("(", pos)
    pos2 = len(s)-1
    for j in range(65,91):
        i = chr(j)
        k = s.find(i)
        if (k != -1 and k < pos2):
            pos2 = k
    for j in range(97,123):
        i = chr(j)
        k = s.find(i)
        if (k != -1 and k < pos2):
            pos2 = k
    #pos2 = s.find("note")
    if (pos2 != -1 and pos2 < pos):
        pos = pos2
    num = s[0:pos].strip()
    try:
        if (not "." in num):
            ans = int(num[0:len(num)-1])
        else:
            ans = float(num[0:len(num)-1])
        return str(ans)+"%"
    except:
        return "NA"
       
n = 2092
dict_all = {}
set_con = set()
if (not os.path.exists("details")):
    os.mkdir("details")

for i in range(2002,2017):
    dict_year = {}
    title = "inflation_rate"
    csvFile = open("details/"+title+"_"+str(i)+".csv", "w", encoding="utf-8")
    writer = csv.writer(csvFile)

    if (i < 2002):
        fileRoute = "/Users/Mr.ZY/Desktop/FIELDS/work/fields_"+str(i)+"/" + title + ".html"
    else:
        fileRoute = "/Users/Mr.ZY/Desktop/FIELDS/work/fields_"+str(i)+"/" + str(n) + ".html"
    if (not os.path.exists(fileRoute)):
        continue
    f = open(fileRoute, "rt", encoding="utf-8")
    result = f.read()
    #print(result)
    soup = BeautifulSoup(result, "lxml")
    #print(i,':   ',soup.title.text[43:])
    #print(soup.prettify())

    list_name = soup.find_all(href=re.compile('../geos'))##find_all("table")
    list_data = soup.select('td[class="category_data"]')##find_all("table")
    if (len(list_data) == 0):
        list_data = soup.select('td[class="Normal"]')
    
    tot = len(list_data)
    if (len(list_data) != len(list_name)):
        print(i,"Year: ",len(list_data), " ", len(list_name))
        list_name = list_name[len(list_name)-tot:len(list_name)]
        print(list_name[0].text)
    #print(len(list_data), " ", len(list_name))
    #print(i,' siz: ',tot)
    fileHeader = ["Country", title+"( migrant(s)/1,000 population)"]
    writer.writerow(fileHeader)
    for j in range(0,tot):
        d = []
        #print(list_data[i].text)
        pos = len(list_data[j].text)#list_data[i].text.find("%")
        #print(pos)
        set_con.add(list_name[j].text)
        d.append(list_name[j].text)
        value = work(list_data[j].text[4:pos])
        d.append(value)
        dict_year[list_name[j].text] = value
        #print(d)
        writer.writerow(d)
    #print(dict_year)
    
    dict_all[i] = dict_year
    #print(dict_year)
    #print(len(set_con))
    #print(set_con)
    csvFile.close()
#print(dict_all)
csvFile = open(title+".csv", "w", encoding="utf-8")
writer = csv.writer(csvFile)
fileHeader = [i for i in range(2002,2017)]
fileHeader.insert(0, "Country")
writer.writerow(fileHeader)
for i in set_con:
    #print(i)
    d=[i]
    for j in range(2002,2017):
        #print(dict_all[j])
        if (i in dict_all[j]):
            d.append(dict_all[j][i])
        else:
            d.append("NA")
    writer.writerow(d)
csvFile.close()

