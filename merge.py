import pandas as pd
data1 = pd.read_csv('list.csv')
data2 = pd.read_csv('result.csv')
result = pd.merge(data1,data2, on='Index', how='outer')
result.to_csv("list.csv")