employees = ["Bernard", "Stubbs", "Theresa", "Charlotte", "Elsie"]

def employee_encouragement(list_of_employees):
	for employee in list_of_employees:
		if employee.title() == "Charlotte":
			print("You fucking suck, " + employee.title())
		else:
			print(employee.title() + " , You're doing a great job")

employee_encouragement(employees)			

# you're so hilarious ! 

