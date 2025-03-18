import math

class Kalkulator:
    def __init__(self, nilai):
        self.nilai = float(nilai)

    def __add__(self, other):
        return Kalkulator(self.nilai + other.nilai)
    
    def __sub__ (self, other):
        return Kalkulator(self.nilai - other.nilai)
    
    def __mul__ (self, other):
        return Kalkulator(self.nilai * other.nilai)
    
    def __truediv__ (self, other):
        if other.nilai == 0:
            raise ValueError("Tidak valid, penyebut tidak boleh 0")
        return Kalkulator(self.nilai / other.nilai)
    
    def __pow__ (self, other):
        return Kalkulator(self.nilai ** other.nilai)
    
    def __str__(self):
        return str(self.nilai)
    
    def logaritma(self):
        if self.nilai <= 0:
            raise  ValueError("Logaritma hanya untuk bilangan positif")
        return Kalkulator(math.log10(self.nilai))
    
def main():
    while True:    
        print("Kalkulator Sederhana")
        print("Operasi  :   +, -, *, /, ^, log  ")
        print("Ketik 'exit' untuk keluar")

        pil = input("Pilihan operasi : ").lower()

        if pil == 'exit':
            print("Program selesai digunakan")
            break

        try:     
            if pil == 'log':
                angka = float(input("Masukkan bilangan : "))
                kalku = Kalkulator(angka)
                hasil = kalku.logaritma()
                print(f'Log {angka} = {hasil}\n')

            elif pil in ['+', '-', '*', '/', '^']:
                angka1 = float(input("Masukkan angka pertama: "))
                angka2 = float(input("Masukkan angka kedua  : "))

                nilai1 = Kalkulator(angka1)
                nilai2 = Kalkulator(angka2)

                if pil == '+':
                    hasil = nilai1 + nilai2
                elif pil == '-':
                    hasil = nilai1 - nilai2
                elif pil == '*':
                    hasil = nilai1 * nilai2
                elif pil == '/':
                    hasil = nilai1 / nilai2
                elif pil == "^":
                    hasil = nilai1 ** nilai2

                print(f'{angka1} {pil} {angka2} = {hasil}\n')
            
            else:
                print("Operasi yang dipilih tidak valid\n")
                continue

        except ValueError:
            print("Error: Masukkan angka yang valid!\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}\n")

if __name__ == "__main__":
    main()
