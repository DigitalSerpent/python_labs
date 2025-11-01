# src/lib/io_helpers.py
import json
import csv
from pathlib import Path

def read_json(file_path: str) -> list:
    """Чтение JSON файла с проверкой структуры"""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    
    if path.suffix.lower() != '.json':
        raise ValueError(f"Неверный тип файла: ожидается .json, получен {path.suffix}")
    
    with path.open('r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Ошибка парсинга JSON: {e}")
    
    if not isinstance(data, list):
        raise ValueError("JSON должен содержать список")
    
    if len(data) == 0:
        raise ValueError("Пустой JSON")
    
    if not all(isinstance(item, dict) for item in data):
        raise ValueError("JSON должен содержать список словарей")
    
    return data

def read_csv(file_path: str) -> tuple[list, list[dict]]:
    """Чтение CSV файла с автоопределением разделителя"""
    path = Path(file_path)
    
    if not path.exists():
        raise FileNotFoundError(f"Файл не найден: {file_path}")
    
    if path.suffix.lower() != '.csv':
        raise ValueError(f"Неверный тип файла: ожидается .csv, получен {path.suffix}")
    
    with path.open('r', encoding='utf-8') as f:
        # Автоопределение разделителя
        sample = f.read(1024)
        f.seek(0)
        
        sniffer = csv.Sniffer()
        dialect = sniffer.sniff(sample)
        has_header = sniffer.has_header(sample)
        
        if not has_header:
            raise ValueError("CSV файл должен содержать заголовок")
        
        reader = csv.DictReader(f, dialect=dialect)
        rows = list(reader)
    
    if len(rows) == 0:
        raise ValueError("Пустой CSV файл")
    
    return reader.fieldnames, rows