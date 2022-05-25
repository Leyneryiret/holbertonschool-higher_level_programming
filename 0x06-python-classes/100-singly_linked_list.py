#!/usr/bin/python3
"""Creating a new class called Node"""


class Node:
    """class Node that defines a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialize Node with nodo attribute"""
        self.data = data
        self.next_node = next_node
        
        @property
        def data(self):
            """Method to retrieve the data"""
            return (self.__data)
        
        @data.setter
        def data(self, value):
            """Setting a new value"""
            if type(value) is not int:
                raise TypeError("data must be an integer")
            else:
                self.__data = value

         @property
         def next_node(self):
             """Method to retrieve the next_node"""
             return (self.__next_node)
         
         @next_node.setter
         def next_node(self, value):
             """Setting a new value"""
             if value == Node or value == None:
                 self.__next_node = value
             else:
                 raise TypeError("next_node must be a Node object")

"""  Singly linked list class """


class SinglyLinkedList:
    """ Init instantiate method """
    def __init__(self):
        self.__head = None

    """ Str method to print """
    def __str__(self):
        datalist = []
        actual_node = self._SinglyLinkedList__head
        while actual_node:
            datalist.append(str(actual_node.data))
            actual_node = actual_node.next_node
        return '\n'.join(datalist)

    """ Sorted Insert - inserts a new Node into the correct sorted
    position in the list (increasing order) """
    def sorted_insert(self, value):
        actual_node = self._SinglyLinkedList__head
        if not actual_node:
            new_node = Node(value, None)
            self._SinglyLinkedList__head = new_node
        elif value < actual_node.data:
            new_node = Node(value, actual_node)
            self._SinglyLinkedList__head = new_node
        else:
            while (actual_node.next_node):
                if value < actual_node.next_node.data:
                    break
                else:
                    actual_node = actual_node.next_node
                new_node = Node(value, actual_node.next_node)
                actual_node.next_node = new_node
