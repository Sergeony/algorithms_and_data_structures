""" Lab_7
    1) Individual task: N=20
        20. Пріоритетна черга. Постановка запитів в чергу виконується підряд
        в кінець черги, зняття – по пріоритету. Черга організована на масиві та списку.
        Пріоритет: max значення числового параметра; при співпаданні параметрів - FIFO.

    2) Results:
            List Queue:
            Enqueue runtime:  105.1
            Dequeue runtime:  8.1
            Get node runtime:  1.2
            ------------------------
            Array Queue:
            Enqueue runtime:  34.6
            Dequeue runtime:  5.5
            Get node runtime:  1.4

    3) Conclusion:
        - ListQueue:
            * enqueue O(1)
            * dequeue O(2n)
            * get_node O(n)

        - ArrayQueue:
            * enqueue O(1)
            * dequeue O(2n)
            * get_node O(n)

        For my opinion, array queue is more faster because it uses native algorithms.
        But actual complexity is the same.
"""
from abc import ABC, abstractmethod
from time import time
from random import randrange


def main():

    # List queue usage example:
    list_queue = ListQueue()
    print("List Queue: ")

    start = time()
    randomly_fill(list_queue, 50)
    end = time()
    print("Enqueue runtime: ", round(end - start, 7) * 10**6 / 50)

    start = time()
    list_queue.dequeue()
    end = time()
    print("Dequeue runtime: ", round(end - start, 7) * 10**6)

    start = time()
    list_queue.get_node(1)
    end = time()
    print("Get node runtime: ", round(end - start, 7) * 10**6)

    print('-' * 50)

    # Array queue usage example:
    arr_queue = ArrayQueue()
    print("Array Queue: ")

    start = time()
    randomly_fill(arr_queue, 50)
    end = time()
    print("Enqueue runtime: ", round(end - start, 7) * 10**6 / 50)

    start = time()
    arr_queue.dequeue()
    end = time()
    print("Dequeue runtime: ", round(end - start, 7) * 10**6)

    start = time()
    arr_queue.get_node(1)
    end = time()
    print("Get node runtime: ", round(end - start, 7) * 10**6)


class Queue(ABC):
    """ Abstract queue class.
    """

    @abstractmethod
    def enqueue(self, value: int) -> None:
        """ Add element to the tail of the queue.
        """
        raise NotImplementedError

    @abstractmethod
    def dequeue(self) -> None:
        """ Delete element with max value.
        """
        raise NotImplementedError

    @abstractmethod
    def get_node(self, value: int):
        """ Get the element by given value.
        """
        raise NotImplementedError


class Node:
    """ Element of the list queue.
    """

    def __init__(self, value: int, next_node=None):
        self.value = value
        self.next_node = next_node

    def __str__(self):
        return str(self.value)


class ListQueue(Queue):
    """ Priority queue based on single linked list.
    """

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, value: int) -> None:
        if self.tail is None:
            self.head = self.tail = Node(value)
        else:
            self.tail.next_node = Node(value)
            self.tail = self.tail.next_node

    def dequeue(self) -> None:
        if self.head is None:
            raise IndexError("Queue is out of range.")

        max_node = self._get_max()

        if max_node == self.head.value:
            if self.head is self.tail:
                self.tail = None

            self.head = self.head.next_node
            return

        current_node = self.head

        while current_node.next_node.value != max_node:
            current_node = current_node.next_node

        if current_node.next_node is self.tail:
            self.tail = None

        current_node.next_node = current_node.next_node.next_node

    def _get_max(self) -> int:
        """ Find first max element.
        """
        current_node = self.head

        max_node = current_node.value

        while current_node is not None:
            if current_node.value > max_node:
                max_node = current_node.value

            current_node = current_node.next_node

        return max_node

    def get_node(self, value: int) -> Node:
        current_node = self.head

        if current_node is None:
            raise IndexError("Queue is out of range.")

        while current_node.value != value:
            if current_node is None:
                raise IndexError("Queue is out of range.")

            current_node = current_node.next_node

        return current_node


class ArrayQueue(Queue):
    """ Priority queue based on array.
    """

    def __init__(self):
        self.nodes = []

    def enqueue(self, value: int) -> None:
        self.nodes.append(value)

    def dequeue(self):
        if len(self.nodes) == 0:
            raise IndexError("Queue is out of range.")

        max_node = self.nodes[0]

        for i in range(len(self.nodes)):
            if self.nodes[i] > max_node:
                max_node = self.nodes[i]

        self.nodes.remove(max_node)

    def get_node(self, value: int) -> int:
        return self.nodes.index(value)


def randomly_fill(queue: Queue, count: int):
    """ Fill queue with given count of nodes with random value.
    """
    for i in range(count):
        queue.enqueue(randrange(1, 10))


if __name__ == "__main__":
    main()
