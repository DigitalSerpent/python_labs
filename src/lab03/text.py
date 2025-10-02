import re
from collections import Counter

def normalize(text: str, *, casefold: bool = True, yooo: bool = True) -> str:
    """
    нормализирую текст(чищу)
    """
    if casefold:
        text = text.casefold()
    if yooo:
        text = text.replace('ё', 'е').replace('Ё', 'Е')
    probely = {'\t', '\r', '\n'}
    for char in probely:
        text = text.replace(char, ' ')
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def tokenize(text: str) -> list[str]:
    """
    Токенизация текста 
    """
    pattern = r'\w+(?:-\w+)*'
    tokens = re.findall(pattern, text)
    
    return tokens

def count_freq(tokens: list[str]) -> dict[str, int]:
    """
    считаю сколько раз встречается слово
    """
    return dict(Counter(tokens))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    """
    частые слова
    """
    sorted_items = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_items[:n]

print("normalize:")
print(normalize("ПрИвЕт\nМИр\t")) 
print(normalize("ёжик, Ёлка")) 
print(normalize("Hello\r\nWorld")) 
print(normalize("  двойные   пробелы  "))

print("tokenize:")
print(tokenize("привет мир")) 
print(tokenize("hello,world!!!"))  
print(tokenize("по-настоящему круто"))  
print(tokenize("2025 год")) 
print(tokenize("emoji 😀 не слово"))

print("count_freq:")
tokens1 = ["a", "b", "a", "c", "b", "a"]
freq1 = count_freq(tokens1)
print(freq1) 

print("top_n:")
print(top_n(freq1, 2))  

tokens2 = ["bb", "aa", "bb", "aa", "cc"]
freq2 = count_freq(tokens2)
print(freq2)  
print(top_n(freq2, 2))