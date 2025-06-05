def sample_fuc():
    a=5
    print("This is a sample function..")
    return a
b=sample_fuc()
print(b)


#parameters
def sample_fun(name):
    print("My name is" ,name)
sample_fun("Victor")
    
#introduction
def intro(name):
    print("Hello, good morning! I am",name)
user=input("Enter your name: ")
intro(user)

#factorial
def recur_fact(n):
    if n==1:
        return n
    else:
        return n*recur_fact(n-1)
num1=int(input("Enter a number"))

if num1< 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num1==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of",num1, "is",recur_fact(num1))
    