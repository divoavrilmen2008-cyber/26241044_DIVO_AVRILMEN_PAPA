# P3_NIM_Nama.py
# Program Identitas Mahasiswa

print("================================")
print("     IDENTITAS MAHASISWA")
print("================================")

# Input data
nama = input("Masukkan Nama           : ")
nim_teks = input("Masukkan NIM            : ")
prodi = input("Masukkan Program Studi  : ")

# Konversi dan pengambilan 2 digit terakhir NIM
nim = int(nim_teks)
dua_digit_nim = int(nim_teks[-2:])

print()
print("================================")
print("        HASIL PROGRAM")
print("================================")
print()

print("Nama          :", nama)
print("NIM           :", nim)
print("Prodi         :", prodi)
print("2 Digit NIM   :", dua_digit_nim)

print()
print("Tipe Data Nama:", type(nama))
print("Tipe Data NIM :", type(nim))
print("Tipe Data Prodi :", type(prodi))
print("Tipe Data 2 Digit NIM :", type(dua_digit_nim))
print("================================")