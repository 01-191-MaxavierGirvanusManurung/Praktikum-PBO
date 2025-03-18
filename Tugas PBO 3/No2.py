import random

class Father:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self._kemungkinanGol()

    def _kemungkinanGol(self):
        if self.blood_type == "A":
            return ["A", "O"]
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid.\nPilih A, B, AB, atau O.\n")
        
    def pil_allele(self):
        return random.choice(self.alleles)
    
class Mother:
    def __init__(self, blood_type):
        self.blood_type = blood_type.upper()
        self.alleles = self._kemungkinanGol()

    def _kemungkinanGol(self):
        if self.blood_type == "A":
            return ["A", "O"]
        elif self.blood_type == "B":
            return ["B", "O"]
        elif self.blood_type == "AB":
            return ["A", "B"]
        elif self.blood_type == "O":
            return ["O", "O"]
        else:
            raise ValueError("Golongan darah tidak valid.\nPilih A, B, AB, atau O.\n")
        
    def pil_allele(self):
        return random.choice(self.alleles)
    
class Child:
    def __init__(self, father, mother):
        self.father = father.pil_allele()
        self.mother = mother.pil_allele()
        self.blood_type = self._kemungkinan()

    def _kemungkinan(self):
        allele = sorted([self.father, self.mother]) 
        if "A" in allele and "B" in allele:
            return "AB"
        elif "A" in allele:
            return "A"
        elif "B" in allele:
            return "B"
        elif allele == ["O", "O"]:
            return "O"
        
    def __str__(self):
        return f"Golongan darah anak : {self.blood_type}"
    
def main():
    print("Pewarisan Golongan Darah")
    try:
        golAyah = input("Masukkan golongan darah ayah   : ")
        golIbu = input("Masukkan golongan darah ibu    : ")

        Ayah = Father(golAyah)
        Ibu = Mother(golIbu)
        anak = Child(Ayah, Ibu)

        print(f"Golongan darah Ayah : {golAyah}")
        print(f"Golongan darah Ibu  : {golIbu}")
        print(anak)
    
    except ValueError as e:
        print(f'Error: {e}')
    except Exception as e:
        print(f"Terjadi kesalahan : {e}")


if __name__ == "__main__":
    main()
