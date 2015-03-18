from sys import exit

#Function to pick favorite subjects
def favorite_subjects():
	print """Pick 2 favorite subject areas from the following list: \n1. Math 	\n2. Science \n3. Arts & History \n(List subjects in order of preference)"""
	subject_1 = raw_input("Subject Area 1 >> ")
	subject_2 = raw_input("Subject Area 2 >> ")
	return subject_1, subject_2

#Function to pick favorite skills	
def favorite_skills():
	print """Pick 2 favorite skill areas from the following list: \n1. Build \n2. Repair \n3. Improve \n(List skills in order of preference)"""
	skill_1 = raw_input("Skill Area 1 >> ")
	skill_2 = raw_input("Skill Area 2 >> ")
	return skill_1, skill_2
	
#Function to process favorite subjects	
def process_subjects(area_1, area_2):
	if "math" in area_1.lower() and "science" in area_2.lower():
		return "Computer Science", "Data Science"
	elif "science" in area_1.lower() and "math" in area_2.lower():
		return "BioTech Engg", "BioMed Engg"
	elif "science" in area_1.lower() and "arts" in area_2.lower():
		return "Medicine", "Pharmacy"
	elif "arts" in area_1.lower() and "science" in area_2.lower():
		return "Physical Therapy", "Literature"
	elif "math" in area_1.lower() and "arts" in area_2.lower():
		return "Teaching", "Architecture"
	elif "arts" in area_1.lower() and "math" in area_2.lower():
		return "Music", "Graphic Design"
	else:
		dead("Learn to type else you will end up a dead beat.")
	
#Function to process favorite skills	
def process_skills(area_1, area_2):
	if "build" in area_1.lower() and "repair" in area_2.lower():
		return "Construction Work", "Technician"
	elif "repair" in area_1.lower() and "build" in area_2.lower():
		return "Handyman", "Inspector"
	elif "repair" in area_1.lower() and "improve" in area_2.lower():
		return "Plumber", "Electrician"
	elif "improve" in area_1.lower() and "repair" in area_2.lower():
		return "Home Improvements", "Painter"
	elif "build" in area_1.lower() and "improve" in area_2.lower():
		return "Carpenter", "Cop"
	elif "improve" in area_1.lower() and "build" in area_2.lower():
		return "Landscaper", "Cleaner"
	else:
		dead("Learn to type else you will end up a dead beat.")
	
#Function to output comments & notes	
def dead(why):
	print why, "Nice job!"
	exit(0)
	
#Function to output final recommendations	
def reccomendation(area_1, area_2):
	print "We reccomend %s and %s as your top 2 majors." % (area_1, area_2)
	exit(0)
	
#Function to start program by providing instructions	
def start():
	print "You are about to finish high school."
	print "You are thinking about going to college."
	print "Are you going to pursue college right after high school?"
	
	undergrad_choice = raw_input("> ")
	
	if undergrad_choice.lower() == "yes":
		do_undergrad = True
		subject_1, subject_2 = favorite_subjects()
		recco_1, recco_2 = process_subjects(subject_1, subject_2)
		reccomendation(recco_1, recco_2)
	elif undergrad_choice.lower() == "no":
		do_undergrad = False
		skill_1, skill_2 = favorite_skills()
		recco_1, recco_2 = process_skills(skill_1, skill_2)
		reccomendation(recco_1, recco_2)
	else:
		dead("Learn to type else you will end up a dead beat.")

start()