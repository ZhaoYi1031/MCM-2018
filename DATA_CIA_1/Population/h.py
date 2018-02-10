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
    pos2 = s.find("note")
    if (pos2 != -1 and pos2 < pos):
        pos = pos2
    num = s[0:pos].replace(",","")
    try:
        ans = int(num)
        return ans
    except:
        return "NA"
        
n = 2119
for i in range(2002,2017):
    title = "population"
    csvFile = open(title+"_"+str(i)+".csv", "w", encoding="utf-8")
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
    print(i,' siz: ',tot)
    fileHeader = ["Country", title+"( migrant(s)/1,000 population)"]
    writer.writerow(fileHeader)
    for i in range(0,tot):
        d = []
        #print(list_data[i].text)
        pos = len(list_data[i].text)#list_data[i].text.find("%")
        #print(pos)
        d.append(list_name[i].text)
        d.append(work(list_data[i].text[4:pos]))
        #print(d)
        writer.writerow(d)

    csvFile.close()
