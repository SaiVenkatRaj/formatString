#using str.center() format function
print(" My name is Raj ".center(100,'$'))

#using str.ljust() format function
print(" My name is Raj ".ljust(50,'l'))

#using str.rjust() format function
print(" My name is Raj ".rjust(50,'r'))


#issue is the print() is returning none at the output after the below statement is executed <<<<<<<<<<<<<<<<<<<<<<<
name = input("Enter your name: ")

b=input("Enter any number: ")
print(b,'',type(b))


#type casting
x=int(input("Enter any number: "))
print(x,'',type(x))

y=float(input("enter a number: "))
print(y,'',type(y))