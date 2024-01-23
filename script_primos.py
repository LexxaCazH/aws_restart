def primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = [str(num) for num in range(1, 251) if primo(num)]

with open("results.txt", "w") as archivo:
    archivo.write("\n".join(primos))

print("Números primos entre 1 y 250")
