def f(i, values = []):
    """This is because list is a global variable"""
    values.append(i)
    print (values)
    return values
f(1)
f(2)
f(3)
"""slicing cann aslo be done in this method in the inverse order :)"""
a=[1,2,3,4,5]
print(a[3:0:-1])
arr = [1, 2, 3, 4, 5, 6]
for i in range(1, 6):
    arr[i - 1] = arr[i]
for i in range(0, 6):
    print(arr[i], end = " ")

fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
"""This is called alaising when two objects in the memory refers to the same location and any change in one of them brings the change into the next one"""
fruit_list3 = fruit_list1[:]

fruit_list2[0] = 'Guava'
print(fruit_list1)
fruit_list3[1] = 'Kiwi'

sum = 0
for ls in (fruit_list1, fruit_list2, fruit_list3):
    if ls[0] == 'Guava':
        sum += 1
    if ls[1] == 'Kiwi':
        sum += 20

print(sum)