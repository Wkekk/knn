import pandas as pd
import numpy as np 
import os


i = 1
df = pd.read_csv('./DataSet/'+os.listdir('./DataSet/')[0])
for File in os.listdir('./Dataset/'):
	if File.endswith(".csv") and i < len(os.listdir('./DataSet/')):
		df2 = pd.read_csv('./DataSet/'+os.listdir('./DataSet/')[i])
		df=df.append(df2)
		i+=1

df.to_csv('./DataSet/DataSet__DataSet_complet__.csv', index=False) 

