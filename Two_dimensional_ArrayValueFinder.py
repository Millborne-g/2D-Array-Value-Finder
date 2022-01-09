#Millborne A. Galamiton BS-CPE-2B
R = int(input("Enter rows:"))#ask the user on how many rows
C = int(input("Enter columns:")) #ask the user on how many columns

el = []#intialize an empty array
ij = []#intialize an empty array, store ij ordered elements so that it would be easy to find
ji = []#intialize an empty array, store ji ordered elements so that it would be easy to find

for i in range(R):#The loop will terminate depending on how many rows
    a=[]#initialize an empty array
    for y in range(C):#ask the user the column, depending how many columns does the user wants
        print("Index[",i,"] [",y,"]:",end=" ")
        a.append(int(input()))
    el.append(a)
print(el)#Display the array 
print()
print("ij-ordering(row-major)")
for i in range(R):#Display the array in ij order
    for y in range(C):
        print("Index[",i,"] [",y,"]:",el[i][y])
        ij.append(el[i][y])
print()
print("ji-ordering(column-major)")
for i in range(C):#Display the array in ji order
    for y in range(R):
        print("Index[",y,"] [",i,"]:",el[y][i])
        ji.append(el[y][i])
print()
print("Enter the index: ")
l1 = int(input(">")) #ask the user an integer to locate the elemen
l2 = int(input(">"))#ask the user an integer to locate the element

for i in range(len(ij)):
    if el[l1][l2] == ij[i]:#check if there is match
        print("ij-ordering(row-major) Element found:","Index[",l1,"][",l2,"]:",el[l1][l2],"is on the",i+1,"position")#display the located position of the element
       
    if el[l1][l2] == ji[i]:#check if there is match
        print("ji-ordering(column-major)Element found:","Index[",l1,"][",l2,"]:",el[l1][l2],"is on the",i+1,"position")#display the located position of the element
       
           