#method overloading in python
class myClass:
  def sum(self,a=None,b=None,c=None):
    if a!=None and  b!=None and c!=None:
      s = a+b+c
    elif a!=None and b!=None:
      s = a*b
    else:
      s = "give at least two number"
    return s

obj = myClass()
print(obj.sum(10,20,30))
print(obj.sum(20,20))
print(obj.sum())