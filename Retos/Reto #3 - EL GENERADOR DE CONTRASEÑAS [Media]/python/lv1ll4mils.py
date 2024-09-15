import string, random

def generador_password() -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation

    longitud = random.randint(8, 16)

    password = ''.join(random.choice(caracteres) for _ in range(longitud))

    return password

password = generador_password()
print(password)
