import argparse
import sys
import os
from pathlib import Path

try:
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx
except ImportError:
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx


def json2csv_command(args):
    """
    JSON в CSV
    """
    try:
        json_to_csv(args.input, args.output)
        print(f"сконвертировано: {args.input} → {args.output}")
    except Exception as e:
        print(f"oшибка: {e}")
        sys.exit(1)


def csv2json_command(args):
    """
    CSV в JSON
    """
    try:
        csv_to_json(args.input, args.output)
        print(f"сконвертировано: {args.input} → {args.output}")
    except Exception as e:
        print(f"oшибка: {e}")
        sys.exit(1)


def csv2xlsx_command(args):
    """
    CSV в XLSx
    """
    try:
        csv_to_xlsx(args.input, args.output)
        print(f"сконвертировано: {args.input} → {args.output}")
    except Exception as e:
        print(f"oшибка: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="CLI-конвертеры данных между форматами JSON, CSV, XLSX",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    subparsers = parser.add_subparsers(
        dest="command", help="Доступные команды конвертации"
    )

    # json2csv
    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )
    json2csv_parser.add_argument(
        "--in", dest="input", required=True, help="Входной JSON файл"
    )  # --in - как аргумент называется в командной строке, как input в args
    json2csv_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной CSV файл"
    )
    json2csv_parser.set_defaults(func=json2csv_command)

    # csv2json
    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2json_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной JSON файл"
    )
    csv2json_parser.set_defaults(func=csv2json_command)

    # csv2xlsx
    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument(
        "--in", dest="input", required=True, help="Входной CSV файл"
    )
    csv2xlsx_parser.add_argument(
        "--out", dest="output", required=True, help="Выходной XLSX файл"
    )
    csv2xlsx_parser.set_defaults(func=csv2xlsx_command)
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
        sys.exit(1)
    args.func(args)

    """
    Traceback (most recent call last):
  File "...", line X, in <module>
    args.func(args)
AttributeError: 'Namespace' object has no attribute 'func'
без использования проверки введения пользователем значений
    """


if __name__ == "__main__":
    main()
