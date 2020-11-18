# Another approac to linked list wrapper class to demonstrate how
# linked lists are created, indexed, and accessed
class Node(object):
    def __init__ (self, d, n=None):
        self.data = d
        self.next_node = n
        
    def get_next(self):
        return self.next_node
    
    def set_next(self, n):
        self.next_node = n
        
    def get_data(self):
        return self.data
    
    def set_data(self, d):
        self.data = d

class LinkedList(object):
    
    def __init__(self, r=None):
        self.root = r
        self.size = 0
    
    def get_size(self):
        return self.size
    
    def add(self, d):
        new_node = Node(d, self.root)
        self.root = new_node
        self.size += 1
        
    def remove(self, d):
        cur_node = self.root
        prev_node = None
        while cur_node:
            if cur_node.get_data() == d:
                if prev_node:
                    prev_node.set_next(cur_node.get_next())
                else:
                    self.root = cur_node
                self.size -= 1
                return True # data found and removed
                
            else:
                prev_node = cur_node
                cur_node = cur_node.get_next()
        
        return False # Data not found or removed
    
    def find(self, d):
        cur_node = self.root
        while cur_node:
            if cur_node.get_data() == d:
                return d
            else:
                cur_node = cur_node.get_next()
        return None
    
    
myList = LinkedList()
myList.add(3)
myList.add(4)
myList.add(8)
myList.add(5)
myList.remove(8)
print(myList.remove(5))
print(myList.find(5))

        