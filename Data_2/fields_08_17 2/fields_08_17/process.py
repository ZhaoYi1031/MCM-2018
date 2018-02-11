import os
import pandas as pd
files = os.listdir(".")
s = set()
for file in files:
	if file.endswith(".csv"):
		temp = list(pd.read_csv(file).iloc[:,0])
		for item in temp:
			s.add(item)
"""
with open("languages.txt","w") as f:
	for item in s:
		f.write(item)
		f.write("\n")
"""	
for file in files:
	if file.endswith(".csv"):


