import sys
import os
from lib.text import *
import tempfile

def main():
    '''
    создаю функцию, проверяющую кодировку введенного текста, так как павершелл читал мое 'привет' как '????!!' - не понимал кириллицу.
    '''
    input_bytes = sys.stdin.buffer.read()
    with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.txt') as f:
        f.write(input_bytes)
        founder_utf = f.name #путь к f
        
    text = ""
    encodings = ['utf-8', 'utf-16-le', 'cp1251']
    
    for encoding in encodings:
        try:
            with open(founder_utf, 'r', encoding=encoding) as f:
                candidat = f.read().strip()
                if candidat and any(c.isalpha() for c in candidat):
                    text = candidat
                    print(f"кодировка: {encoding}", file=sys.stderr)
                    print(f"текст: '{text}'", file=sys.stderr)
                    break
        except UnicodeDecodeError:
            continue
    os.unlink(founder_utf)
    
    if not text:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    
    if not tokens:
        print("Всего слов: 0")
        print("Уникальных слов: 0")
        print("Топ-5:")
        return
    
    freq_dict = count_freq(tokens)
    top_words = top_n(freq_dict, 5)
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    
    for word, count in top_words:
        print(f"{word}:{count}")

if __name__ == "__main__":
    main()