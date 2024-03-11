def mask(input_str):
	Masked_str=list(input_str)\
	For index in input_str:
		Mask_str[index] = “*”
	Return ‘’.join(masked_str)
 
def mask_string(input_str):
	return input_str[:2] + “*” * (len(input_str) - 2)
 
def mask_dob(input_date):
	Return f”{input_dob[:2]}” 
 
def mask_email(input_email):
	return f”{input_email[:2]}{}”
 
 
 
Employee = {}
 
Employee[first_name]=mask_string(input(“Enter first name:”))
Employee[last_name]=mask_string(input(“Enter last name:”))
Employee[date_of_birth]=mask_dob(input(“Enter date of birth name:”))
Employee[email]=mask_email(input(“Enter email:”))

print(Employee)
