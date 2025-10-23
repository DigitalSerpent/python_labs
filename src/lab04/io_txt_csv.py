import csv
from pathlib import Path


def read_text(path, encod="utf-8"):#как в задании, читает файл и отдает текст
    path = Path(path)
    return path.read_text(encoding=encod)#метод Path, который читает весь файл и возвращает текст

def write_csv(rows, path, header=None):#запись таблицы
    path = Path(path)
    rows = list(rows)
    
    if rows:
        first_len = len(rows[0])
        for i, row in enumerate(rows):
            if len(row) != first_len:
                raise ValueError() 
    path.parent.mkdir(parents=True, exist_ok=True)#ошибка длин строк
    
    with path.open("w", newline="", encoding="utf-8") as file: #w - открыть для записи
        writer = csv.writer(file)
        writer.writerows(rows) #записываю все строки данных в файл


def ensure_parent_dir(path):#создание папок
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)