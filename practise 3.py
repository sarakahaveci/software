
file = open("BX-Books.csv","r")

first ={}
how_many ={}

for line in file:
    line = line.split(';')
    isbn = line[0].strip()
    name = line[1].strip()
    first[isbn] = name
    #print isbn,name
    #how_many.setdefault(isbn,0)
    #how_many[isbn] +=1
'''
    first=[]
    number = line.split(',').pop(0)
    name = line.split(',').pop(1)
    a.append(number)
    a.append(name)
    '''

#print first
print first.items()

#for k,v in first.items():
 #   print k