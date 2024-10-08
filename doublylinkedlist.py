class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        
    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return
        
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)
        
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return
            
        last_node = self.get_last_node()
        itr = last_node
        #itr = self.head
        llstr = ''
        
        while itr:
            llstr += str(itr.data) + '-->'
            itr = itr.prev
        
        
        print("Link list in reverse: ", llstr)
        
        
    def get_last_node(self):
        cur = self.head
        
        while cur.next:
            cur = cur.next
            
        return cur
    
    def get_length(self):
        count = 0
        cur = self.head
       
        while cur.next:
            cur = cur.next 
            count += 1
        
        return count
        
    def insert_at_beginning(self, data):
        if self.head == None:
            node = Node(data)
            node.prev = self.head
            self.head = node
        
        else:
            node = Node(data)
            node.prev = self.head
            self.head.prev = node
            self.head = node
            
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data)
            return
        
        
        cur = self.head
        
        while cur.next:
            cur = cur.next
            #cur.prev = cur
            
        cur.next = Node(data)
        cur.prev = cur
        
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
            
        count = 0
        cur = self.head
        
        while cur:
            if count == index - 1:
                node = Node(data)
                if node.next:
                    node.next.prev = node
                cur.next = node
                break
                
            cur = cur.next
            count += 1
        
    def remove_at(self, index):
        pass
        
    
    def insert_values(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)
            
        #for data in data_list:    
         #   self.insert_at_beginning(data)
            
        

if __name__ == "__main__":
    DLL = DoublyLinkedList()
    DLL.insert_values([0,12,4,5,2,30,23])
    DLL.print_forward()
    DLL.print_backward()
    