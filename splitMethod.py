#use of split() method
#syntax:- input().split(seperator, max value)

x, y = input("Enter 2 numbers: ").split()
print("First number is: ", x)
print("Second number is: ", y)


a, b, c=input("Enter 3 values: ").split()
print("The 3 values you entered are {}, {} and {}".format(a, b, c))


#using list comprehension and split method
c, d, e, f=[int(x) for x in input("Enter 4 numbers: ").split()]
print("You have entered {}, {}, {} and {}".format(c, d, e, f))

g=[int(x) for x in input("Enter multiple values: ").split()]
print("List is: ", g)