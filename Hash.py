class Hash_table:
    def __init__(self,size):
        self.table=[None]*size
        self.size=size
    def get_hash_value(self,name):
        temp = 0
        for char in name:
            temp += ord(char)
        return temp%self.size
    def insert(self,name):
        h=self.get_hash_value(name)
        curr=self.table[h]
        if curr is not None:
            while curr is not None:
                print(h,"current index")
                h+=1
                if h>=len(self.table):
                    break
                curr=self.table[h]
            if h>=len(self.table):
                print("cant be inserted")
                return False
            else:
                print(h, "current index")
                self.table[h]=name
                return  True
        else:
            print(h, "current index")
            self.table[h]=name
            return True
    def search(self,name):
        h = self.get_hash_value(name)
        curr = self.table[h]
        if curr!=name:
            while curr !=name:
                print(h,"index")
                h+=1
                if h>=len(self.table):
                    break
                curr=self.table[h]
            if h>=len(self.table):
                print("cant found!")
                return False
            else:
                print(h, "index")
                print(self.table[h])
                return True
        else:
            print(h, "index",end=' ')
            print(self.table[h])
            return True
    def remove(self,name):
        h = self.get_hash_value(name)
        curr = self.table[h]
        if curr != name:
            while curr != name:
                h += 1
                if h >= len(self.table):
                    break
                curr = self.table[h]
            if h >= len(self.table):
                print("Can't be Removed")
                return
            else:
                self.table[h]=None
        else:
            self.table[h]=None



    def show(self):
        for i1 in range(len(self.table)):
            if self.table[i1]==None:
                print("EMpty")
            else:
                print(i1)
                print(self.table[i1])
    def load_factor(self):
        n=0
        for i in range(len(self.table)):
            if self.table[i]==None:
                continue
            else:
                n+=1
        print(n/self.size)
def main():
    s=int(input("ENter the size of the hash Table"))
    h=Hash_table(s)
    c=int(input("1. Insert a name\n"
            "2. Search for a name\n"
            "3. Remove a name\n"
            "4. Display the Hash Table\n"
            "5. Display Load Factor of the table\n"
            "6. Exit\nEnter your choice:"))
    is_on=True
    while is_on:
        if c==1:
            n=input("ENter the name")
            h.insert(n)
        elif c==3:
            n = input("ENter the name")
            h.remove(n)
        elif c==2:
            n = input("ENter the name")
            h.search(n)
        elif c==4:
            h.show()
        elif c==6:
            h.load_factor()
        else:
            is_on=False
        c = int(input("1,2,3,4,5,6"))
main()
def hash_function(fruit):
    s=0
    for i in fruit:
        s+=ord(i)&0XFFFFFFFFFF
    h=(31+s)&0XFF
    return h
def hash2(fruit):
    s=0
    for i in range(len(fruit)):
        s+=(ord(fruit[i]))
    mid=len(fruit)//2
    s//=mid
    return s
def hash(fruit):
    s=0
    cons=31
    for i in range(3):
        s+=cons+(ord(fruit[i]))
        cons+=s*i
    return s
def main():
    s=["Apples","Apricots","Avocados","Bananas","Bing Cherry","Blueberries","Boysenberries"
        ,"Cantaloupe","Cherries","Clementine","Crab apples","Cucumbers","Damson plum","Dates"
        ,"Dewberries","Dinosaur Eggs","Dragon Fruit","Eggfruit","Elderberry","Entawak",
       "Evergreen Huckleberry","Farkleberry","Fig","Finger Lime","Gooseberries","Grapefruit"
        ,"Guava","Hackberry","Honeycrisp Apples","Imbe","Indonesian Lime","Jackfruit","Jambolan"
        ,"Java Apple","Kaffir Lime","Kiwi","Kumquat","Lime (Lemon)","Longan","Loquat",
       "Lychee","Mango","Melon","Mulberry","Nashi Pear","Navel Orange","Nectarine",
       "Ogeechee Limes","Olive","Oranges","Oval Kumquat","Papaya","Paw Paw","Peach",
       "Pineapple","Pomegranate","Prickly Pear","Quararibea cordata",
       "Queen Anne Cherry","Quince","Rambutan","Raspberries","Star Fruit","Strawberries"
        ,"Sugar Baby Watermelon","Tamarind","Tangerine","Tart Cherries","Tomato","Ugni","Uniq Fruit",
       "Vanilla Bean","Velvet Pink Banana","Voavanga","Watermelon","White Mulberry","Wolfberry",
       "Xango Mangosteen","Xigua","Ximenia caffra fruit","Yangmei","Yellow Passion Fruit",
       "Yunnan Hackberry","Zig Zag Vine fruit","Zinfandel Grapes","Zucchini"]
    table=[None]*(10*len(s))
    l=[]
    for  i in s:
        h=hash_function(i)
        # h=hash2(i)
        # h=hash(i)
        l.append(h)
    for i in range(len(l)):
        for j in range(i,len(l)):
            # print(l[j])
            if l[i]==l[j]:
                print(l[i],l[j])
                print("collision")
main()
import random
def hash_func(x,size):
    return x%size
def collision(table,h,x):
    curr = table[h]
    if curr is not None:
        return False
    else:
        table[h]=x
def calc_size(table):
    s=0
    for i in range(len(table)):
        if table[i]==None:
            continue
        else:
            s+=1
    return s
def mian():
    m_list=[]
    s=int(input("ENter the size of the table:"))
    for i1 in range(50):
        table=[None]*s
        while True:
            r=random.randint(1,100)
            h=hash_func(x=r,size=s)
            c=collision(table=table, h=h, x=r)
            if c==False:
                calc=calc_size(table=table)
                print(calc)
                m_list.append(calc)
                break
    m=0
    for i in range(len(m_list)):
        m+=m_list[i]
    print(m/len(m_list))

mian()