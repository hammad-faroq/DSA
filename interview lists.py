def sum_of_numbers(list1,sum):
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
            if list1[i]+list1[j]==sum:
                print(list1[i],list1[j])
# sum_of_numbers([3,2,3,4,5,6,3,9,6,5,7,4,],11)
def fun(a, n):
    if (n == 1):
        return a[0]
    else:
        x = fun(a, n - 1)
    if (x > a[n - 1]):
        return x
    else:
        return a[n - 1]
# Driver code
arr = [12, 10, 30, 50, 100]
# print(fun(arr, 5))
def fun(i):
    if (i % 2 == 1):
        i += 1
        return (i - 1)
    else:
        return fun(fun(i - 1))
# print(fun(200))
def test(i,j):
    if(i==0):
        return j
    else:
        return test(i-1,i+j)
# print(test(4,7))
def fun(n):
    if (n > 0):
        fun(n - 1)
        print(n, end=" ")
        fun(n - 1)
# driver code
fun(3)