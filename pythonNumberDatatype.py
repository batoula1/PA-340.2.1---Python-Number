#1. Declare two integers and assign them values. Then, add the values
a = 10
b = 20

sum = a + b
print("a + b", sum)


#2. Declate two floats. Assign them values and add them
c = 10.5
d = 20.5

sumOfFloats = c + d
print ("c + d", sumOfFloats)

#3. Declares an integer variable and a float variable, assigns numbers to each, and adds them together
e = 4
f = 3.5

sumOfIntAndFloat = e + f
print("e + f", sumOfIntAndFloat)

#4. Declare two integer variables, assigns an integer to each, and divides the larger number by the smaller number
g = 40
h = 20

divOfIntegers = g/h
print("g/h", divOfIntegers)

#5. Declare two float variables, assigns a number to each, and divides the larger by the smaller number
i = 25.3
j = 12.3

divOfFloats = i/j
print("i/j", divOfFloats)


#6. Create three variables that represent products at a cafe
cappuccino = 4.5
espresso = 2
greenTea = 3.5

#7. Create two more variables called subtotal and totalSale, and complete an “order”. Calculate the subtotal and then the totalSale
subtotal = (3*cappuccino) + (4*espresso) + (2*greenTea)
print("Subtotal: ", subtotal)

salesTaxes = 0.08 * subtotal

totalSale = subtotal + salesTaxes

print("Total Sale: ", totalSale)


#Write a Python program that calculates the area of a circle based on the radius = 63
radious = 63
PI = 3.14

area = PI * pow(radious, 2)
print("Are of a circle: ", area)