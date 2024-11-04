class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        
    def print_list(self):
        cur_node = self.head
        string = ""
        while cur_node:
            string += str(cur_node.data)
            if cur_node.next:
                string += " → "
            cur_node = cur_node.next
        print(string)