str1="this is a string"
print(str1)
print(len(str1))
name="usama"
print(name[2])
#slicing
print(name[0:3])
print(name[:3])
print(name[2:])
print(name[-1])
print(name[-3:])
#string functions
print(name.upper())
print(name.lower())
print(name.strip())
print(name.replace("a","b"))
print(name.split("a"))
print(name.find("a"))
print(name.count("a"))
print(name.isalpha())
print(name.isdigit())
print(name.isalnum())
print(name.endswith("a"))
print(name.startswith("a"))
#conditional statement
age=int(input("age : "))
if(age>18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
#conditional statement
age=int(input("age : "))
if(age>18):
    print("you are eligible to vote")
elif(age==18):
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")
