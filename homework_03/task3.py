# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения. 
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность. Достаточно вернуть один допустимый вариант. *Верните все возможные варианты комплектации рюкзака.



items = ['палатка', 'нож', 'кастрюля', 'ложка', 'аптечка', 'свисток', 'спрей', 'аннигиляторная пушка', 'громоотвод', 'еда']
mass = [60, 1, 5, 0.3, 4, 0.1, 0.5, 20, 50, 15]
dict = dict(zip(items, mass))
mass_limit = 91

# Отсоритруем рюкзак
sorted_dict = sorted(dict.items(), key = lambda item: item[1], reverse=True)

# Создадим список, куда будем помещать вещи, которые сможем взять
actual_mass = 0
items_to_go = tuple()
for key, value in sorted_dict:
    if actual_mass + value <= mass_limit:
        items_to_go = items_to_go +  (key,)
        actual_mass += value
        
print(*items_to_go)
print(f'Вес предметов {actual_mass:.1f}')

