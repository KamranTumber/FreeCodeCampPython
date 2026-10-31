# ==========================================
# Python Data Types & Type Checking
# ==========================================

# 1. String (str): Represents textual data
name = "Alice"
print(name, type(name))  # type() returns the data type of the variable (<class 'str'>)


# 2. Boolean (bool): Represents truth values (True or False)
is_student = True
print(is_student, type(is_student))  # Outputs <class 'bool'>


# 3. Integer (int): Represents whole numbers
age = 20
print(age, type(age))  # Outputs <class 'int'>


# 4. Float (float): Represents numbers with decimal points
score = 80.5

# isinstance() checks if an object belongs to a specific class/type and returns True or False
print(isinstance(score, float))  # Outputs True

print(score, type(score))  # Outputs the value and <class 'float'>