import pytest
import json
import csv
from pathlib import Path
from src.lab05.json_csv import json_to_csv, csv_to_json


def test_json_to_csv_basic(tmp_path):
    """JSON в CSV"""
    # тестовый JSON
    src = tmp_path / "test.json"
    data = [{"name": "Alice", "age": 25}]
    src.write_text(json.dumps(data), encoding="utf-8")
    dst = tmp_path / "output.csv"
    json_to_csv(str(src), str(dst))
    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        rows = list(reader)
    assert len(rows) == 1
    assert rows[0]["name"] == "Alice"


def test_csv_to_json_basic(tmp_path):
    """CSV в JSON"""
    src = tmp_path / "test.csv"
    with src.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Maria", "age": "30"})
    dst = tmp_path / "output.json"
    csv_to_json(str(src), str(dst))
    assert dst.exists()
    with dst.open(encoding="utf-8") as f:
        data = json.load(f)
    assert len(data) == 1
    assert data[0]["name"] == "Maria"
