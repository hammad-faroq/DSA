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
class Process:
    def __init__(self, processId, processName, processExecTime):
        self.processId = processId
        self.processName = processName
        self.processExecTime = processExecTime
class Scheduler:
    def __init__(self, processArray, processArrayLength, timeQuantum):
        self.processArray = processArray
        self.processArrayLength = processArrayLength
        self.timeQuantum = timeQuantum
    def assign_processor(self,max=0):
        exe = self.processArray[0].processExecTime
        if exe == 0 or exe - self.timeQuantum < 0:
            return
        # for i in range(len(self.processArray)):
        #     exe=self.processArray[i].processExecTime
        #     max=exe
        for i in range(len(self.processArray)):
            exe=self.processArray[i].processExecTime
            if exe==0 or exe-self.timeQuantum<0:
                continue
            exe=exe-self.timeQuantum
            self.processArray[i].processExecTime=exe
            print(f"Executing Process {self.processArray[i].processName} for {self.processArray[i].processExecTime} Units.")
        self.assign_processor()
def mian():
    arr = [Process(1, "notepad", 20), Process(13, "mp3player", 5), Process(4,
                                                                           "bcc", 30), Process(11, "explorer", 2)]

    s = Scheduler(arr, 4, 5)
    s.assign_processor()
mian()


