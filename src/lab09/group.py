import csv
from pathlib import Path
from typing import List
from src.lab08.models import Student

class Group:
    def __init__(self, storage_path: str):
        """
        инициализация группы с путем к CSV
        """
        self.path = Path(storage_path)
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """
        файл с заголовком, если его нет
        """
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with self.path.open('w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['fio', 'birthdate', 'group', 'gpa'])
    
    def _read_all(self) -> List[dict]:
        """
         записи из CSV 
        """
        students = []
        with self.path.open('r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                #GPA в float
                row['gpa'] = float(row['gpa'])
                students.append(row)
        return students
    
    def _write_all(self, students: List[dict]):
        """
        записи в CSV 
        """
        with self.path.open('w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=['fio', 'birthdate', 'group', 'gpa'])
            writer.writeheader()
            writer.writerows(students)
    
    def list(self) -> List[Student]:
        """
        студенты как объектыы Student
        """
        rows = self._read_all()
        students = []
        for row in rows:
            try:
                student = Student.from_dict(row)
                students.append(student)
            except (ValueError, KeyError) as e:
                print(e)
        return students
    
    def add(self, student: Student):
        """
        новый студент в CSV
        """
        rows = self._read_all()
        #проверка на одноименника
        for row in rows:
            if row['fio'] == student.fio:
                raise ValueError(f"ФИО '{student.fio}' есть уже")
        
        rows.append(student.to_dict())
        self._write_all(rows)
    
    def find(self, substr: str) -> List[Student]:
        """
        находит студента по подстроке в ФИО
        """
        all_students = self.list()
        return [s for s in all_students if substr.lower() in s.fio.lower()]
    
    def remove(self, fio: str) -> bool:
        """
        удаляет студента по ФИО
        возвращает True если студент был удален, False если не нашел
        """
        rows = self._read_all()
        initial_count = len(rows)
        
        rows = [row for row in rows if row['fio'] != fio]
        
        if len(rows) < initial_count:
            self._write_all(rows)
            return True
        return False
    
    def update(self, fio: str, **fields):
        """
        обновляет поля существующего студента
        """
        rows = self._read_all()
        updated = False
        
        for row in rows:
            if row['fio'] == fio:
                for field, value in fields.items():
                    if field in row:
                        row[field] = value
                updated = True
                break
        
        if updated:
            self._write_all(rows)
        else:
            raise ValueError(f"ФИО '{fio}' не найден")
    
    def stats(self) -> dict:
        """
        ★ доп задание со звездочкой: статистика по группе ★
        """
        students = self.list()
        if not students:
            return {
                "count": 0,
                "min_gpa": 0,
                "max_gpa": 0,
                "avg_gpa": 0,
                "groups": {},
                "top_5_students": []
            }
        
        gpas = [s.gpa for s in students]
        groups = {}
        
        for student in students:
            groups[student.group] = groups.get(student.group, 0) + 1
        
        # сортировочка по gpa по убыванию
        sorted_students = sorted(students, key=lambda s: s.gpa, reverse=True)
        top_5 = [{"fio": s.fio, "gpa": s.gpa} for s in sorted_students[:5]]
        
        return {
            "count": len(students),
            "min_gpa": min(gpas),
            "max_gpa": max(gpas),
            "avg_gpa": sum(gpas) / len(gpas),
            "groups": groups,
            "top_5_students": top_5
        }