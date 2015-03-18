from sys import argv

script, cheese_count, boxes_of_crackers = argv

def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket. \n"
	
cheese_and_crackers(int(cheese_count), int(boxes_of_crackers))

#Here is an example of passing values directly as arguments
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

#Here is an example of passing values to the function's arguments
print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#Here is an example of passing a mathematical expression directly to the function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

#Here is an example of passing values to the function via a combination of
#variable and constant
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
