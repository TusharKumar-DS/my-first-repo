'''
#What more we can learn with jusyt Hello
#print - a function to print whats inside (" ")
print("hello, world")'''
#Input - whom to say hello
name = input("what is your name :")
name = name.strip().title()
print("hello",name)
#more ways to print this same result
print("hello ,"+name)
#comma , this seperates arguments we can also use this as
print("hello,",name)
#Strip - to remove extra space from left and right 
#capitalize - to capial JUST 1st letter
#title - to capitalize all 1st letter
#note : its position is important too else useless
#name = name.strip().capitalize().title()
##here we put f coz name is in bracket so f will tell it its special string else
print("hello,(name)")
print(f"hello,{name}")
print(f"hello,"(name)) #will give error se we need other brackets
