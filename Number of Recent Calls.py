class RecentCounter:

    def __init__(self):
        self.count=0
        self.queue=[None]
        self.out=[None]

    def ping(self, t):
        range1=[t-3000, t]
        self.queue.append(t)
        self.count+=1
        j=-1
        which=self.queue[j]
        while which!=None:
            # print(range)
            if which not in range(range1[0],range1[1]+1):
                print("hell yes")
                self.count-=1
                self.queue.pop(j)
                j+=1
            j -= 1
            which=self.queue[j]
        self.out.append(self.count)
        print(self.out)
oobj=RecentCounter()
oobj.ping(642)
oobj.ping(1849)
oobj.ping(4921)
oobj.ping(5936)
oobj.ping(5957)
