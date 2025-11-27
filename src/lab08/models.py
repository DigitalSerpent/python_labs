from dataclasses import dataclass
from datetime import datetime, date
import re

@dataclass
class Student:
    fio: str
    birthdate: str  #YYYY-MM-DD
    group: str
    gpa: float      #0-5
    
    def __post_init__(self):
        #дата
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError(f"неверный формат у даты:{self.birthdate}")
        
        #GPA
        if not (0 <= self.gpa <= 5):
            raise ValueError(f"неверный формат гпа: {self.gpa}")
        
        #фио
        if len(self.fio.split()) < 2:
            raise ValueError(f"неверный формат у фио: {self.fio}")
    
    def age(self) -> int:
        """возвращает колво полных лет"""
        birth_date = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        age = today.year - birth_date.year
        
        #проверка на то, был ли уже др
        if today.month < birth_date.month or (today.month == birth_date.month and today.day < birth_date.day):
            age -= 1 
        return age
    
    def to_dict(self) -> dict:
        """преобразует объект в словарь для сериализации"""
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa
        }
    
    @classmethod
    def from_dict(cls, data: dict):
        """создает объект из словаря"""
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"]
        )
    
    def __str__(self):
        """вывод информации о студенте"""
        return f"Студент: {self.fio}, {self.age()} лет, группа {self.group}, GPA: {self.gpa}"