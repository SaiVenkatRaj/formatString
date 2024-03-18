

string = "This is a string and I have {x:.2f} rupees"

print(string.format(x=5))

a = "This string is in {}"
print(a.format("Python"))

b = "I have {} rupees"
print(b.format(4))

#difference in passing integer, string in to format() method
print("The temperature today is {} degrees celsius outside".format("twenty"))
print("The temperature today is {} degrees celsius outside".format(20))





print("{0:20}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))
print("It is {0:5} degrees outside !".format(40))





#spacing concept, giving 10 spaces for the word 'Raj' and so on...
#here string is left aligned and number is right aligned in given space
print("I am {0:10} and my age is {1:4}!".format('Raj', 24))




introduction = 'My name is {firstName} {lastName} aka {aka}'
fullName = {
    'firstName': 'Raj',
    'lastName': 'Kanchanapally',
    'aka': 'Iron Man'
}

#here ** are used to unpack the dictionary items
print(introduction.format(**fullName))

#using %s for strings
#number after the dot indicate number of letters printed
print("%.3s"%('geeksforgeeks', ))

a='Raj'
b='Kanchanapally'
print("My first name is %.1s and lastname is %.5s"%(a, b))


phone='iphone'
model=15
price=1000

print('There is an %s whose model is %s and the price is $%s'%(phone, model, price))
print('There is an %s whose model is %d and the price is $%d'%(phone, model, price))