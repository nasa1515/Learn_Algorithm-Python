
class Queue():

    def __init__(self) -> None:
        self.stack_1 = []
        self.stack_2 = []
    
    def push(self, data):
        self.stack_1.append(data)
        
    def pop(self):
        if len(self.stack_1) == 0 and len(self.stack_2) == 0:
            raise Exception("stack all empty")

        if len(self.stack_2) == 0:
            while len(self.stack_1) != 0:
                self.stack_2.append(self.stack_1.pop())

        return self.stack_2.pop()

if __name__ == "__main__":
    
    queue = Queue()