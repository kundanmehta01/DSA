st = []
st.append(8)
st.append(7)
st.append(5)
st.append(2)

print(st) #Print Stack
print (st [-1]) #see top element

st.pop() #Remove first(top) element
print(st)

class Stack:
    def __init__(self):
        self.st = []

    def push(self,x):
        self.st.append(x)

    def pop(self,x):
        self.st.pop(x)

    