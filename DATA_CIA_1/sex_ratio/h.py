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
    m = len(s)
    ans = []
    while pos < m:
        pos = s.find(":", pos)
        if (pos == -1):
            return ans
        
        #print(pos)
        nextpos = s.find("male", pos+1)
        #print(s[pos+1:nextpos])
        ans.append(s[pos+1:nextpos])
        pos = pos+1
        
n = 2018
for i in range(2002,2017):
    title = "sex_ratio"
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
    fileHeader = ["Country", title, "at birth", "0-14", "15-64", "65 years and ove", "total population"]
    writer.writerow(fileHeader)
    for i in range(0,tot):
        d = []
        #print(list_data[i].text)
        pos = len(list_data[i].text)#list_data[i].text.find("%")
        #print(pos)
        list_age = work(list_data[i].text)
        #print(list_age)
        d.append(list_name[i].text)
        d.append(list_data[i].text[4:pos+1])
        #print(d)
        #if (i==0):
            #print(len(list_age), '    ', list_age)
        if (len(list_age) == 7):
            list_age.insert(2, str(
                                round((float(list_age[2])+float(list_age[3])+float(list_age[4])), 2)
                                ))
            list_age.pop(3)
            list_age.pop(3)
            list_age.pop(3)
            #if (i==0):
                #print(len(list_age), '    ', list_age)
        for j in list_age:
            d.append(j)
        writer.writerow(d)

    csvFile.close()
