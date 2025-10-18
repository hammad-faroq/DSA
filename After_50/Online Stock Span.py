class StockSpanner:

    def __init__(self):
        self.l=[]

    def next(self, price: int) -> int:
        hoa=False
        c = 1
        if self.l==[]:
            self.l.append((price,1))
            return 1
        else:

            while self.l!=[]:
                prev,count=self.l[-1]
                if prev <= price:
                    c+=count
                    self.l.pop()
                    hoa=True
                # if prev>price:
                #     if hoa:
                #         self.l.append((prev, count))
                #         self.l.append((price, c))
                #         hoa = False
                #         return  count+c

                else:
                        # self.l.append((prev, count))
                        # self.l.append((price, 1))
                        # return 1
                    break
            self.l.append((price, c))
            return c
s=StockSpanner()
print(s.next(100))
print(s.next(80))
print(s.next(60))
print(s.next(70))
print(s.next(60))
print(s.next(75))
print(s.next(85))




