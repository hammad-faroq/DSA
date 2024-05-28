class Student:
    def __init__(self, rollNo, cgpa):
        self.rollNo = rollNo
        self.cgpa = cgpa

class Student_max_heap:
    def __init__(self,size):
        self.maxsize=size
        self.currsize=0
        self.student_size=[None]*size
        self.c=0
    def swap(self,x,y):
        self.student_size[x],self.student_size[y]=self.student_size[y],self.student_size[x]
    def heapify_up(self,index):
        if index==1:
            return
        parent=self.parent(index)+1
        curr=self.student_size[index]
        curr=curr[0]
        parent_value=self.student_size[parent]
        parent_value=parent_value[0]
        if parent_value<curr:
            self.swap(parent,index)
            self.heapify_up(parent)
    def heapify_down(self,index):
        left=self.left(index)-1
        right=self.right(index)-1
        left_child=self.student_size[left]
        left_child=left_child[0]
        right_child=self.student_size[right]
        right_child=right_child[1]
        if left_child<right_child:
            self.swap(left,right)
        elif right_child<left_child:
            self.swap(right_child,left_child)
    def height(self):
        print(f"Height :{self.c}")
    def remove(self):
        max=self.student_size[1]
        self.student_size.remove(max)
        self.heapify_down(index=1)
        self.c-=1
    def insert(self,student):
        s = (student.cgpa, student.rollNo)
        if self.currsize==0:
            self.student_size[1]=s
            self.currsize+=1
            self.c+=1
        else:
            if self.c>=1:
                i1=self.left(self.c)-1
                i2=self.right(self.c)-1
                if self.student_size[i1] is not None and self.student_size[i2] is not None:
                    self.c+=1
                    self.insert(student)
                    return
                if self.student_size[i1] is None:
                    self.student_size[i1]=s
                    self.heapify_up(i1)
                    self.currsize+=1
                elif self.student_size[i2] is None:
                    self.student_size[i2]=s
                    self.heapify_up(i2)
                    self.currsize+=1
    def level_order_traversal(self):
        for i in self.student_size:
            if i==None:
                continue
            print(f"ROll_no :{i[1]} GPA {i[0]}")
    def isEmpty(self):  # Checks whether the heap is empty or not
        return self.currsize == 0

    def isFull(self):  # Checks whether the heap is full or not
        return self.currsize == self.maxsize
    def parent(self, i):
        return (i - 1) // 2
    def left(self, i):
        return 2 * i + 1
    def right(self, i):
        return 2 * i + 2
s=Student_max_heap(10)
s.insert(Student(26,3.7))
s.insert(Student(27,4.0))
s.insert(Student(1,4.3))
s.insert(Student(2,5))
s.insert(Student(1,6))

s.height()
s.level_order_traversal()
s.remove()
# s.remove()
print()
s.level_order_traversal()
s.height()

# s.print()