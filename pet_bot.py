
#import configparser
#config = configparser.ConfigParser()
#config.read("configPet.ini")

class Pet(object):
    stars = 0#целое от 0 до бесконечность+
    level = 0#целое от 0 до 100+
    skill = 1#вещественное от 0 до 2.5
    name = ""
    def __init__(self, name):
        self.name = name
    def about(self):
        return self.printName()+self.printStars()+self.printLevel()+self.printSkill()
    def printName(self):
        return self.name+"\n"
    def printLevel(self):
        return "Уровень: "+str(self.level)+"\n"
    def printStars(self):
        return "Звездочки: "+str(self.stars)+"\n"
    def printSkill(self):
        return "Рабочий навык: "+str(self.skill)+"\n"
    



pet = Pet("petya")

#print(pet.about())
