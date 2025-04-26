#functions

def add(a,b):
    c=a+b
    print(c)

add(2,3)

def avg(a,b,c):
    d=(a+b+c)/3
    print(d)

avg(2,3,4)


list={1,2,3,4,5}

def length(list):
    print(len(list))

length(list)

def fact(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    print(f)

fact(5)

def oddeven(n):
    if(n%2==0):
        print("even")
    else:
        print("odd")

oddeven(4)

#Recursion

def fact(n):
    if(n==1):
        return 1
    else:
        return n*fact(n-1)

print(fact(5))                  