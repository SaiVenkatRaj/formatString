
def unorganized(a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)
 

def organized(a, b):
    for i in range(a, b):
 
        # Using formatters to give 6
        # spaces to each set of values
        print("{:6d} {:6d} {:6d} {:6d}"
              .format(i, i ** 2, i ** 3, i ** 4))
 

n1 = int(input("Enter lower range :-\n"))
n2 = int(input("Enter upper range :-\n"))
 
print("------Before Using Formatters-------")
 
# Calling function without formatters
unorganized(n1, n2)
 
print()
print("-------After Using Formatters---------")
print()
 
# Calling function that contains
# formatters to organize the data
organized(n1, n2)