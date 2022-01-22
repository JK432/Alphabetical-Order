#Assume that the variables x and y refer to strings. Write a code segment that prints these strings in alphabetical order. You should assume that they are not equal
x=input()
y=input()

car1=x[:1]
car2=y[:1]
if(ord(car1)>ord(car2)):
    print(y)
    print(x)
else:
  print(x)
  print(y)