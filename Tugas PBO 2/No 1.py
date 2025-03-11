import random

class Robot:
    def __init__(self, nama, hp, damage):
        self.nama = nama
        self.damage = damage
        self.hp = hp
        self.Max_hp = hp
        self.defend = False
    
    def attack(self, target):
        if random.random() < 0.8:
            attack_damage = self.damage
            target.hp -= self.damage
            if target.defend == True:
                attack_damage = self.damage - (self.damage * 0.7) 
            print(f"{self.nama} memberikan kerusakan pada {target.nama} sebesar {attack_damage}")
        else:
            print(f"{self.nama} gagal menyerang {target.nama}")
        self.defend = False

    def regen(self):
        heal = random.randint(5, 10)
        self.hp += heal
        if(self.Max_hp <= self.hp):
            self.hp = self.Max_hp
        print(f"{self.nama} memulihkan {heal} HP")
        self.defend = False

    def defend_mode(self):
        self.defend = True
        print(f"{self.nama} siap bertahan")

    def isAlive(self):
        return self.hp > 0
    
    def isDead(self):
        return self.hp <= 0

class Game:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2
        self.ronde = 1

    def turn(self, robot, target):
        while True:
            print("\n1. Attack      2. Defend       3. Regen        4. Surrender")
            action = input(f"{robot.nama}, pilih aksi: ")
            if action == "1":
                robot.attack(target)
                return
            elif action == "2":
                robot.defend_mode()
                return
            elif action == "3":
                robot.regen()
                return
            elif action == "4":
                print(f"\n----------{target.nama} menang----------")
                exit()
            else:
                print("Pilih aksi yang sesuai")
    
    def gameplay(self):
        while self.robot1.isAlive() and self.robot2.isAlive():
            print(f"\nRound-{self.ronde} ==========================================================")
            print(f"{self.robot1.nama} [{self.robot1.hp}|{self.robot1.damage}]")
            print(f"{self.robot2.nama} [{self.robot2.hp}|{self.robot2.damage}]")

            self.turn(self.robot1, self.robot2)
            self.turn(self.robot2, self.robot1)

            if self.robot1.isAlive() and self.robot2.isDead():
                print(f"\n----------{self.robot1.nama} menang----------")

            if self.robot2.isAlive() and self.robot1.isDead():
                print(f"\n----------{self.robot2.nama} menang----------")
                
            self.ronde += 1

robotA = Robot("Ace", 500, 50)
robotB = Robot("Heart", 400, 50) 
robotC = Robot("Diamond", 500, 30) 
robotD = Robot("Club", 400, 30) 

print("Pilihan Robot : ")
print("1. Ace; HP = 500, Damge = 50")
print("2. Heart; HP = 400, Damge = 50")
print("3. Diamond; HP = 500, Damge = 30")
print("4. Club; HP = 400, Damge = 30")

robot_1 = robotA
robot_2 = robotA

P = True
while P == True:
    P = False
    pil = input("Robot 1: ")
    if pil == "1":
        robot_1 = robotA
    elif pil == "2":
        robot_1 = robotB
    elif pil == "3":
        robot_1 = robotC
    elif pil == "4":
        robot_1 = robotD
    else:
        P = True
        print("Pilih yang sesuai")

P = True
while P == True:
    P = False
    pil1 = input("Robot 2: ")
    if pil1 == "1":
        robot_2 = robotA
    elif pil1 == "2":
        robot_2 = robotB
    elif pil1 == "3":
        robot_2 = robotC
    elif pil1 == "4":
        robot_2 = robotD
    else:
        P = True
        print("Pilih yang sesuai")

game = Game(robot_1, robot_2)
game.gameplay()
