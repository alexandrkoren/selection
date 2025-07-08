import csv

# Чтение данных из csv-файла
def read_from_csv(filename):
    result = {}
    with open(filename, mode='r', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)                    # Пропускаем заголовки
        for row in reader:
            key = row[0]                # Ключ в словаре - id животного
            values = tuple(row[1:])     # Остальные столбцы как tuple
            result[key] = values
    return result

# Собираем всех родственников
def get_relatives(pedigree, id):
    relatives = {id: 0}

    def find_relatives(current_id, level):
        mother_id, father_id = pedigree.get(current_id, (None, None))
        if mother_id:
            if mother_id not in relatives:
                relatives[mother_id] = level
            elif level < relatives[mother_id]:
                relatives[mother_id] = level
            find_relatives(mother_id, level + 1)
        if father_id:
            if father_id not in relatives:
                relatives[father_id] = level
            elif level < relatives[father_id]:
                relatives[father_id] = level
            find_relatives(father_id, level + 1)
    
    find_relatives(id, 1)
    return relatives

# Уровень родства
def relationship_ratio(cow_id, bull_id, pedigree):
    cow_relatives = get_relatives(pedigree, cow_id)
    bull_relatives = get_relatives(pedigree, bull_id)
    common_relatives = list(cow_relatives.keys() & bull_relatives.keys())
    ratio = 0
    for relative in common_relatives:
        p_cow = 0.5**cow_relatives[relative]
        p_bull = 0.5**bull_relatives[relative]
        ratio += p_cow*p_bull
    return ratio