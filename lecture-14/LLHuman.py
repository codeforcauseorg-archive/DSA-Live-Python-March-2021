class Human:

    def __init__(self, name, love=None):
        self.name = name
        self.love = love


ram = Human("Ram")
mohita = Human("Mohita")
shubham = Human("Shubham")
priya = Human("Priya")
shobhit = Human("Shobhit")

ram.love = mohita
mohita.love = shubham
shubham.love = priya
priya.love = shobhit

head = ram

print(head.love.love.name)