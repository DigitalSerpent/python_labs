import sys
import os
sys.path.append(os.path.dirname(__file__))

from src.lab09.group import Group
from src.lab08.models import Student

def main():
    print("--  9 Лаба  --")
    
    #инициализация группы
    group = Group("data/lab09/students.csv")   #group становится нашей "базой данных" студентов
    print("инициализирована")
    
    #добавление студентов
    print("\n1. добавление студентов:")
    student1 = Student("Иванов Иван Иванович", "2005-05-15", "SE-01", 4.5)
    student2 = Student("Гусева Мария Александровна", "2001-01-01", "CS-02", 3.8)
    student3 = Student("Корней Корнеевич", "1923-08-20", "AI-03", 4.9)
    
    group.add(student1)
    group.add(student2)
    group.add(student3)
    print("добавлены")
    
    #вывод списка
    print("\n2. список всех студентов:")
    all_students = group.list()
    for student in all_students:
        print(f"  - {student}")
    
    #поиск
    print("\n3. поиск по подстроке 'Иван':")
    found = group.find("Иван")
    for student in found:
        print(f"  - Найден: {student}")
    
    #обновление
    print("\n4. Обновление GPA студента Иванов:")
    group.update("Иванов Иван Иванович", gpa=4.8)
    print("GPA обновился")
    
    #статистика
    print("\n5. статистика группы:")
    stats = group.stats()
    print(f"  Количество студентов: {stats['count']}")
    print(f"  Средний GPA: {stats['avg_gpa']:.2f}")
    print(f"  Группы: {stats['groups']}")
    
    #удаление
    print("\n6. удаление студента Гусевой:")
    if group.remove("Гусева Мария Александровна"):
        print("студент удален")
    else:
        print("студент не найден")
        
    #финальный список
    print("\n7. финальный список студентов:")
    final_students = group.list()
    for student in final_students:
        print(f"  - {student}")

if __name__ == "__main__":
    main()