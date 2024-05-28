class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self, key, value):
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(self.root, key, value)
    def _insert(self, current_node, key, value):
        if key < current_node.key:
            if current_node.left is None:
                current_node.left = Node(key, value)
            else:
                self._insert(current_node.left, key, value)
        elif key > current_node.key:
            if current_node.right is None:
                current_node.right = Node(key, value)
            else:
                self._insert(current_node.right, key, value)
        else:
            # If the key already exists, update the value
            current_node.value = value
    def find(self, key):
        return self._find(self.root, key)
    def _find(self, current_node, key):
        if current_node is None:
            return None
        if key < current_node.key:
            return self._find(current_node.left, key)
        elif key > current_node.key:
            return self._find(current_node.right, key)
        elif key==current_node.key:
            if current_node.value=="Data.txt":
                with open(file="Data.txt",mode="r") as file5:
                    d=file5.readlines()
                    for i in d:
                        d1=i.split(":")
                        if d1[0].lower()==key.lower():#THIs will print the output from the memory
                            return f"Output: {d1[1]}\nURLs Read From File"
            else:
                return f"Output: {current_node.value}\nURLs Read From Memory"
    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements
    def _inorder_traversal(self, current_node, elements):
        if current_node:
            self._inorder_traversal(current_node.left, elements)
            elements.append((current_node.key, current_node.value))
            self._inorder_traversal(current_node.right, elements)
def result_urls():
    with open(file="result.txt",mode="r") as file1:
        d=file1.readlines()
    return d
def URLs_to_dict(res_URLs):
    url_dict = {}
    for entry in res_URLs:
        key, url = entry.split(":", 1)
        url_dict[key.lower()] = url
    return url_dict
def calculate_word_frequency(arr):
    words = []
    for string in arr:
        words.extend(string.lower().split())
    words.sort()
    frequency = {}
    current_word = None
    count = 0
    for word in words:
        if word == current_word:
            count += 1
        else:
            if current_word is not None:
                frequency[current_word] = count
            current_word = word
            count = 1
     # Don't forget to add the last word count
    if current_word is not None:
        frequency[current_word] = count
    return frequency
def history_data():
    with open(file="hist.txt", mode="r") as file:
        d = file.readlines()
    return d
def main():
    hist_data=history_data()
    frequency = calculate_word_frequency(hist_data)
    sorted_dict = dict(sorted(frequency.items(), key=lambda item: item[1], reverse=True))
    print(sorted_dict)
    res_URLs=result_urls()
    url_dict=URLs_to_dict(res_URLs)
    count = 0
    with open("Data.txt", "w+") as file4:
        for key in sorted_dict.keys():
            count += 1
            if count <= 20:
                if key.lower() in url_dict:#O(1) time complexity because searching a key in dict is o(1) bec of hash table
                    sorted_dict[key] = url_dict[key.lower()]
            else:
                if key.lower() in url_dict:
                    data = f"{key}:{url_dict[key.lower()]}"
                    file4.write(data)
                    sorted_dict[key] = "Data.txt"
    print(sorted_dict)
    bS=BST()
    for i in sorted_dict:
        bS.insert(i,sorted_dict[i])
    is_on=True
    while is_on:
        user=input("Please Enter the search query:").lower()
        print(bS.find(key=user))
        if user=="no":
            is_on=False
main()









# Step 2: Sort the dictionary by values
# sorted_items = sorted(data.items(), key=lambda item: item[1])
#
# sorted_items is a list of tuples sorted by the second element (the values)
# print("Sorted items by value:", sorted_items)

# Step 3 (Optional): Create a sorted dictionary
# sorted_dict = {k: v for k, v in sorted_items}
# print("Sorted dictionary by value:", sorted_dict)
# # print(d1)
# for j in d:
#     print(j)
#     for i in d1:
#         print(i.split(":"))

# with open(file="Data.txt",mode="w+") as file4:
#     for i in sorted_dict:
#         count+=1
#         if count<=5:#add the urls to the dictionary untill the top 10000
#             for j in d1:
#                 curr=j.split(":")
#                 if i.lower()==curr[0].lower():
#                     sorted_dict[i]=curr[1]#Curr 1  is the url of that key that matches in the search_result.txt
#         else:#If the no of records arre greater than 10000 it gonna simmply copy the url of that keyword into a new file and update the alue of tthat key
#             #in the dictionary with that file name
#             for j in d1:
#                 curr=j.split(":")
#                 if i.lower()==curr[0].lower():
#                     data=str(i)+str(curr[1])
#                     file4.write(data)
#                     sorted_dict[i]="Data.txt"