#boolean
a= True
print(type(a))
b= False
print(type(b))

# bool() function
a=''
print(bool(a))
a={}
print(bool(a))
a='hi'
print(bool(a))

x=1
y=2
print(x==y)


#list items are indexed, ordered, changeable, allow duplicates

#indexed
var=["Geeks", "for", "geeks"]
print(var)
print(var[0], var[1], var[-1])


#ordered
var=[2,3,4, 7,5,9,0]
print(var)

#changeable
var[0]=0
print(var)

#allow duplicates
list1=[1,2,2,3,3,3,3,3,5]
print(list1)

##list in a list
list2=[1,2,[3,4],[5,6],7]

#accesing the items in the list inside another list
print(list2[2][0])


#adding one item at the end of the list using append() method
list2.append(34)
print(list2)

#pop() removes only one element, the last item by default if no value is passed
list2.pop()

#adding multiple items at the end of the list using extend() method
#syntax: list.extend(['item', 'item2', 'item3'])
list2.extend([23, 'hi', 'hello'])

#inserting the new items at a specific position using the insert() method
#syntax: list.insert(index, value)
list2.insert(1,'me')
print(list2)

#pop() removes a specific item if index value is passed
list2.pop(3)

#reversing a list using reverse() method
list2.reverse()
print(list2)



#list comprehension: 1)output expression	2)input sequence	3)a variable	4)an optional predicate part
odd_square=[x**2 for x in range(1,12) if x%2 == 1]
# here x**2 is Output expression, (1,12) is the input sequence, 'x' is the variable and "if x%2 == 1" id the optional predicate
print(odd_square)

#for extracting a phone number from a given string
string="My phone number is 9898175959"
number=[x for x in string if x.isdigit()]
print(number)

num=''
for x in range(len(number)):
	num=num + number[x]
print(num)

#filtering odd numbers using lambda expression
lst=filter(lambda x: x%2 == 1, range(1,12))
print(list(lst))

#list comprehension using ord()
#function for extracting the special characters in a given string
def removeAll(input):
	chars=[char for char in input if ord(char) in range(ord('a'), ord('z')+1,1) or ord(char) in range(ord('A'),ord('Z')+1,1)]
	return ''.join(chars)

if __name__ == "__main__":
	input="dfsdgh$#fs3Ggf$$fasdgGFS#"
	print(removeAll(input))

print()
#swap all elements in a list
list=[1,2,3,4,5,6]
print(len(list))

swaplist=[]
for x in range(len(list)-1):
	swaplist.append(list[x-(len(list)-1)])
print(swaplist)

#enumerate() method
l12=[1,23,45,66]
print(list(enumerate(l12)))


#nested list comprehension
matrix=[]
for i in range(3):
	matrix.append([])

	for j in range(3):
		matrix[i].append(j)
print(matrix)


#nested list comprehension
matrix=[[j for j in range(5)] for i in range(5)]
print(matrix)


#extracting odd numbers from a given list
matrix=[[1,2,3],[4,5,6],[7,8,9]]

odd=[]
for row in matrix:
	for element in row:
		if element%2 != 0:
			odd.append(element)
print(odd)


#another example
odd=[element for row in matrix for element in row if element % 2 != 0]
print(odd)
