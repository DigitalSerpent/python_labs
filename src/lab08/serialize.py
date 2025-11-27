import json
from pathlib import Path
from .models import Student

def students_to_json(students: list[Student], path: str) -> None:
    """
    список студентов в JSON
    """
    path_obj = Path(path)
    #папки если их нет
    path_obj.parent.mkdir(parents=True, exist_ok=True)
    
    data = [student.to_dict() for student in students]
    
    with path_obj.open('w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2, separators=(',', ': '))

def students_from_json(path: str) -> list[Student]:
    """
    список студентов ИЗ JSON 
    """
    path_obj = Path(path)
    
    if not path_obj.exists():           #проверка существования файла
        raise FileNotFoundError(path)
    
    with path_obj.open('r', encoding='utf-8') as f: #json.load(f) - читает JSON и преобразует в список словарей
        data = json.load(f)
    
    students = []
    for item in data:
        try:
            student = Student.from_dict(item)
            students.append(student)
        except (ValueError, KeyError) as e:
            print(e)
    
    return students