import sys
import os
from io_txt_csv import read_text, write_csv
#пробую разные пути для импорта
try:
    from lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    try:
        sys.path.append('C:/Users/maria/Desktop/python_labs/src')
        from lib.text import normalize, tokenize, count_freq, top_n
    except ImportError:
        sys.exit(1)
try:
    text = read_text('data/lab04/input.txt')
except FileNotFoundError as e:
    print(f"Ошибка: {e}") 
    sys.exit(1)
tokens = tokenize(normalize(text))
word_counts = count_freq(tokens)
top_5 = top_n(word_counts, 5)
top_list = top_n(word_counts, len(word_counts.keys()))

write_csv(top_list, 'data/lab04/report.csv', ('word', 'count'))

print(f"Всего слов: {len(tokens)}") 
print(f"Уникальных слов: {len(set(tokens))}")

if top_5:
    max_len = max(len(word) for word, count in top_5)
    max_len = max(max_len, 5)
    
    first_line = 'слово' + ' ' * (max_len - 5) + '| частота'
    print(first_line)
    print('-' * len(first_line))
    for word, count in top_5:
        print(f'{word}' + ' ' * (max_len - len(word)) + f'| {count}')
else:
    print("Топ-5: нет данных")