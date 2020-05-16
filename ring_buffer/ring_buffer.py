class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        self.size = 0
        self.oldest = 0


    def append(self, item):
        if self.size < self.capacity: 
            #if size is less than capacity just add to buffer
            self.storage.append(item)
            self.size += 1

            print(self.storage, self.oldest)
            #if size == capacity remove oldest and add to buffer
        elif self.size == self.capacity:
            self.storage[self.oldest] = item
            self.oldest += 1
        
            if self.oldest == self.capacity:
                self.oldest = 0


    def get(self):
        return self.storage

# A ring buffer is a non-growable buffer with a fixed size. 
# When the ring buffer is full and a new element is inserted, the oldest element in the ring buffer is overwritten with the newest element. This kind of data structure is very useful for use cases such as storing logs and history information, where you typically want to store information up until it reaches a certain age, after which you don't care about it anymore and don't mind seeing it overwritten by newer data.

# Implement this behavior in the RingBuffer class. RingBuffer has two methods, `append` and `get`. The `append` method adds the given element to the buffer. The `get` method returns all of the elements in the buffer in a list in their given order. It should not return any `None` values in the list even if they are present in the ring buffer.

buffer = RingBuffer(5)

buffer.append(1)
buffer.append(2)
buffer.append(3)
buffer.append(4)

