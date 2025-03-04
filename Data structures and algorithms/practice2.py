# linked_list = {
#     0:(1,1),
#     1:(2,2),
#     3:(3,-1)
# }
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node

#     def delete(self, key):
#         temp = self.head

#         if temp is not None:
#             if temp.data == key:
#                 self.head = temp.next
#                 temp = None
#                 return

#         while temp is not None:
#             if temp.data == key:
#                 break
#             prev = temp
#             temp = temp.next

#         if temp == None:
#             return

#         prev.next = temp.next
#         temp = None

#     def traverse(self):
#         temp = self.head
#         while temp:
#             print(temp.data, end=" -> ")
#             temp = temp.next
#         print("None")

# linked_list = LinkedList()
# linked_list.insert(1)
# linked_list.insert(2)
# linked_list.insert(3)
# linked_list.traverse()

# linked_list.delete(2)
# linked_list.traverse()


# Linear search

# def search_element(arr,x):
#     for i in range (len(arr)):
#         if arr[i] == x:
#             return i
#         return -1
# arr=[2,23,7,8]
# x= 44
# result= search_element(arr,x)
# if  result != -1:
#     print("Element found at index,{result}")
# else:
#     print("Element not found")





#binary search
# def binary_search(arr,x):
#     l = 0
#     r= len(arr) -1
    
#     while (l<=r):
#         mid= (l+r)//2
#         if arr[mid] ==x:
#             return mid
#         elif arr[mid] <x:
#             l = mid + 1
#         else :
#             r = mid -1 
# arr= [2, 3, 4, 10, 40]
# x= 10
# result = binary_search(arr,x)
# if result == -1:
#     print("Element not found at index ")
# else:
#     print("Element at found index" ,result)



### Insertion sort


###fibonnaci
# def fibonnaci(n):
#    if n ==0:
#     return 0
#    elif n == 1:
#     return 1
   
#    else:
#     return fibonnaci(n-1) + fibonnaci(n-2)
# print(fibonnaci(4))



def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n-1)
print(factorial(4))
    
