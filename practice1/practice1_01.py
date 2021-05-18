name = input("Enter your name, please: ")
age = int(input("Enter your age, please: "))
country = input("Enter your country, please: ")
pronoun = None
gender = None

while True:
    gender = input("Enter your gender, please(f for female, m for male): ")
    if gender == 'f':
        pronoun = 'she'
        break
    elif gender == 'm':
        pronoun = 'he'
        break
    else:
        continue

print(f"{name} is {age} years old, {pronoun} lives in {country}. {name} is a Geek Brains student.")