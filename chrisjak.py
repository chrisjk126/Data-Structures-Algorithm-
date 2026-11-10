class Stack:
    """Implementation of a Stack Data Structure (LIFO - Last In, First Out)"""
    def __init__(self):
        self.items = []

    def push(self, item):
        """Adds an item to the top of the stack"""
        self.items.append(item)
        print(f"Pushed {item} to stack.")

    def pop(self):
        """Removes and returns the top item from the stack"""
        if not self.is_empty():
            removed = self.items.pop()
            print(f"Popped {removed} from stack.")
            return removed
        print("Stack Underflow: Stack is empty.")
        return None

    def peek(self):
        """Returns the top item without removing it"""
        if not self.is_empty():
            return self.items[-1]
        return "Stack is empty."

    def is_empty(self):
        """Checks if the stack has no elements"""
        return len(self.items) == 0

    def size(self):
        """Returns the total number of items in the stack"""
        return len(self.items)


class Queue:
    """Implementation of a Queue Data Structure (FIFO - First In, First Out)"""
    def __init__(self, capacity=5):
        self.items = []
        self.capacity = capacity

    def enqueue(self, item):
        """Inserts an item at the rear of the queue"""
        if not self.is_full():
            self.items.append(item)
            print(f"Enqueued {item} to queue.")
        else:
            print("Queue Overflow: Queue is full.")

    def dequeue(self):
        """Removes and returns the front item from the queue"""
        if not self.is_empty():
            removed = self.items.pop(0)
            print(f"Dequeued {removed} from queue.")
            return removed
        print("Queue Underflow: Queue is empty.")
        return None

    def peek(self):
        """Returns the front item without removing it"""
        if not self.is_empty():
            return self.items[0]
        return "Queue is empty."

    def is_empty(self):
        """Checks if the queue has no elements"""
        return len(self.items) == 0

    def is_full(self):
        """Checks if the queue has reached its maximum capacity"""
        return len(self.items) >= self.capacity


# --- Testing the Operations ---
if __name__ == "__main__":
    print("--- Testing Stack Operations ---")
    my_stack = Stack()
    my_stack.push("A")
    my_stack.push("B")
    print(f"Stack Size: {my_stack.size()}")
    print(f"Top element (Peek): {my_stack.peek()}")
    my_stack.pop()
    print(f"Is stack empty? {my_stack.is_empty()}\n")

    print("--- Testing Queue Operations ---")
    my_queue = Queue(capacity=3)
    my_queue.enqueue("A")
    my_queue.enqueue("B")
    print(f"Front element (Peek): {my_queue.peek()}")
    print(f"Is queue full? {my_queue.is_full()}")
    my_queue.dequeue()
    print(f"Is queue empty? {my_queue.is_empty()}")