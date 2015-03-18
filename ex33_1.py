#Define the loop function such that it takes in the length and incrementor 
#variables provided by the user
def loop_function(loop_length, loop_incrementor):
	i = 0
	numbers = []
	#Use a FOR loop
	for i in range(i,loop_length):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + loop_incrementor
		print "Numbers now: ", numbers
		print "At the bottom is is %d" % i
	return numbers

#Prompt the user for length and incrementor values	
length = raw_input("Type the length of the list: ")
incrementor = raw_input("Type the incrementor of the list: ")

#Convert the string values to integer values
int_length = int(length)
int_incrementor = int(incrementor)

#Call the loop function by passing the int variables
#Return the function value into a list
numbers_list = loop_function(int_length, int_incrementor)

#Print the list
print "The numbers: "

for num in numbers_list:
	print num