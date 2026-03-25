hours = input('Enter the worked hours in week: ')
wage = int(input('Enter the hourly wage: '))

hours = hours.split()

week_hours = [int(x) for x in hours]

total_hours = sum(week_hours)

if total_hours <= 40:
  total_wage  = total_hours * wage
else:  
  overtime = total_hours - 40
  total_wage = 40 * wage + overtime * wage * 1.5

print('the total wage in week is',total_wage)   



'''# Input weekly hours (example: "8 8 8 8 8 4 0")
hours = input("Enter hours worked each day in a week (7 numbers): ")

# Wage per day
day_wage = 500

# Convert day wage into hourly wage (assuming 8 hours per day)
hourly_wage = day_wage / 8

# Split into list and convert to integers
week_hours = [int(x) for x in hours.split()]

# Calculate total weekly hours
total_hours = sum(week_hours)

# Wage calculation
if total_hours <= 40:
    total_wages = total_hours * hourly_wage
else:
    overworked = total_hours - 40
    total_wages = 40 * hourly_wage + overworked * hourly_wage * 1.5

print("The total wage is ₹", total_wages)
'''