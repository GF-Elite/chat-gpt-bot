import random

def tebak_angka():
    angka_rahasia = random.randint(1, 100)
    tebakan = 0
    while True:
        tebakan = int(input("Tebak angka antara 1-100: "))
        if tebakan < angka_rahasia:
            print("Tebakan terlalu kecil! Coba lagi.")
        elif tebakan > angka_rahasia:
            print("Tebakan terlalu besar! Coba lagi.")
        else:
            print("Selamat, kamu berhasil menebak angka yang benar!")
            break

tebak_angka()
