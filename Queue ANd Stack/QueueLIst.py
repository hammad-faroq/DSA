class QueueLinkedList:
    """THis Class will Implement the Queue FUnctionality using linkned list methodology"""
    def __init__(self,max_size):
        self.head=self.tail=-1
        self.max_size=max_size
        self.count=0
        self.queue=[]
    def enqueue(self,data):
        if len(self.queue)==self.max_size:
            print("MAXsizE!")
            return
        elif self.head==self.tail==-1:
            self.queue.insert(0,data)
            self.head=self.tail=data
        else:
            self.queue.insert(0,data)
            self.head=data
            self.tail=self.queue[len(self.queue)-1]
    def dequeue(self):
        if self.head == self.tail == -1:
            return
        else:
            print(self.tail)
            self.queue.remove(self.tail)
    def is_empty(self):
        if self.head==self.tail==-1:
            return True
        return False
    def is_full(self):
        if len(self.queue)==self.max_size:
            return True
        return False

    def show(self):
        for i in self.queue:
            print(i)
q=QueueLinkedList(5)
q.enqueue("Haseeb")
q.enqueue("HAroon")
q.enqueue("Haris")
q.enqueue("Hammad")
q.show()
print()
q.dequeue()
print()
q.show()

