import random
import time

Gold = 10000


class Enemey():
    def __init__(self, hp, attackPower, sheild, size):
        self.hp = hp
        self.attackPower = attackPower
        self.sheild = sheild
        self.size = size

    def __str__(self):
        return "\n\t\tEnemy Status\nHp = {}\nAttackPower = {}\nSheild = {}\nSize = {}\n".format(self.hp,
                                                                                                self.attackPower,
                                                                                                self.sheild,
                                                                                                self.size)


class Robo():
    def __init__(self, hp=3, AttackPower=2, sheild=1, soldiers=0):
        self.hp = hp
        self.AttackPower = AttackPower
        self.sheild = sheild
        self.soldiers = soldiers


    def SellSoldiers(self):
        global Gold
        Squantity = int(input("How Many Soldier You Sell: "))

        if Squantity > self.soldiers:
            print("You Have Only {} Soldiers".format(self.soldiers))
        else:
            Gold += 1000 * Squantity

            self.soldiers -= Squantity

    def BuySoldier(self):
        global Gold
        quantity = int(input("How Many Soldier You Buy: "))

        if quantity * 1000 > Gold:
            print("Not Enough Gold...")
        else:
            Gold -= 1000 * quantity

            self.soldiers += quantity

    def Upgrade(self):
        global Gold
        print("What You Want Upgrade: \n 1-Guns(it gives power) \n 2-Sheild")
        up = int(input())

        if up == 1:
            if self.AttackPower >= 20:
                print("Your Attack Power is Full")

            else:
                if Gold < 1000 * (self.AttackPower + 1):
                    print("Not Enough Gold...")
                else:
                    Gold -= 1000 * (self.AttackPower + 1)
                    print("Your Attack Power Improved...")
                    self.AttackPower += 1


        elif up == 2:
            if self.sheild >= 20:
                print("Your Sheild is Full")

            else:
                if Gold < 1000 * (self.sheild + 1):
                    print("Not Enough Gold...")
                else:
                    Gold -= 1000 * (self.sheild + 1)
                    print("Your Sheild Improved...")
                    self.sheild += 1

        else:
            print("Undefined Value...")
            self.Upgrade()

    def GoTo(self):

        PlanetList = ["Mars", "Earth", "Base(Roboland)", "Wait Current Position", "Wait in Space",
                      "Discover New Planet"]

        print("""

        1--> Mars
        2--> Earth  
        3--> Base(Roboland)
        4--> Wait current positions  
        5--> Wait in Space
        6--> Discover New Planet
        7--> Detail Information
        8--> Exit

             """)

        while True:
            global location
            reply = int(input("Choose Planet = "))

            if reply > 0 and reply <= 6:
                location = PlanetList[reply - 1]
                print("You Are in {} now. ".format(location))
                break
            elif reply == 7:
                xlr.PlanetInfomation()
                break
            elif reply == 8:
                print("...")
                break
            else:
                print("Undefined Value...")

    def PlanetInfomation(self):
        print("""
           "Mars"  : "The Most Dangerous Population are Here",
           "Earth" : "The population are Not Dangerous ",
           "Base(Roboland)" : "Your peoples",
           "Wait Current Position " : "You Can only Stay There",
           "Discover New Planet" : "You cant know What will Happens..."
           """)


    def Attack(Self, planet):
        global Gold
        score = ((xlr.hp + xlr.sheild) * xlr.soldiers) - (planet.attackPower * planet.size)
        gainGold = (planet.attackPower * planet.size) - (
                    (planet.attackPower * planet.size) - ((xlr.hp + xlr.sheild) * xlr.soldiers))

        Gold += gainGold * 1000

        if score < 0:
            print("Your Soldiers Failed... You are Only...")

            while True:

                print(xlr.__str__())
                print("\n")
                print(planet.__str__().format())

                print("Are you gonna die :)...")
                print("1- Fight \n 2- Escape")

                s = int(input("Your Choose: "))
                if s == 1:
                    planet.hp -= xlr.AttackPower - planet.sheild
                    if planet.hp < 0:
                        planet.size -= 1
                        if planet.size <= 0:
                            print("All Enemys Dead...")

                    xlr.hp -= planet.attackPower - xlr.sheild
                    if xlr.hp < 0:
                        xlr.soldiers -= 1
                        if xlr.soldiers <= 0:
                            print("All Enemys Dead...")


                elif s == 2:
                    print("You Know How Can you be alive")
                    break
                else:
                    print("Undefined...")


        else:
            xlr.soldiers = score / ((xlr.hp) * (xlr.soldiers))

            print("Congragulations You Win")


    def fight(self):
        global Gold
        print("""
                1--> Mars
                2--> Earth  
                3--> Base(Roboland)  
                4--> Discover New Planet
                5--> See Enemy Details
                6--> Exit
                     """)
        opponent = int(input("Choose Where Do you Attack: "))

        if opponent == 1:
            xlr.Attack(p_Mars)

        elif opponent == 2:
            xlr.Attack(p_Earth)

        elif opponent == 3:
            print("\n\nYou Will Fight With RoboKing For the Roboland...\n")
            xlr.Attack(p_roboland)


        elif opponent == 4:
            discover = random.randrange(1, 20)
            if discover > 16:
                xlr.Attack(p_RGroup)
            else:
                xlr.Attack(p_REnemy)



        elif opponent == 5:
            print("Mars->", p_Mars.__str__())
            print("Earth->", p_Earth.__str__())
            print("Roboland->", p_roboland.__str__())
            print("\n And You Can't Know New Planets...")

        else:
            print("Are You Scared ??")

    def __str__(self):
        return "\n\t\tStatus\nHp = {}\nAttackPower = {}\nSheild = {}\nSoldiers = {}\nGold = {}\n".format(self.hp,
                                                                                                         self.AttackPower,
                                                                                                         self.sheild,
                                                                                                         self.soldiers,
                                                                                                         Gold)


xlr = Robo()


p_Mars = Enemey(hp=3, attackPower=2, sheild=2, size=100)
p_Earth = Enemey(hp=1, attackPower=1, sheild=0, size=2000)
p_roboland = Enemey(hp=3, attackPower=2, sheild=2, size=500)
p_RGroup = Enemey(hp=random.randrange(1, 5), attackPower=random.randrange(1, 5), sheild=random.randrange(1, 5),
                  size=random.randrange(10, 500))
p_REnemy = Enemey(hp=random.randrange(1, 5), attackPower=random.randrange(3, 10), sheild=(1, 10), size=1)


def terminal():
    while True:
        print("""
     Terminal

     1-) Go to...
     2-) Attack
     3-) Upgrade you skills
     4-) Buy Soldiers
     5-) Sell Soldiers
     6-) All Status
     Exit (press 'q')

     """)
        choose = int(input("Choose What do you want to do : "))

        if choose == 'q':
            print("Thx For Play...")
            exit()

        elif choose == 1:
            xlr.GoTo()

        elif choose == 2:
            xlr.fight()

        elif choose == 3:
            xlr.Upgrade()

        elif choose == 4:
            xlr.BuySoldier()

        elif choose == 5:
            xlr.SellSoldiers()

        elif choose == 6:
            print("Status:", xlr.__str__())

        else:
            print("Please Choose Again...")
            continue


terminal()