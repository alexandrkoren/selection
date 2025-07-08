from helper import read_from_csv, relationship_ratio

# Чтение данных
pedigree = read_from_csv('data/pedigree.csv')
bulls = read_from_csv('data/bulls.csv')
cows = read_from_csv('data/cows.csv')

# print(relationship_ratio('FR00000003715', 'RU00000003716', pedigree))
