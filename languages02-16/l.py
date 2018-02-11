import os
import pandas as pd
files = os.listdir(".")
for file in files:
	if file.endswith(".csv"):
		with open(file) as f:
			data = f.read()
			
		