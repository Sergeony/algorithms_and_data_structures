""" Lab_10: hash tables

    Answer the questions:
        1) У хеш таблицю запиються дані з ключем та посиланням на наступний елемент.
        2) Індекс визначається хешом.
        3) Існують так звані колізії, які виникають, коли декілька ключів мають однаковий хеш.
        4) Одна операція.
        5) Синонімами є ключі з однаковим хешом.
        6) Дані можуть займати багато пам'яті.
        7) Переробити будь-які дані на валідні, одного розміру.
        8) Базові хеш-функції:
            * ділення по модулю
            * Н2(лінійне випробування, )
            * перетворення системи числення
            * середина квадрата
            * згортки
        9) без списків, ключи синоніми записуються у перший вільний рядок.
        10) записуються ключі, які і є адресами записів.
        11) Н2(лінійне випробування, наприклад)
        12) з розподіленими ланцюжками переповнень.
        13) Ключі-синоніми утворють зв'язний список, добавляючи ще одне поле.
        14) Загальна область переповнень
        15) дуже не ефективне використання пам'яті

"""


""" My own hash table implementation. """
from algorithms_and_data_structures.data_structures.my_linked_list import LinkedList


class HashTable:
    """ A hash table, based on a tuple and singly linked lists. """

    def __init__(self, size=30):
        self._size = size
        self.hashes = tuple(LinkedList() for _ in range(size))

    def _get_hash(self, key: str) -> int:
        """ Calculate the hash of the key like this:
                1) Add all the key character codes.
                2) Find the remainder after dividing sum by the size of the table.
        """
        return sum(ord(char) for char in key) % self._size

    def insert(self, key: str, value: any):
        """ Add a new item to the table.

        -Add a new node to the end of the list of keys with the same hashes
        as the hash of the given key, if there is no such key.
        -Otherwise, update the existing key with the new value.
        -Note that the hash table stores keys as the node values, and
        values as the second node values.
        """
        key_hash = self._get_hash(key)

        if self.hashes[key_hash].lookup(key) is None:
            self.hashes[key_hash].append(key)
            self.hashes[key_hash].tail.second_value = value
        else:
            for node in self.hashes[key_hash]:
                if node.value == key:
                    node.second_value = value

    def delete(self, key: str):
        """ Remove a node from the list of keys with the same hashes
        as the hash of the given key.
        """
        nodes = self.hashes[self._get_hash(key)]

        for i, node in enumerate(nodes):
            if node.value == key:
                nodes.delete(i)

    def lookup(self, key: str) -> [any, None]:
        """ Find value of the node from the list with the same hashes
        as the hash of the given key and return it.
        """
        nodes = self.hashes[self._get_hash(key)]

        for node in nodes:
            if node.value == key:
                return node.second_value
        return None

    def __str__(self):
        string = "{"
        for key_hash in self.hashes:
            for key in key_hash:
                string += str(key) + ": " + str(key.second_value) + ", "
        return string + "}"
