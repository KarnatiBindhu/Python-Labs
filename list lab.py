#Write a python program to sum all the items in the list.

list=[10,11,12,13]
sum=0
for n in list:
    sum+=n
print(sum)

#Write a python program to get the largest and smallest number from a list without builtin functions.

list=[100,200,300]
largest=smallest=list[0]
for num in list[1:]:
    if num>largest:
        largest=num
    if num<smallest:
        smallest=num
print("Largest:",largest)
print("Smallest:",smallest)

#Write a python program to find the duplicate values from a list and display those. 

list=[1,2,3,4,5,5,7,8,7]
unique=[]
duplicate=[]
for n in list:
    if n in unique and n not in duplicate:
        duplicate.append(n)
    else:
        unique.append(n)
print(duplicate)

#write a python program to split a given list into two parts where the length of the first part of the list is given.
#original list [1,1,2,3,4,4,5,1]
#length of the first part of the list:3
#splitted the said list into two parts
#([1,1,2),(3,4,4,5,1])


list=[1,1,2,3,4,4,5,1]
split=3
n1=list[:split]
n2=list[split:]
print("n11:",n1)
print("n12:",n2)

#write a python program to traverse a given list in reverse order,and print the output.

list=[1,2,3,4,5]
for n in reversed(list):
    print(n)
