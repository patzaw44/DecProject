"""Zmodyfikuj program, który generował opowiadanie (Zadanie 1) tak, aby pobierał zmienne od użytkownika.
 Niech program dodatkowo wyświetla opowiadanie od tyłu"""

# Pobieranie zmiennych
first_name = input("Enter male first name: ").title()
last_name = input("Enter male last name: ").title()
year_of_birth = int(input("Enter year of birth: "))
city = input("Enter city: ").title()
country = input("Enter country: ").title()
first_family_member = input("Enter father or grandfather: ")
name_of_the_first_family_member = input("Enter male second name: ").title()
profession_of_the_first_family_member = input("Enter the profession of a first family member: ")
second_family_member = input("Enter father or grandfather: ")
name_of_the_second_family_member = (input("Enter third male name: ").title())
profession_of_the_second_family_member = input("Enter the profession of a third family member: ")
number_of_older_sisters = int(input("Enter number of older sisters: "))
number_of_younger_sisters = int(input("Enter number of younger sisters: "))
number_of_younger_brothers = int(input("Enter number of younger brothers: "))
print()

# opowiadanie:
print(f"""{first_name} {last_name} was born in {year_of_birth} in {city}, in {country}.
His {first_family_member}, {name_of_the_first_family_member}, was a {profession_of_the_first_family_member}.
His {second_family_member}, {name_of_the_second_family_member}, was a {profession_of_the_second_family_member}.
He had {number_of_older_sisters} older sisters, {number_of_younger_sisters} younger sisters and 
{number_of_younger_brothers} younger brothers.""")
print()

# opowiadanie od tyłu:
story = (f"""{first_name} {last_name} was born in {year_of_birth} in {city}, in {country}.
      His {first_family_member}, {name_of_the_first_family_member}, was a {profession_of_the_first_family_member}.
      His {second_family_member}, {name_of_the_second_family_member}, was a {profession_of_the_second_family_member}.
      He had {number_of_older_sisters} older sisters, {number_of_younger_sisters} younger sisters and 
      {number_of_younger_brothers} younger brothers.""")

new_story = story[::-1]
print(new_story)