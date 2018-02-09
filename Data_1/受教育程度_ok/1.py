import csv

START = 2000
END = 2017

file = open("country_code.csv", "rt", encoding="utf-8")
reader0 = csv.reader(file)

conDict = {}
for item in reader0:
    conDict[item[2]] = item[0]



csvFile = open("RAW_education.csv", "rt", encoding="utf-8")
reader = csv.reader(csvFile)

csvFile2 = open("education.csv", "w", encoding="utf-8")
writer = csv.writer(csvFile2)

tot = 0
# 建立空字典
result = {}

lastLoc = ""
lastSub = ""
d=[]
dict={}
for item in reader:
    tot = tot+1
    # 忽略第一行
    if reader.line_num == 1:
        fileHeader = []
        fileHeader.append("Country")
        fileHeader.append("Country_code") #item[0])
        fileHeader.append("Type")
        for i in range(START, END):
            fileHeader.append(i)
        writer.writerow(fileHeader)
        continue
    loc = item[0]
    sub = item[1]
    #print(loc, ' ', sub, ' ', lastLoc, ' ', lastSub)
    if (loc == lastLoc and sub == lastSub):
        dict[int(item[2])] = item[3]
        #d.append(item[3])
    else:
        #print(d)
        #print(dict)
        #if (tot>10):
            #break
        for i in range(START,END):
            if (i in dict):
                d.append(dict[i])
            else:
                d.append(0)
        if (d[0] != 0):
            writer.writerow(d)
        d = []
        dict = {}
        if (sub == "TRY_MEN" or sub == "TRY_WOMEN"):
            continue
        if (loc in conDict):
            d.append(conDict[loc])
        else:
            print(loc)
            break
        d.append(loc)
        d.append(sub)
        #d.append(item[3])
        dict[int(item[2])] = item[3]
        
        print(loc)
    lastLoc = loc
    lastSub = sub


csvFile2.close()
csvFile.close()
print(fileHeader)
print(tot)
