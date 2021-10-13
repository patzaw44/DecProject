"""Zmodyfikuj program, który generował opowiadanie (Zadanie 1) tak, aby pobierał zmienne od użytkownika.
 Niech program dodatkowo wyświetla opowiadanie od tyłu"""

first_name = input("Enter male first name: ").title()
last_name = input("Enter male last name: ").title()
date_of_birth = int(input("Enter date of birth: "))
city = input("Enter city: ").title()
country = input("Enter country: ").title()
first_family_member = input("Enter father or grandfather: ")
name_of_the_first_family_member = input("Enter male second name: ").title()
profession_of_the_first_family_member = input("Enter the profession of a first family member: ")
second_family_member = input("Enter father or grandfather: ")
name_of_the_second_family_member = (input("Enter second male name: ").title())
profession_of_the_second_family_member = input("Enter the profession of a second family member: ")
number_of_older_sisters = int(input("Enter number of older sisters: "))
number_of_younger_sisters = int(input("Enter number of younger sisters: "))
number_of_younger_brothers = int(input("Enter number of younger brothers: "))

print(f"{first_name} {last_name} was born in {date_of_birth} in {city}, in {country}.\n"
      f"His {first_family_member}, {name_of_the_first_family_member}, was a {profession_of_the_first_family_member}.\n"
      f"His {second_family_member}, {name_of_the_second_family_member}, was a {profession_of_the_second_family_member}.\n"
      f"He had {number_of_older_sisters} older sisters, {number_of_younger_sisters} younger sisters and "
      f"{number_of_younger_brothers} younger brothers.")