class Node:
    def __init__(self,value):
        self.item = value
        self.next = None
        self.previos = None
    
    def get_item(self):
        return self.item

    def __str__(self):
        return str(self.item)
    
    def __repr(self):
        return self.__str__()
class DCLL:
    def __init__(self):
        self.head = None
        self.size = 0 
        self.end = None

    def __iter__(self):
      return iterate(self)

    def append(self, value):
        if self.head == None:
            a = Node(value)
            self.head = a
            self.end = a
            self.size += 1 
        else:
            b = Node(value)
            b.previos = self.end
            self.end.next = b
            self.end = b 
            self.head.previos = self.end
            self.end.next = self.head
            self.size += 1 

    def index(self, index):
        if index >= 0:
            if self.size - index < index:
                count = self.size
                current = self.end 
                index += 1 
                while count != index:
                    current = current.previos
                    count -= 1
                return current
            else:
                count = 0
                current = self.head
                while count != index:
                    current = current.next
                    count += 1
                return current
        else:                                   #for negative numbers
            if -index < self.size + index:
                current = self.end
                count = -1
                while count != index:
                    current = current.previos
                    count -= 1
                return current
            else:
                current = self.head
                count = 0
                while count != self.size + index:
                    current = current.next
                    count += 1 
                return current
    
    def pop(self, index):
        current = self.index(index)
        backone = current.previos
        nextone = current.next
        if self.head == current:
            self.head = nextone
        if self.end == current:
            self.end = backone
        backone.next = nextone
        nextone.previos = backone
        self.size -= 1 
        return current
    
    def getlenth(self):
        return self.size

    def __str__(self):
        count = 0
        description = '['
        current = self.head
        while count != self.size-1 :
            description += str(current.item) + ", "
            current = current.next
            count += 1  
        description += str(current.item)
        return description + "]"  
    
    def clear(self):
        self.head = None
        self.size = 0 
        self.end = None
    
class iterate:
    def __init__(self,windowlist):
        self.windowlist = windowlist
        self.current = windowlist.head
        self.count = 0
        self.size = windowlist.getlenth()
    def __next__(self):
        if self.current is not None:
            self.count += 1 
            temp = self.current.item
            self.current = self.current.next
            if self.count != self.size:
                return temp    
        else:
            raise StopIteration




    
    
    
    






