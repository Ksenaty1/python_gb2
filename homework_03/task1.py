# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. В результирующем списке не должно быть дубликатов. [1, 2, 3, 1, 2, 4, 5] -> [1, 2]

lst = [1, 2, 3, 1, 2, 4, 5]
all_el = set(lst)

for el in all_el:
    lst.remove(el)

print(lst)

# 