'''DAY 2 - variables & data types'''
'''
#arithmetic operations starts here
x = 1
y = 2
z = x+y
print(z)#also we can do print(x+y) so we save 1 variable
# +(add) -(sub) *(mul) /(div) %(remainder) **(exponent) //(integer division)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)

#lets take input from user to operate
x = int(input("value of x: "))
y = int(input("value of y: "))
print(x + y)#can change and try all others
#well we use int earlier or else we mess us coz by default these all are string
#example
x = input("value of x: ")
y = input("value of y: ")
print(x+y)#well well as it cant decide on is own it gave both int and str o/p
#float , double , int , str etc etc are some data types
#round - to round off a number
print(round(3.5678)) # came to be 4
x = float(input("What's x? "))
y = float(input("What's y? "))

z = x / y

print(f"{z:.2f}")#help us to decide upto how much decimal place we need that
print(f"{z:.4f}")
'''

#FUNCTIONS
#so print is a function like print know when we say print it prints or return whats inside that
#we can make our custome one too
#USE def when need to define our custome function
'''def hello(to):#to is for parameters 
    print("hello,", to)
name = input("What's your name? ")
hello(name)'''

def hello(to="world"):
    print("hello,", to)
hello()
#combined
def hello(to="world"):
    print(f"hello, {to}")
name = input("What's your name? ").strip().title()
hello(name)