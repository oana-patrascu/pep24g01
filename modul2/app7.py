nume = input('Cum te numesti?')
varsta = int(input('Ce varsta ai? '))

print(f'Ceau {nume} te ai nascut in {2024 - varsta}')


[7:46 PM] Vlad Lupu (Guest)
import datetime
today = datetime.date.today()
year = today.year
# Get name from user input
name = input("Your name: ").title()
# Get age from user input
age = int(input("Your age: "))
# Year of birth
yearOfBirth = year - age
print(f"""
What's your name? {name}
How old are you? {age}
Hello, {name}! So you were born in {yearOfBirth}""")
 like 1