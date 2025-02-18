from datetime import datetime
def calculate_age(year_of_birth):
    current_year = datetime.now().year
    return current_year - year_of_birth
name = str(input("Enter your name: "))
try:
    year_of_birth = int(input("Enter your year of birth: "))
    age = calculate_age(year_of_birth)
    print(f"Hello, {name}! You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
