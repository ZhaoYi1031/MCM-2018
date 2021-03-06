import csv

#def work(typ, s):
#    if (typ == "Q"):
#        return s[0:4]
#    return s

START = 1970
END = 2017

file = open("../country_code.csv", "rt", encoding="utf-8")
reader0 = csv.reader(file)

conDict = {}
for item in reader0:
    conDict[item[2]] = item[0]

csvFile = open("RAW_trade.csv", "rt", encoding="utf-8")
reader = csv.reader(csvFile)

csvFile2 = open("trade.csv", "w", encoding="utf-8")
writer = csv.writer(csvFile2)

tot = 0

lastSub = ""
lastLoc = ""
lastMea = ""
d=[]
dict={}
for item in reader:
    tot = tot+1
    # 忽略第一行
    if reader.line_num == 1:
        fileHeader = []
        fileHeader.append("Country")
        fileHeader.append("Country_code") #item[0])
        fileHeader.append("Subject")
        fileHeader.append("Measure")
        for i in range(START, END):
            fileHeader.append(i)
        writer.writerow(fileHeader)
        continue
    if (item[3] == "AGRWTH" or item[0] in ["EA", "EU", "OAVG", "EA19", "EU28", "OECDE", "OECD", "G-7"]):
        continue
    loc = item[0]
    sub = item[2]
    mea = item[3]
    #print(loc, ' ', sub, ' ', lastLoc, ' ', lastSub)
    if (loc == lastLoc and sub == lastSub and mea == lastMea):
        dict[int(item[5])] = item[6]
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
        
        if (loc in conDict):
            d.append(conDict[loc])
        else:
            print(loc)
            break
        d.append(loc)
        d.append(sub)
        d.append(mea)
        dict[int(item[5])] = item[6]
    lastLoc = loc
    lastSub = sub
    lastMea = mea


csvFile2.close()
csvFile.close()
print(fileHeader)
print(tot)
