class node:
  def __init__ (self,data):
    self.data=data
    self.addrs=None
class SLL:
  def __init__ (self):
    self.head=None
  def insertatbeg(self):
    val=int(input("enter the value to be inserted"))
    Newnode=node(val)
    Newnode.addrs=self.head
    self.head=Newnode
  def display(self):
    temp=self.head
    while temp!=None:
      print(temp.data)
      temp=temp.addrs
sl1=SLL()
ch=0
while ch!=4:
  print("1.insert at beg  2.delete at beg  3.display  4.search") 
  ch=int(input())
  if ch==1:
    sl1.insertatbeg()
    sl1.display()
  elif ch==3:
    sl1.display()
  else:
    print("invalid choice")         
