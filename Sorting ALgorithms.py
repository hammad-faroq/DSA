def bubble_sort(list):
    """THIs is a simple algorith for bubble sort"""
    for i in range(len(list)-1):#Once second loop is done and swapping is completed this loop will make sure that the swapping will be done one less time in the next iteration
        for j in range(len(list)-1-i):#THis loop will swap the items in the list
            if list[j]>list[j+1]:
                list[j],list[j+1]=list[j+1],list[j]
    print(list)
# bubble_sort([9,8,7,6,4,5,3,2,1])
def selection_sort(list):
    """This simply finds the min_indexx from the list and just swap the first index value with the min_index_value and continues till the end """
    for i in range(len(list)):
        min_index=i#We always take first element or first index as min_index
        for j in range(i+1,len(list)):
            if list[min_index]>list[j]:
                min_index=j
        list[i],list[min_index]=list[min_index],list[i]
    print(list)
# selection_sort([5,4,3,6,7,8,1,9,0])
def insertion_sort(list):
    """IDK how this algorithm is working!"""
    for i in range(1,len(list)):
        curr=list[i]
        j=i-1
        while j>=0 and curr<list[j]:
            list[j+1]=list[j]
            j-=1
        list[j+1]=curr
    print(list)
# insertion_sort([2,1,7,6,5,8,0])
def merge_sort(list):
    if len(list)>1:
        left_array=list[:len(list)//2]
        right_array=list[len(list)//2:]
        #Recursion
        merge_sort(left_array)
        merge_sort(right_array)
        #Merge
        i=0#Left idx
        j=0#Right idx
        k=0#Mergerd array idx
        while i<len(left_array) and j<len(right_array):
            if left_array[i]<right_array[j]:
                list[k]=left_array[i]
                i+=1
            else:
                list[k]=right_array[j]
                j+=1
            k+=1
        while i<len(left_array):#These are the two boundry checks if only one array get inserted at the kth index and other remains as it is
            list[k] = left_array[i]
            i += 1
            k+=1
        while j<len(right_array):
            list[k] = right_array[j]
            j += 1
            k+=1
# lis=[2,1,8,6,3,0,9,5,-1]
# merge_sort(lis)
# print(lis)
def insartion_sort(list):
    """Just a simple algorithm which works by taking first element as sorted element and takes the second element from the list and compares from the previous
    if samller then do back swapping else move to the next index in the list"""
    for i in range(1,len(list)):
        j=i
        while j>0 and list[j-1]>list[j]:
            list[j-1],list[j]=list[j],list[j-1]#Back swapping
            j-=1
    print(lis)
lis=[2,1,8,6,3,0,9,5,-1]
insartion_sort(lis)
print(lis)
# def mer(list):
#     left_array = list[:len(list) // 2]
#     right_array = list[len(list) // 2:]
#     # Merge
#     i = 0  # Left idx
#     j = 0  # Right idx
#     k = 0  # Mergerd array idx
#     print(left_array)
#     print(right_array)
#     while i < len(left_array) and j < len(right_array):
#         if left_array[i] < right_array[j]:
#             list[k] = left_array[i]
#             i += 1
#             print("yes")
#         else:
#             print("yy")
#             list[k] = right_array[j]
#             j += 1
#         k += 1
#     while i < len(
#             left_array):  # These are the two boundry checks if only one array get inserted at the kth index and other remains as it is
#         list[k] = left_array[i]
#         i += 1
#         k += 1
#     while j < len(right_array):
#         list[k] = right_array[j]
#         j += 1
#         k += 1
# lis1=[3,2,1,5,6,7,8,0]
# mer(lis1)
# print(lis1)