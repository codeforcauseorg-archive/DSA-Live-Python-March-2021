class Bird:

    population = 0

    def __init__(self):
        self.__wings = 2

    def fly(self):
        print("flying wohoooo")

    def getWingsCount(self):
        return self.__wings



chikoo = Bird()
print(chikoo.getWingsCount())


# Bird.fly(chikoo)
# chikoo.fly()

