umur = int(input("Masukan umur anda : "))

if umur < 0:
    print("anda belum lahir")
elif umur < 18:
    print("anda belum cukup umur")
elif umur >= 18 and umur <= 60:
    print("anda cukup umur")
elif umur > 60:
    print("banyakin ibadah, bentar lagi mati")

print("Program selesai")
