import pandas as pd

pedigree = pd.read_csv('data/pedigree.csv', encoding='utf-8', sep=',')
bulls = pd.read_csv('data/bulls.csv', encoding='utf-8', sep=',')
cows = pd.read_csv('data/cows.csv', encoding='utf-8', sep=',')

row = bulls.iloc[0]
print(row['id'])