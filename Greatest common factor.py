def gcd(a,b):
    """This works on the Euclidean algorithm not the simple prime factirization method"""
    if b==0:
        return a
    return gcd(a=b,b=a%b)
# print(gcd(10,15))
def sum_of_digits(n):
    """Recurion of the sum of digits of a positive integer"""
    if n==1:
        return n
    return n%10+sum_of_digits(n//10)
# print(sum_of_digits(1122))
def fib(n):
    """This is the rrecursive functiton to find the fibonacci number at the nth position in the fib sequence"""
    if n in [0,1]:##This is the termination condition
        return n
    return fib(n-1)+fib(n-2)##This is the recursive case
# print(fib(8))
def binary_search12(array,tar):
    """THis is the iterable of the binary search"""
    mid=(len(array)-1)//2
    mid1=(len(array)-1)//2
    i=0
    while mid<=len(array) and mid>=0:
        midn=array[mid-1]
        i+=1
        if tar==midn:
            print(i)
            return tar
        elif tar>midn:
            mid1=mid1//2
            mid=(mid+mid1)+1
        elif tar<midn:
            mid1 = mid1 // 2
            mid=(mid-mid1)-1

def binary_search(array,target):
    """This is the recursive function of the binary search"""
    mid=(len(array)-1) // 2
    mid_number=array[mid-1]
    if target==mid_number:
        return target
    elif target>mid_number:
        return binary_search(array=array[mid:],target=target)
    elif target<mid_number:
        return binary_search(array=array[:mid],target=target)
def binary_search01(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

print(binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51],51))

