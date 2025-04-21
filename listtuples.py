#list is mutable
marks=12
marks=13
marks=14
marks=15
marks=16

marks=[12,13,14,15,16]
print(marks)
average_marks = sum(marks) / len(marks)
print(average_marks)
print(type(marks))
print(marks[0])
print(marks[-1])
marks[0]=100
print(marks)
#slicing
print(marks[1:3])  # Slicing to get the second and third marks
print(marks[:3])  # Slicing to get the first three marks
print(marks[2:])  # Slicing to get the marks from the third mark to the end
print(marks[-1])  # Slicing to get the last mark
#list,append,insert,remove,pop,sort,reverse
list.append(marks,17)
print(marks)
list.insert(marks,2,18)
print(marks)
list.remove(marks,18)
print(marks)
list.pop(marks,2)
print(marks)
marks.sort() #possible in string
print(marks)
marks.reverse()
print(marks)
#additional operations
marks.extend([19,20])
print(marks)
marks.clear()  # Clears all elements from the list
print(marks)
#tuple same work on list but tuple is immutable(change nai hota hai)
mark=(12,13,14,15,16)
print(mark)
average_marks = sum(mark) / len(mark)
print(average_marks)
print(type(mark))
print(mark[0])
print(mark[-1])
#index counting
print(mark.index(12))
print(mark.count(12))

#practice
a=input("enter the name")
b=input("enter the name")
c=input("enter the name")
st=[a,b,c]
print(st)

#palindrome
l1=[1,2,3,4,5]
copy_l1=l1.copy()
copy_l1.reverse()
if (copy_l1 == l1):
    print("palindrome")
else:
    print("not a palindrome")

