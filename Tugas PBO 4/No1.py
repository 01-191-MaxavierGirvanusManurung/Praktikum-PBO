import math

while True:
    try:
        n = float(input("Masukkan angka : "))
        if n == 0:
            print("Error: Akar kuadrat dari nol tidak diperbolehkan.")
        elif n < 0:
            print("Input tidak valid. Harap masukkan angka positif.")
        else:
            x = math.sqrt(n)
            print(f"Akar kuadrat dari {n} adalah {x}")
            break
    except ValueError:
        print("Input tidak valid. Harap masukkan angka yang valid.")
    
