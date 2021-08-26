"""Add a couple methods to our LinkedList class,
and use that to implement a Stack.
You have 4 functions below to fill in:
insert_first, delete_first, push, and pop.
Think about this while you're implementing:
why is it easier to add an "insert_first"
function than just use "append"?"""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def insert_first(self, new_element):
        "Insert new element as the head of the LinkedList"
        if self.head is None:
             self.head = Element(new_element)
        else:
            newnode = Element(new_element)
            newnode.next = self.head
            self.head = newnode

    def delete_first(self):
        "Delete the first (head) element in the LinkedList as return it"
        # pass\
        if self.head:
            previous = self.head
            if previous.next:   
                deleted = previous.value         
                self.head = previous.next
            else:
                value = previous.value
                deleted = Element(value)
                self.head.value = None
            return deleted
        else:
            return None

class stack(object):
    def __init__(self,top=None):
        self.ll = LinkedList(top)

    def push(self, new_element):
        "Push (add) a new element onto the top of the stack"
        # pass
        self.ll.insert_first(new_element)

    def pop(self):
        "Pop (remove) the first element off the top of the stack and return it"
        # pass
        deleted = self.ll.delete_first()
        if(deleted.value is None):
            return None
        else:
            return deleted
    