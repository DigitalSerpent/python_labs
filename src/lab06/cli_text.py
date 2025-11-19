import argparse
import sys
import os
from pathlib import Path
import re
from collections import Counter


def read_text_simple(path: str, encoding: str = "utf-8") -> str:
    """
    чтение текста
    """
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {path}")
    return path.read_text(encoding=encoding)


try:
    from lib.text import normalize, tokenize, count_freq, top_n
except ImportError:
    try:
        sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
        from lib.text import normalize, tokenize, count_freq, top_n
    except ImportError:
        print("не удалось импортировать функции из lib/text.py")
        sys.exit(1)


def print_table(top_words):
    if not top_words:
        return
    max_word_len = max(len(word) for word, count in top_words)
    word_width = max(max_word_len, 5)
    print(f"{'слово':<{word_width}} | частота")
    print("-" * (word_width + 11))
    for word, count in top_words:
        print(f"{word:<{word_width}} | {count}")


def cat_command(args):
    """
    cat - вывод содержимого файла
    """
    try:
        content = read_text_simple(args.input)
        lines = content.split("\n")
        for i, line in enumerate(lines, 1):
            if args.n:  # проверка флага в аргументах командной строки
                print(f"{i:6d}\t{line}")
            else:
                print(line)

    except FileNotFoundError:
        print(f"файл '{args.input}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"ошибка при чтении файла: {e}")
        sys.exit(1)


def stats_command(args):
    """
    stats - анализ частот слов
    """
    try:
        text = read_text_simple(args.input, encoding="utf-8")
        normalized_text = normalize(text)
        tokens = tokenize(normalized_text)
        word_counts = count_freq(tokens)
        top_words = top_n(word_counts, args.top)

        print(f"Всего слов: {len(tokens)}")
        print(f"Уникальных слов: {len(set(tokens))}")
        print(f"Топ-{args.top}:")

        print_table(top_words)

    except FileNotFoundError:
        print(f"Ошибка: файл '{args.input}' не найден")
        sys.exit(1)
    except Exception as e:
        print(f"ошибка при анализе текста: {e}")
        sys.exit(1)


def main():
    """
    хелпер
    """
    parser = argparse.ArgumentParser(  # ArgumentParser = "анализатор аргументов", cоздает объект, который умеет парсить командную строку
        description="CLI-утилиты для анализа текста",
        formatter_class=argparse.RawDescriptionHelpFormatter,  # типа форматируй справку как есть, без авто-переносов
    )  # argparse.RawDescriptionHelpFormatter - это встроенный класс в библиотеке argparse
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла")
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу")
    cat_parser.add_argument("-n", action="store_true", help="Нумеровать строки")
    cat_parser.set_defaults(func=cat_command)

    stats_parser = subparsers.add_parser("stats", help="частоты слов в тексте")
    stats_parser.add_argument("input", help="Путь к текстовому файлу")
    stats_parser.add_argument(
        "top", nargs="?", type=int, default=5, help="Кол-во топ-слов"
    )
    stats_parser.set_defaults(func=stats_command)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    args.func(args)


if __name__ == "__main__":
    main()
