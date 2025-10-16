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
    probely = ['\t', '\r', '\n'] #табуляция - \t, перевод строки - \n, возврат каретки - \r
    for char in probely:
        text = text.replace(char, ' ')
    text = re.sub(r'\s+', ' ', text).strip()

    return text

def tokenize(text: str) -> list[str]:
    """
    Токенизация текста
    """
    pattern = r'[a-zA-Zа-яёА-ЯЁ0-9_]+(?:-[a-zA-Zа-яёА-ЯЁ0-9_]+)*'
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