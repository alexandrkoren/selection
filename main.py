import time
import pandas as pd
from collections import defaultdict
from helper import read_from_csv, relationship_ratio

# Чтение данных
pedigree = read_from_csv('data/pedigree.csv')
bulls = read_from_csv('data/bulls.csv')
cows = read_from_csv('data/cows.csv')

# Генерируем всевозможные пары, подходящие под критерии
start_gen = time.time()
pairs = []
for cow_id, cow_ebv in cows.items():
    cow_ebv = float(cow_ebv[0]) if cow_ebv[0] else 0        # Если нет ebv, то принимаю ebv = 0
    for bull_id, bull_ebv in bulls.items():
        bull_ebv = float(bull_ebv[1]) if bull_ebv[1] else 0
        if relationship_ratio(cow_id, bull_id, pedigree) <= 0.05:   # Условие родства
            ebv_avg = (cow_ebv + bull_ebv)/2
            pairs.append((cow_id, bull_id, ebv_avg))
print('Generation time: ', time.time() - start_gen)

# Сортировка пар по ключу ebv_avg
start_sort = time.time()
pairs.sort(key=lambda elem: (-elem[2]))
print('Sorting_time ', time.time() - start_sort)

# Выборка коров
start_assignment = time.time()
assignments = []
bull_cnt_max = int(0.1*len(cows))       # Макимальное количество коров на одного быка
bull_cnt = defaultdict(int)             # Текущее количество коров на определенного быка
for cow_id, bull_id, _ in pairs:
    if cow_id not in {cow for cow, _ in assignments}:   # Если корова еще не выбрана
        if bull_cnt[bull_id] < bull_cnt_max:            # Условие количества коров на одного быка
            assignments.append((cow_id, bull_id))
            bull_cnt[bull_id] += 1
print('Assignment_time: ', time.time() - start_assignment)

# Запись в файл
result_df = pd.DataFrame(assignments, columns=['cow_id', 'bull_id'])
result_df.to_csv('data/cow_bull_assignments.csv', index=False)
