class MyQueue:

    def __init__(self):
        self.items = []

    def push(self, x: int) -> None:
        self.items.append(x)

    def pop(self) -> int:
        return self.items.pop(0)

    def peek(self) -> int:
        return self.items[0] 

    def empty(self) -> bool:
        return self.items == []

    def __str__(self):
        return f'{self.items}'


# Your MyQueue object will be instantiated and called as such:
myQueue = MyQueue();
myQueue.push(1);
print(myQueue)
myQueue.push(2); 
print(myQueue) 
print(myQueue.peek())
print(myQueue.pop())
print(myQueue)
print(myQueue.empty());