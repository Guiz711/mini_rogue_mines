import random as rd

class Characters:
    def __init__(self, name, position, life, attack, accuracy, shield):
        self.name = name
        self.position = position
        self.life = life
        self.attack = attack
        self.accuracy = accuracy
        self.shield = shield

    def isCharacterAhead (self, charmanager, direction):
        x, y = self.position
        if direction =="nord":
            for k in range (len(charmanager.instance.charactersList)):
                xch, ych = charmanager.instance.charactersList[k].position
                if x+1 == xch and y == ych:
                    return k

        elif direction == "sud":
            for k in range (len(charmanager.instance.charactersList)):
                xch, ych = charmanager.instance.charactersList[k].position
                if x+1 == xch and y == ych:
                    return k

        elif direction == "est":
            for k in range (len(charmanager.instance.charactersList)):
                xch, ych = charmanager.instance.charactersList[k].position
                if x+1 == xch and y == ych:
                    return k

        elif direction == "ouest":
            for k in range (len(charmanager.instance.charactersList)):
                xch, ych = charmanager.instance.charactersList[k].position
                if x+1 == xch and y == ych:
                    return k
        
        return -1

    def move(self, charmanager, carte, direction):
        positionx, positiony = self.position
        if direction == "nord" and carte.peutAller(self.position, "nord"):
            k = self.isCharacterAhead(charmanager, direction)
            if k == -1:
                self.position = (positionx, positiony + 1)
            else:
                self.makeAttack (charmanager.charactersList[k])
        elif direction == "sud" and carte.peutAller(self.position, "sud"):
            k = self.isCharacterAhead(charmanager, direction)
            if k == -1:
                self.position = (positionx, positiony + 1)
            else:
                self.makeAttack (charmanager.charactersList[k])
        elif direction == "est" and carte.peutAller(self.position ,"est"):
            k = self.isCharacterAhead(charmanager, direction)
            if k == -1:
                self.position = (positionx, positiony + 1)
            else:
                self.makeAttack (charmanager.charactersList[k])
        elif direction == "ouest" and carte.peutAller(self.position, "ouest"):
            k = self.isCharacterAhead(charmanager, direction)
            if k == -1:
                self.position = (positionx, positiony + 1)
            else:
                self.makeAttack (charmanager.charactersList[k])

    def receiveAttack(self, charmanager, attacker):
        self.life -= (1-self.shield)*attacker.attack
        if self.life <=0:
            charmanager.removeCharacter(self)


    def makeAttack(self, defender):
        if (rd.random() < self.accuracy):
            defender.receiveAttack(self)


class Me (Characters):
    class __Me:

        def __init__ (self, name, position, life, attack, accuracy, shield):
            self.name = name
            self.position = position
            self.life = life
            self.attack = attack
            self.accuracy = accuracy
            self.shield = shield

    instance = None

    def __init__(self, name, position):
        if not instance:
            instance = Me(name, position, 20, 3, 0.95, 12)
            a = CharactersManager()
            a.append(instance)

    def getMe():
        return instance

class Monsters (Characters):

    def __init__(self, name, position, life, attack, accuracy, shield):
        self.name = name
        self.position = position
        self.life = life
        self.attack = attack
        self.accuracy = accuracy
        self.shield = shield

    def moveTowardMe (self, charmanager, carte):
        xmonster, ymonster = self.position
        xme, yme = getMe().position

        if abs(xme - xmonster) > abs(yme - ymonster):
            if xme > xmonster:
                self.move(charmanager, carte, "est")
            else:
                self.move(charmanager, carte, "ouest")
        else:
            if yme > ymonster:
                self.move(charmanager, carte, "sud")
            else:
                self.move(charmanager, carte, "nord")

class CharactersManager:
    class __CharactersManager:
        listOfCharacters = [
            {
                "name" : "Bat",
                "life" : 10,
                "attack" : 3,
                "accuracy" : 0.8,
                "shield" : 0.1
            }, 
            {
                "name" : "Snake",
                "life" : 20,
                "attack" : 5,
                "accuracy" : 0.85,
                "shield" : 0.2
            },
            {
                "name" : "BigBoss",
                "life" : 30,
                "attack" : 8,
                "accuracy" : 0.2,
                "shield" : 0.2
            }
            ]

        def __init__(self):
            self.charactersList = []

        def addMonster (self, position):
            i = rd.randint(0, 2)
            dico = self.listOfCharacters [i]
            name = dico["name"]
            life = dico["life"]
            attack = dico["attack"]
            accuracy = dico["accuracy"]
            shield = dico["shield"]
            newcharacter = Monsters (name, position, life, attack, accuracy, shield)
            self.charactersList.append(newcharacter)

        def removeCharacter (self, personnage):
            self.charactersList.remove(personnage)


    instance = None
    
    def __init__(self):
        if not CharactersManager.instance:
            CharactersManager.instance = CharactersManager.__CharactersManager()
    
    def addCharacter (self, position):
        CharactersManager.instance.addMonster(position)

    def removeCharacter (self, personnage):
        CharactersManager.instance.removeCharacter(personnage)

    def getCharactersManager():
        return instance
