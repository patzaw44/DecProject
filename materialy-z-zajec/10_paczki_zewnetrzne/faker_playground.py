from faker import Faker

fake = Faker('pl_PL')

print(fake.name())
print(fake.address())
print(fake.text())
print(fake.email())
print(fake.phone_number())
