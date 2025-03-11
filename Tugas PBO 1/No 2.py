n = int(input("Masukkan jumlah siswa : "))
data = {}

for i in range(n):
    nama = str(input(f"Masukkan nama siswa ke-{i+1}\t: "))
    nilai = float(input(f"Masukkan nilai untuk {nama}\t: "))
    data[nama] = nilai

print("\nDictionary = ", data)
