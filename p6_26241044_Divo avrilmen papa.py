# Tugas Pertemuan 6 - Operator Logika NOT, AND, OR, XOR
# Nama: Divo Aveilmen Papa
# NIM: 26241044

a = int(input("Digit A : "))
b = int(input("Digit B : "))

kondisi1 = a >= 5
kondisi2 = b >= 5

print("Kondisi 1 :", kondisi1)
print("Kondisi 2 :", kondisi2)
print("NOT :", not kondisi1)
print("AND :", kondisi1 and kondisi2)
print("OR  :", kondisi1 or kondisi2)
print("XOR :", kondisi1 ^ kondisi2)

# OR dan XOR berbeda ketika kedua kondisi True karena OR bernilai True jika salah satu atau keduanya True,
# sedangkan XOR hanya True jika salah satu saja yang True, dan False jika keduanya sama (True-True / False-False).