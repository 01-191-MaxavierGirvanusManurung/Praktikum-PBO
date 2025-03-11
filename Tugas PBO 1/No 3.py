nama = str(input("Masukkan nama : "))
nim = str(input("Masukkan NIM : "))
resolusi = str(input("Masukkan Resolusi Tahun Ini : "))

with open('Me.txt', 'w') as f:
    f.write(f"Masukkan nama\t\t\t\t: {nama}\n")
    f.write(f"Masukkan NIM\t\t\t\t: {nim}\n")
    f.write(f"Masukkan Resolusi Tahun Ini\t: {resolusi}\n")

with open('Me.txt', 'r') as f:
    f.read()
