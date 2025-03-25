from abc import ABC, abstractmethod

class Binatang:
    def __init__(self, nama, umur):
        if nama == "":
            raise ValueError("Data nama harus ada!")
        if umur == "":
            raise ValueError("Data umur harus ada!")
        if not isinstance(nama, str):
            raise ValueError("Nama harus dengan karakter yang valid!")
        if not isinstance(umur, (int, float)) or umur < 0:
            raise ValueError("Umur harus dengan angka positif yang valid!")
        
        self.__nama = nama
        self.__umur = umur

    @abstractmethod
    def make_sound(self):
        pass

    def get_nama(self):
        return self.__nama
    
    def get_umur(self):
        return self.__umur
    
    def set_umur(self, umur):
        if not isinstance(umur, (int, float)):
            raise ValueError("Umur harus dengan angka positif yang valid!")
        self.__umur = umur
        
class Anjing(Binatang):
    def make_sound(self):
        return "Woof!"
    
    def run(self):
        return f"{self.get_nama()} sedang berlari."
    
class Kucing(Binatang):
    def make_sound(self):
        return "Meow!"
    
    def sleep(self):
        return f"{self.get_nama()} sedang Tidur."

try:
    dog = Anjing("Jake", 3)
    cat = Kucing("Cake", 2)

    print(dog.get_nama())
    dog.set_umur(5)
    print(dog.get_umur())
    print(dog.make_sound())
    print(dog.run())
    print()

    print(cat.get_nama())
    print(cat.get_umur())
    print(cat.make_sound())
    print(cat.sleep())

except ValueError as e:
    print(f"Error : {e}")
