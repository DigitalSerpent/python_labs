from collections import deque
from typing import Any, Optional

class Stack:
    """
    cтек (LIFO) - Last In, First Out
    """
    def __init__(self):
        self._data = []
    
    def push(self, item: Any) -> None:
        """добавить элемент на вершину стека"""
        self._data.append(item)
    
    def pop(self) -> Any:
        """снять верхний элемент стека и вернуть его"""
        if self.is_empty():
            raise IndexError("пустой стек")
        return self._data.pop()
    
    def peek(self) -> Optional[Any]:
        """вернуть верхний элемент без удаления"""
        if self.is_empty():
            return None
        return self._data[-1]
    
    def is_empty(self) -> bool:
        """проверить пустой ли стек"""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """кол-во элементов в стеке"""
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Stack({self._data})"


class Queue:
    """
    очередь (FIFO) - First In, First Out
    """
    def __init__(self):
        self._data = deque()
    
    def enqueue(self, item: Any) -> None:
        """добавить элемент в конец очереди"""
        self._data.append(item)
    
    def dequeue(self) -> Any:
        """взять элемент из начала очереди и вернуть его"""
        if self.is_empty():
            raise IndexError("пустая очередб")
        return self._data.popleft()
    
    def peek(self) -> Optional[Any]:
        """вернуть первый элемент без удаления"""
        if self.is_empty():
            return None
        return self._data[0]
    
    def is_empty(self) -> bool:
        """проверить пустая ли очередь"""
        return len(self._data) == 0
    
    def __len__(self) -> int:
        """кол-во элементов в очереди"""
        return len(self._data)
    
    def __repr__(self) -> str:
        return f"Queue({list(self._data)})"