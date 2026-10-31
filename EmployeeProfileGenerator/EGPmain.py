# ==========================================
# 1. Personal Information & String Building
# ==========================================

# Define basic personal details as text (strings)
first_name = "John"
last_name = "Doe"

# Combine the first and last name using an f-string (formatted string literal)
full_name = f"{first_name} {last_name}"

# Initialize the base address and use augmented assignment (+=) to append the apartment
address = "123 Main Street"
address += ", Apartment 4B"


# ==========================================
# 2. Employment Details & F-Strings
# ==========================================

# Define the employee's age and use an f-string to embed the integer directly (no need for str())
employee_age = 28
employee_info = f"{full_name} is {employee_age} years old"
print(employee_info)

# Define years of experience and format it into a display string
experience_years = 5
experience_info = f"Experience: {experience_years} years"
print(experience_info)

# Create a detailed summary "card" combining multiple data types (strings, integers)
position = "Data Analyst"
salary = 75000
employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}"
print(employee_card)


# ==========================================
# 3. String Slicing (Parsing Employee Code)
# ==========================================

# Base employee code string following a specific format: 'DEV-2026-JD-001'
employee_code = "DEV-2026-JD-001"

# Extract the department prefix: takes characters from index 0 up to (excluding) index 3 -> 'DEV'
department = employee_code[0:3]
print(department)

# Extract the year code: takes characters from index 4 up to index 8 -> '2026'
year_code = employee_code[4:8]
print(year_code)

# Extract the initials: takes characters from index 9 up to index 11 -> 'JD'
initials = employee_code[9:11]
print(initials)

# Extract the trailing ID digits using negative indexing (-3 means start 3 characters from the end) -> '001'
last_three = employee_code[-3:]
print(last_three)