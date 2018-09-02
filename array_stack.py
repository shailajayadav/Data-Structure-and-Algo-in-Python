class EmptyStackError(Exception):
    pass
class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return self.items==[]

    def size(self):
        return len(self.items)

    def push(self,item):
        return self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise EmptyStackError("Stack is empty")
        return self.items[-1]

    def display(self):
        print(self.items)

st=Stack()
"""
while True:
    print("1.Push")
    print("2.Pop")
    print("3.Peek")
    print("4.Size")
    print("5.Display")
    print("6.Quit")

    choice=int(input("enter the choice:"))

    if choice==1:
        x=int(input("Enter elements to push : "))
        st.push(x)
    elif choice==2:
        st.pop()
    elif choice==3:
        print(st.peek())
    elif choice==4:
        print(st.size())
    elif choice==5:
        st.display()
    elif choice==6:
        break
    else:
        print("wrong choice")
        
    
"""          
        
    
