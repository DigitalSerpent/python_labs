from typing import Any, Optional, Iterator

class Node:
    """
    узел односвязного списка
    """
    def __init__(self, value: Any):
        self.value = value
        self.next: Optional['Node'] = None
    
    def __repr__(self) -> str:
        return f"Node({self.value})"


class SinglyLinkedList:
    """
    сам односвязный список
    """
    def __init__(self):
        self.head: Optional[Node] = None
        self.tail: Optional[Node] = None
        self._size = 0
    
    def append(self, value: Any) -> None:
        """добавить элемент в конец списка за O(1)"""
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self._size += 1
    
    def prepend(self, value: Any) -> None:
        """добавить элемент в начало списка за O(1)"""
        new_node = Node(value)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self._size += 1
    
    def insert(self, idx: int, value: Any) -> None:
        """вставить элемент по индексу"""
        if idx < 0 or idx > self._size:
            raise IndexError(f"индекс {idx} вне диапазона [0, {self._size}]")
        
        if idx == 0:
            self.prepend(value)
            return
        elif idx == self._size:
            self.append(value)
            return
        
        # вставка в середину
        new_node = Node(value)
        current = self.head
        for _ in range(idx - 1):
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        self._size += 1
    
    def remove_at(self, idx: int) -> None:
        """удалить элемент по индексу"""
        if idx < 0 or idx >= self._size:
            raise IndexError(f"индекс {idx} вне диапазона [0, {self._size})")
        
        if idx == 0:
            # удаление первого элемента
            self.head = self.head.next
            if self.head is None:
                self.tail = None
        else:
            # удаление из середины или с конца
            current = self.head
            for _ in range(idx - 1):
                current = current.next
            
            current.next = current.next.next
            if current.next is None:
                self.tail = current
        
        self._size -= 1
    
    def __iter__(self) -> Iterator[Any]:
        """итератор по значениям в списке"""
        current = self.head
        while current is not None:
            yield current.value
            current = current.next
    
    def __len__(self) -> int:
        """кол-во элементов в списке"""
        return self._size
    
    def __repr__(self) -> str:
        """строковое представление списка"""
        values = list(self)
        return f"SinglyLinkedList({values})"
    
    def pretty_print(self) -> str:
        """★★★Красивый вывод в формате [A] -> [B] -> [C] -> None★★★"""
        elements = []
        current = self.head
        while current is not None:
            elements.append(f"[{current.value}]")
            current = current.next
        elements.append("None")
        return " -> ".join(elements)