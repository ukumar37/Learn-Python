import decimal, math
from decimal import *
from sys import argv

#script, user_name = argv
#prompt = '> '

print "Please enter your name?"
user_name = prompt = '> '

print "Hello %s, I am the math machine." % user_name
print "You will give me a radius, and I will spit out the diameter, circumference, and area."

print "So here goes!"
print "What is your radius?"
radius = float(raw_input(prompt))

print "radius %s" % radius

# this function computes the diameter of a circle
def diameter(radius_value):
    print "CALCULATING diameter of a circle with the radius %s" % float(radius_value)
    return float(2. * radius_value)

print "The diameter of the circle is %s" % diameter(radius)

#this one does the same, but for the circumference.
def circumference(radius_value):
    pi = 3.14
    print "FINDING circumference of a circle with the radius %s" % float(radius_value)
    return Decimal(2 * pi * float(radius_value))

print "The circumference of the circle is %s" % float(circumference(radius))

#again, the same, but for area
def area(radius_value):
    pi = 3.14
    print "DOING STUFF to find the area with the radius %s" % float(radius_value)
    return Decimal (pi * math.pow(float(radius_value),2))
 
print "The area of the circle is %s" % float(area(radius))