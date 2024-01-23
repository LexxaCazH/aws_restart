def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Encuentra y almacena los números primos entre 1 y 250
primos = [str(num) for num in range(1, 251) if es_primo(num)]

# Almacena los resultados en un archivo
with open("results.txt", "w") as archivo:
    archivo.write("\n".join(primos))

print("Números primos entre 1 y 250 almacenados en results.txt.")
