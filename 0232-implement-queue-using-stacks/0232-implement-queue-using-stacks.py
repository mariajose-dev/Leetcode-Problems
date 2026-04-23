class MyQueue(object):

    def __init__(self):
        self.stack = []   # stack → used for pushing new elements (input side)
        self.queue = []   # queue → used for popping/peeking (output side)

    def push(self, x):
        self.stack.append(x)   # add element to stack (like enqueue at back)

    def pop(self):
        if not self.queue:     # if output stack is empty
            while self.stack:  # move all elements from stack → queue
                self.queue.append(self.stack.pop())  
                # pop from stack and push into queue (reverses order)

        return self.queue.pop()   # remove and return front element of queue

    def peek(self):
        if not self.queue:     # if output stack is empty
            while self.stack:  # transfer elements to maintain correct order
                self.queue.append(self.stack.pop())

        return self.queue[-1]  # return front element without removing

    def empty(self):
        return not self.stack and not self.queue  
        # queue is empty only if both stacks are empty
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()