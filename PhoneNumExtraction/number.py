file=input('Enter the text file name to read: ')
file2=input("Enter a file name you want to save with extracted numbers wfith '.txt' at the end: ")

fileVar=open(file,'r')
fileEdit=open(file2,'w')

for line in fileVar:
    stringInLine=''
    for string in line:
        if string.isdigit() is True:
            stringInLine+=string
    print(stringInLine)
    fileEdit.write(stringInLine+'\n')

fileVar.close()
fileEdit.close()
