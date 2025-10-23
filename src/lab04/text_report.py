import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv


def main():
    input_path = "data/lab04/input.txt"
    output_path = "data/lab04/report.csv"
    
    try:
        text = read_text(input_path, encod="utf-8")
    except FileNotFoundError:
        print(f"Ошибка: {input_path} не найден")
        sys.exit(1)
    except UnicodeDecodeError:
        print(f"Ошибка: падает {input_path}")
        sys.exit(1)
    
    normalized_text = normalize(text)
    tokens = tokenize(normalized_text)
    
    freq_dict = count_freq(tokens)
    sorted_words = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    
    rows = [(word, count) for word, count in sorted_words]
    write_csv(rows, output_path, header=("word", "count"))
    
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {len(freq_dict)}")
    print("Топ-5:")
    
    top_words = top_n(freq_dict, 5)
    for word, count in top_words:
        print(f"{word}:{count}")


if __name__ == "__main__":
    main()