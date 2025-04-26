#file input and output
f=open("file.txt","r")
print(f.read())
f.close()


a=input("enter the name")
f=open("file.txt","a ")
f.write("hello "+a)
f.close()    