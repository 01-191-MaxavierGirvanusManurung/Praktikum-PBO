class Tugas:
    def __init__(self):
        self.tugas = []

    def tambah(self, tgs):
        self.tugas.append(tgs)
        print("Tugas berhasil ditambahkan!")

    def hapus(self, n):
        if not self.tugas:
            raise ValueError("Daftar tugas sedang kosong.")
        if n < 1 or n > len(self.tugas):
            raise ValueError(f"Tugas dengan daftar nomor {n} tidak ditemukan.")
        self.tugas.pop(n-1)
        print(f"Tugas dengan daftar nomor {n} telah dihapus.")

    def tampilkan(self):
        if not self.tugas:
            raise ValueError("Daftar Tugas kosong.")
        print("Daftar Tugas : ")
        for i in self.tugas:
            print(f"-{i}")
    
daftar = Tugas()
while True:
    print("\nPilih aksi")
    print("1. Tambah Tugas")
    print("2. Hapus Tugas")
    print("3. Tampilkan daftar Tugas")
    print("4. Keluar")

    try:
        pil = int(input("Masukkan pilihan : "))
        if pil not in [1,2,3,4]:
            raise ValueError("Masukkan pilihan yang sesuai!")
        
        if pil == 1:
            tugas = input("Masukkan tugas yang ingin ditambahkan : ")
            daftar.tambah(tugas)

        elif pil == 2:
            n = input("Masukkan nomor tugas yang ingin dihapus : ")
            if not n.isdigit():
                raise ValueError("Masukkan angka valid!")
            daftar.hapus(int(n))

        elif pil == 3:
            daftar.tampilkan()

        elif pil == 4:
            print("Keluar dari program.")
            exit()

    except ValueError as e:
        print(f"Error : {e}")
