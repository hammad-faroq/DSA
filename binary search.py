class Binary_search:
    def __init__(self,array,number):
        self.array=array
        self.number = number
        if self.is_Sorted():
            self.b_s()
        else:
            print("Binary search is only for the sorted list!")
    def is_Sorted(self):
        for i in range(len(self.array)-1):
            if self.array[i] <self.array[i+1]:
                is_sorted1=True
            else:
                is_sorted1=False
        return is_sorted1
    def b_s(self):
        mid=len(self.array)//2
        mid1=len(self.array)//2
        while mid<=len(self.array) and mid>=0:
            mid_number = self.array[mid - 1]
            if self.number>mid_number:
                mid1=mid1//2
                mid=mid+mid1+1
            elif self.number <mid_number:
                mid1=mid1//2
                mid=mid-mid1-1
            elif self.number==mid_number:
                print(self.number)
                return
        print("No number exist",self.number)
    def comparison(self,other):
        for i in other:
            Binary_search(array=self.array,number=i)
b=Binary_search([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31],0)
b.comparison([1,5,8,10,0,-1])















# target=30
# # print(i for i in range(100))
# # print((9//2))
# # class Binary_search:
# #     def __init__(self,array):
# #         self.array=array
# def binary_search(arr, target):
#     left, right = 0, len(arr) - 1
#
#     while left <= right:
#         mid = (left + right) // 2
#
#         # Check if target is present at mid
#         if arr[mid] == target:
#             return mid
#
#         # If target is greater, ignore left half
#         elif arr[mid] < target:
#             left = mid+1
#
#         # If target is smaller, ignore right half
#         else:
#             right = mid-1
#
#     # If the element is not present in the list
#     return -1
#
#
# # Example usage
# # arr = [2, 3, 4, 10, 40]
# # target = 10
# # result = binary_search(arr, target)
#
# # if result != -1:
# #     print("Element is present at index", result)
# # else:
#     print("Element is not present in the array")


