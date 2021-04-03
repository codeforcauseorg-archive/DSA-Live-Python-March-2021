class Hitman:

    population = []

    def __init__(self, name):
        self.name = name
        self.alive = True
        self.kills = 0
        Hitman.population.append(self)

    def kill(self, enemy):
        if self.alive and enemy.alive:
            enemy.alive = False
            self.kills += 1
        elif not self.alive:
            print("Dead can not kill")
        else:
            print("You can not kill dead")

    # def __repr__(self):
    #     return "{} is alive - {} and killed = {}".format(self.name, self.alive, self.kills)


sai = Hitman("K Sai")
ravi = Hitman("Ravi")

sai.kill(ravi)
sai.kill(ravi)
sai.kill(ravi)
sai.kill(ravi)
sai.kill(ravi)
sai.kill(ravi)
sai.kill(ravi)

ravi.kill(sai)

print(ravi)

# print(Hitman.population)