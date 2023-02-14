'''
The Customer Service Represetatives (CSRs) in the marketing department with a security clearance of 'TS' were able
to thwart an attack on the server and for that management has decided to reward them with a 10% increase in their salary. 
To evaluate the impact on the budget, you have been asked to run a report on the employee file and display the results 
of BEFORE AND AFTER the salary increase. Also calculate the total difference between the old salary and the new
salary (as shown in the image).

You will create a dictionary that has the full employee name as the key and only their NEW salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as shown in the image)
'''

import csv

#open the file
with open("employee_data","r") as file:
    data = csv.reader(file)
    header = file.readline().strip().split(",")
    first_name_index = header.index("First Name")
    last_name_index = header.index("Last Name")
    clearance_index = header.index("Clearance")


total_difference = 0
for employee in data:
    if data['Clearance'] == 'TS':
        old_salary = data['Salary']
        new_salary = old_salary * 1.1  # 10% increase
        total_difference += (new_salary - old_salary)

employee_dict = {}
for employee in data:
    if data['Clearance'] == 'TS':
        new_salaries[data['name']] = data['salary'] * 1.1
        employee_dict.append(new_salaries)

print("Employee Name:",header.index("First Name") and header.index("Last Name") )
print("Total difference: $", total_difference)
print("New salaries: ", new_salaries)



    

#print()
#print('=========================================')
#print()

#iternate through the dictionary and print out the key and value as per image




          

#print()
#print('=========================================')
#print()

#print out the total difference between the old salary and the new salary as per image.

        
    

