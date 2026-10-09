class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Stack():
    def __init__(self):
        self.head=None

    def isempty(self):
        if self.head==None:
            return True
        else:
            return False
        
    def push(self,data):
        if self.head==None:
            self.head=Node(data)
    
        else:
            new_node=Node(data)
            new_node.next=self.head
            self.head=new_node
    
    def topElement(self):
        if self.isempty():
            return "Underflow"
        else:
            return self.head.data
        
    def pop(self):
        if self.isempty():
            return "Underflow"
        else:
            popped_Node=self.head
            self.head=self.head.next
            popped_Node.next=None

            return popped_Node.data
        
stack_obj=Stack()
stack_obj.push(5)
stack_obj.push(2)
stack_obj.push(7)
stack_obj.push(8)
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())
print("the element at the top")
print(stack_obj.topElement())
print("the element popped")
print(stack_obj.pop())