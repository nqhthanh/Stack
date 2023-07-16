class Phone:
    ID = None
    name = None
    price = 0
    color = None

    def __init__(self, ID, name, p, c):
        self.ID = ID
        self.name = name
        self.p = p
        self.c = c

    def printphone(self):
        print(f"ID: {self.ID} Name: {self.name} Price: {self.p} Color: {self.c}")

class Node:
    info = None
    next = None
    def __init__(self, val):
        self.info = val

class Stack:
    head = None
    def __init__(self, node):
        self.head = None
        self.info = node

    """Print all phone in the list"""
    def printall(self):
        tmp = self.head
        while tmp is not None:
            tmp.info.printphone()
            tmp = tmp.next

    """Add phone"""
    def push(self, phone):
        new_node = Node(phone)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head == None

    """Remove phone at top"""
    def pop(self):
        if self.is_empty():
            print("Stack nay rong")
            return None
        else:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            return popped_node.info

    """Get the head of stack info"""
    def front(self):
        if self.is_empty():
            print("Stack nay rong")
            return None
        else:
            return self.head.info

    """Reverse the stack"""
    def reverse(self):
        if self.is_empty():
            print("Stack nay rong")
            return None
        else:
            tmp = self.head
            pre = None
            while tmp is not None:
                next_node = tmp.next
                tmp.next = pre
                pre = tmp
                tmp = next_node
            self.head = pre

    """Remove until name = name"""
    def popuntil(self, name):
        if self.is_empty():
            print("Stack nay rong")
            return None
        else:
            while self.head.info.name != name:
                self.pop()

if __name__ == '__main__':
    p = Phone(1, 'Iphone', 1800, 'black')
    n = Node(p)
    st = Stack(n)

    st.push(p)
    print("Khoi tao stack:")
    st.printall()
    print('----------------------------------------------')

    p1 = Phone(2, 'Blackberry', 800, 'white')
    st.push(p1)
    p2 = Phone(3, 'Samsung Note 20 Ultra', 1200, 'black')
    st.push(p2)
    print("Sau khi them 2 dien thoai vao:")
    st.printall()
    print('----------------------------------------------')

    print("Dien thoai da xoa:")
    poped_node = st.pop()
    poped_node.printphone()

    print('----------------------------------------------')
    print("Stack sau khi xoa phan tu dau:")
    st.printall()

    print('----------------------------------------------')
    print("Thong tin cua dien thoai tren cung: ")
    st.front().printphone()

    print('----------------------------------------------')
    print("Stack sau khi dao nguoc: ")
    st.reverse()
    st.printall()

    print('----------------------------------------------')
    print("Stack sau khi xoa den dien thoai ten Blackberry: ")
    st.popuntil('Blackberry')
    st.printall()

