class Node:
    def __init__(self,data):
        self.data= data
        self.next = None

node1 = Node(5)
node2 = Node(10)
node3 = Node(15)

#Connecting the Nodes
node1.next=node2
node2.next=node3

head = node1

#Traversing the Linked List
def Traverse(head):
  curr = head
  while curr is not None:
      print(curr.data)
      curr = curr.next

#Inserting at first position
newNode = Node(1)
newNode.next = node1
head = newNode

#Inserting at last position
newNode = Node(25)
curr = head
while curr.next != None:
    curr=curr.next

curr.next = newNode

#Inserting at Kth position
newNode = Node(20)
k=4
curr = head
for i in range(k-1):
    curr=curr.next

newNode.next=curr.next
curr.next = newNode 

#Deleting first Node
k=0
if k==0:
    head = head.next

#Deleting kth Node
k=2
curr = head

for i in range(k-2):
    curr = curr.next

curr.next=curr.next.next

Traverse(head)

