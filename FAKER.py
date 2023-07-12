from faker import Faker

# Crea un objeto Faker
fake = Faker()

# Genera datos ficticios
nombre = fake.name()
direccion = fake.address()
telefono = fake.phone_number()

# Imprime los datos ficticios generados
print("Nombre:", nombre)
print("Dirección:", direccion)
print("Teléfono:", telefono)
