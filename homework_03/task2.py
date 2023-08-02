# В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки препинания и регистр символов. 
# За основу возьмите любую статью из википедии или из документации к языку.(Может помочь метод translate из модуля string)

from string import digits, punctuation
from collections import Counter


with open('data.txt', 'r', encoding='utf-8') as file:
    str = file.read()

# Удаляем ненужные символы и изменяем регистр
symb_remove = digits + punctuation
for symb in symb_remove:
    str = str.replace(symb, '')

str = str.lower()

# Создаем словарь и считаем дубликаты
lst = str.split()
all_words = dict().fromkeys(lst, 0)
for el in lst:
    all_words[el] += 1
words = dict(sorted(all_words.items(), key=lambda item: item[1], reverse=True)[:10])
for key, value in words.items():
    print(f"{key}: {value} повторений")
    
    

# более легкий способ
#print(*Counter(lst).most_common(10))