import sys
import os
sys.path.append(os.path.dirname(__file__))

from src.lab10.structures import Stack, Queue
from src.lab10.linked_list import SinglyLinkedList
print("-- 10 лаба --")

def test_stack():
    print("Тестирование Stack")
    stack = Stack()
    
    #добавление элементов
    stack.push("первый")
    stack.push("второй")
    stack.push("третий")
    print(f"Стек после добавления: {stack}")
    
    #просмотр верхнего элемента
    print(f"Верхний элемент: {stack.peek()}")
    
    #извлечение элементов
    print(f"Извлечен: {stack.pop()}")
    print(f"Извлечен: {stack.pop()}")
    print(f"Стек после извлечения: {stack}")
    print(f"Пуст ли стек: {stack.is_empty()}")
    print()

def test_queue():
    print("Тестирование Queue")
    queue = Queue()
    
    # Добавление элементов
    queue.enqueue("первый")
    queue.enqueue("вторый")
    queue.enqueue("третий")
    print(f"Очередь после добавления: {queue}")
    
    # Просмотр первого элемента
    print(f"Первый элемент: {queue.peek()}")
    
    # Извлечение элементов
    print(f"Извлечен: {queue.dequeue()}")
    print(f"Извлечен: {queue.dequeue()}")
    print(f"Очередь после извлечения: {queue}")
    print(f"Пуста ли очередь: {queue.is_empty()}")
    print()

def test_linked_list():
    print("Тестирование SinglyLinkedList")
    lst = SinglyLinkedList()
    
    # Добавление в конец
    lst.append("A")
    lst.append("B")
    lst.append("C")
    print(f"Список после append: {lst}")
    print(f"Красивый вывод: {lst.pretty_print()}")
    
    # Добавление в начало
    lst.prepend("начало")
    print(f"После prepend: {lst}")
    print(f"Красивый вывод: {lst.pretty_print()}")
    
    # Вставка по индексу
    lst.insert(2, "середина")
    print(f"После insert(2): {lst}")
    print(f"Красивый вывод: {lst.pretty_print()}")
    
    # Удаление по индексу
    lst.remove_at(1)
    print(f"После remove_at(1): {lst}")
    print(f"Красивый вывод: {lst.pretty_print()}")
    
    # Итерация
    print("Итерация по списку:")
    for item in lst:
        print(f"  - {item}")
    
    print(f"Длина списка: {len(lst)}")

def main():
    print("-- ЛР10 - Структуры данных --\n")
    test_stack()
    test_queue()
    test_linked_list()

if __name__ == "__main__":
    main()