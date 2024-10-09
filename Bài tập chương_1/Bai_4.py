class Stack:
    def __init__(self, capacity):
        self.capacity = capacity  
        self.data = []            

    def push(self, value):
        if self.isFull():
            print("Ngăn xếp đã đầy, không thể thêm phần tử.")
            return
        self.data.append(value)   
    def pop(self):
        if self.isEmpty():
            print("Ngăn xếp rỗng, không thể lấy phần tử.")
            return None
        return self.data.pop()    

    def isEmpty(self):
        return len(self.data) == 0  
    def isFull(self):
        return len(self.data) >= self.capacity  
if __name__ == "__main__":
    stack = Stack(5)  
    stack.push(1.1)
    stack.push(2.2)
    stack.push(3.3)
    stack.push(4.4)
    stack.push(5.5)
    stack.push(6.6)  
    while not stack.isEmpty():
        print("Phần tử lấy ra:", stack.pop())

    stack.pop()  