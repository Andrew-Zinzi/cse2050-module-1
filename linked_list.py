from node import Node
class LinkedList():
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self, item):
        if self.size == 0:
            self.head = Node(item)
            self.tail = self.head
        else:
            newHead = Node(item, self.head)
            self.head = newHead
        self.size =+ 1

    def add_last(self, item):
        if self.size == 0:
            self.tail = Node(item)
            self.head = self.tail
        else:
            newTail = Node(item, self.tail)
            self.tail = newTail
        self.size =+ 1
    
    def remove_first(self):
        if self.size == 0:
            return None
        
        elif self.size == 1:
            removeHead = self.head
            removeTail = self.tail
            self.head = self.head.next
            removeHead.next = None
            self.tail = self.tail.next
            self.size =- 1
            return removeHead, removeHead.data

        
        else:
            removeHead = self.head
            self.head = self.head.next
            removeHead.next = None
            self.size =- 1
            return removeHead, removeHead.data
    def get_first(self):
        if self.size == 0:
            return None
        else:
            return self.head, self.head.data

    def is_empty(self):
        return self.size == 0

    def size(self):
        return self.size
    
        

        
        
            
