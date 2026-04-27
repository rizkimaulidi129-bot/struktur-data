import re

# Input nama pendek (maksimal 1 kata pendek)
while True:
    nama = input("Masukan nama anda : ")
    if len(nama) > 0 and len(nama) <= 10 and nama.isalpha():
        print(f"Halo, {nama}! Lanjut ke program selanjutnya.\n")
        break
    else:
        print("Silahkan coba lagi\n")

# Input angka untuk tabel perkalian
while True:
    try:
        angka = int(input("Masukkan angka: "))
        break
    except ValueError:
        print("Input tidak valid, masukkan angka!")

# Tampilkan tabel perkalian 1 sampai 10
for i in range(1, 11):
    print(f"{angka} x {i} = {angka * i}")
