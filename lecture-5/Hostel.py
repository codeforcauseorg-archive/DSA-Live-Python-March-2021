class Human:

    population = 0

    def __init__(self, name):
        self.name = name
        self.balance = 1000
        Human.population += 1

    def party(self):
        if self.balance >= 100:
            print("{} like the partyyy".format(self.name))
            self.balance -= 100
        else:
            print("No money, no party")

    def borrow(self, friend, amount=500):
        if friend.balance >= amount:
            friend.balance -= amount
            self.balance += amount
            print("Take it")
        else:
            print("Bro! I am just like you")

sai = Human("K Sai")

for i in range(12):
    sai.party()
    print(sai.balance)

kartik = Human("Kartik")
print(kartik.balance)

sai.borrow(kartik, 2000)
sai.borrow(kartik)
sai.borrow(kartik)


# print("Populaion", Human.population)

