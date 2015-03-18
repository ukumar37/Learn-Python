my_name = 'Uday Kumar'
my_age = 44 # that is the truth
my_height = 70 # inches
my_weight = 165 # lbs
my_eyes = 'brown'
my_teeth = 'white'
my_hair = "black"

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the tea." % my_teeth

#this line is tricky, try to get it right
print "If I add %d, %d, and %d, I get %d." % (
		my_age, my_height, my_weight, my_age + my_height + my_weight)
		
print "My height in feet is %d feet." %(my_height / 12.0)