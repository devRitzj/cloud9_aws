myString="This is a string"
print(myString)
print(type(myString))
print(myString + " : is of data type " + str(type(myString)))

fstring = "Water"
SecString = "fall"

thirdString = fstring + SecString
print(thirdString)
name = input("Please Enter your name  : ")
print(name)
color = input ("What is your Favorite Color : ")
animal = input ("Enter your favorite animal : ")
print ("{}, you like a {} {}!". format(name,color,animal))