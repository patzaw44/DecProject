from faker import Faker

fake = Faker('pl_PL')

# Index,Year,Age,Name,Movie
people = []
for i in range(100000):
    first_name = fake.first_name()
    last_name = fake.last_name()
    name = f"{first_name} {last_name}"
    print(name)
    age = fake.pyint(min_value=20, max_value=70)
    print(age)

    year = fake.year()
    print(year)

    movie1 = fake.catch_phrase()
    print(movie1)

    movie2 = fake.sentence(3)
    print(movie2)
    movie3 = fake.text(15)
    print(movie3)
    people.append((i, name, age, year, movie1, movie2, movie3))

print(people)

