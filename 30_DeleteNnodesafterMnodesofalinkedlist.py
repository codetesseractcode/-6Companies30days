# your task is to complete this Function
# Function shouldn't return anything

'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def linkdelete(self, head, n, m):
        temp = head
        while temp:
            for i in range(m-1):
                if temp is None:
                    return head
                temp=temp.next
            if temp is None or temp.next is None:
                return head
            dele=temp.next
            for i in range(n):
                if dele is None:
                    break
                dele=dele.next
            temp.next=dele
            temp =dele
                
        return head
                
