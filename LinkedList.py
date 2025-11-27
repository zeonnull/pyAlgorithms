

class LinkedList:
    class __Node:
        def __init__(self, value):
            self.value = value
            self.next = None

        def __repr__(self):
            return f'value={self.value}'

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add_first(self, value):
        new_node = self.__Node(value)
        if self.__head is None:
            self.__head = self.__tail = new_node
        else:
            new_node.next = self.__head
            self.__head = new_node

    def add_last(self, value):
        if self.__head is None:

        new_node = self.__Node(value)
        self.__tail.next = new_node