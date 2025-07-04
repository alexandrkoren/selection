import pandas as pd

# Чтение данных
pedigree = pd.read_csv('data/pedigree.csv', encoding='utf-8', sep=',')
bulls = pd.read_csv('data/bulls.csv', encoding='utf-8', sep=',')
cows = pd.read_csv('data/cows.csv', encoding='utf-8', sep=',')

# Формирование начальной популяции
bull_limit = cows.shape[0]*0.1
pairs = pd.DataFrame(columns=['cow_id', 'bull_id'])
for cow in cows.values:
    cow_id = cow[0]
    bull_id = bulls.sample().iloc[0]['id']
    new_pair = pd.DataFrame({'cow_id': [cow_id], 'bull_id': [bull_id]})
    pairs = pd.concat([pairs, new_pair], ignore_index=True)