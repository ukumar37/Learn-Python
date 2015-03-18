##Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
	pass
	
##Make a class named Dog that is-a Animal and has-a __init__ that takes the parameters
##self and name
class Dog(Animal):

	def __init__(self, name):
		##get the name attribute of self (object) and set it to value name
		self.name = name
		
		##Dog has-a sound
		self.sound = "bark"
		
	def introduce(self):
		print "I am a dog. My name is %s" % self.name + " and I make the sound %s." % self.sound
		
##Make a class named Cat that is-a Animal and has-a __init__ that takes the parameters
##self and name
class Cat(Animal):

	def __init__(self, name):
		self.name = name
		
		##Cat has-a pet sound
		self.sound = "purr"
		
	def introduce(self):
		print "I am a cat. My name is %s" % self.name + " and I make the sound %s." % self.sound
		
##Make a class named Person that has-a __init__ that takes parameters self and name
class Person(object):

	def __init__(self, name):
		##Person has-a a name
		self.name = name
		
		##Person has-a pet of some kind
		self.pet = None
		
##Make a class named Employee that is-a Person and has-a __init__ that takes the 
##parameters self, name, and salary
class Employee(Person):

	def __init__(self, name, salary):
		##?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		##Employee has a salary
		self.salary = salary
		
##create a class called Fish
class Fish(object):
	pass
	
##create a class called Salmon that is-a Fish
class Salmon(Fish):
	pass
	
##create a class called Halibut that is-a fish
class Halibut(Fish):
	pass
	
##rover is-a Dog
rover = Dog("Rover")
rover.introduce()

##Satan is-a Cat
satan = Cat("Satan")
satan.introduce()

##Mary is-a Person
mary = Person("Mary")

##Get the pet attribute of Mary and set it to satan
mary.pet = satan

## frank is-a Employee who has-a name Frank and has-a salary 120000
frank = Employee("Frank", 120000)

##frank has-a pet called rover
frank.pet = rover

##create a flipper that is-a Fish
flipper = Fish()

##create a crouse that is-a Salmon
crouse = Salmon()

#create a harry that is-a Halibut
harry = Halibut()