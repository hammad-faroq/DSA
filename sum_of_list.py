def sum_of_list(array):
    """This is the recursive function to find the sum of elements in a list"""
    l=len(array)
    if l==1:##Always consider that in recursion,Recursive sace and Termination condition is very important
        return array[l-1]
    return array[-l]+sum_of_list(array=array[(-l)+1:])
print(sum_of_list([1, 2, 3, 4, 5,15,00,0,-1]))
def s(my_list):
    """THis is the iterave way of summing all the elements in the list :)"""
    sum=0
    while True:
        l=len(my_list)
        print(l)
        if l == 1:
            l1=my_list[0]
            sum+=l1
            print(sum)
            break
        sum+=my_list[-l]
        my_list=my_list[(-l)+1:]
# s(my_list=[1,2,3,4,5,15])