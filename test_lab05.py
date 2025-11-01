import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))
try:
    #импортирую
    from lab05.json_csv import json_to_csv, csv_to_json
    from lab05.csv_xlsx import csv_to_xlsx
    print("тест")
    os.makedirs("data/lab05/out", exist_ok=True)
    #тестирую
    print("1 - JSON → CSV")
    json_to_csv("data/lab05/samples/people.json", "data/lab05/out/people_from_json.csv")
    print("2 - CSV → JSON")
    csv_to_json("data/lab05/samples/people.csv", "data/lab05/out/people_from_csv.json")
    print("3 - CSV → XLSX")
    csv_to_xlsx("data/lab05/samples/people.csv", "data/lab05/out/people.xlsx")
    print("4 - Cities CSV → XLSX.")
    csv_to_xlsx("data/lab05/samples/cities.csv", "data/lab05/out/cities.xlsx")
    print("\n✅ УРА РАБОТАЕТ")
    print("результ: data/lab05/out/")
    
except Exception as e:
    print(f"не работает: {e}")
    import traceback
    traceback.print_exc()