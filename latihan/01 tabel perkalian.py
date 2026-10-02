# Latihan 1 - Tabel Perkalian
# Input: satu bilangan bulat
# Proses: mengulang perkalian dari 1 sampai 10
# Output: tabel perkalian

n = int(input("Bilangan: "))

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")