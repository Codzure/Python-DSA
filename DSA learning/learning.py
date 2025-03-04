

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1


    def print_linked_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next 


    def append(self, value): 
        new_node = Node(value) 
        if self.head is None: 
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True
    
    def pop(self, value):
        if self.head is None:
            return None

        temp = self.head
        pre = self.head

        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        pre.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp

my_linkedList = LinkedList(1)
my_linkedList.append(2)
my_linkedList.append(3)
my_linkedList.append(4)
my_linkedList.pop(4)

my_linkedList.print_linked_list()

