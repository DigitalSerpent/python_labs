import json
import csv
from pathlib import Path
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from lib.io_helpers import read_json, read_csv

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    JSON-файл в CSV
    список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строчками
    """
    #чтение и валидация JSON
    data = read_json(json_path)
    #определение полей 
    all_fields = set()
    for item in data:
        all_fields.update(item.keys())
    fieldnames = sorted(all_fields)
    #создание директории для выходного файла, если её нет
    output_path = Path(csv_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    #запись CSV
    with output_path.open('w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for item in data:
            #заполнение отсутствующих полей пустыми строчками
            row = {field: item.get(field, '') for field in fieldnames}
            writer.writerow(row)
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    CSV в JSON 
    """
    #чтение и валидация CSV
    fieldnames, rows = read_csv(csv_path)
    #создание директории для выходного файла, если её нет
    output_path = Path(json_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    #запись JSON
    with output_path.open('w', encoding='utf-8') as json_file:
        json.dump(rows, json_file, ensure_ascii=False, indent=2)