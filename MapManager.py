from Personnage import CharactersManager
from treasures import TreasureManager
import curses
import random as rand

class Salle:
    def __init__(self,pos,size):
        self.pos = pos
        self.size = size
        


    

class Map:
    characterslist = CharactersManager()
    treasurelist = TreasureManager()
    
    def __init__(self):
        self.carte = [[0]*50 for i in range(50)]
        self.listeSalles = [[0]*3 for i in range(3)]
        # self.treasurelist = treasurelist
        # self.characterslist = characterslist
        

    def creer_salle(self,size,x,y,i,j):
        n = 0
        bool = rand.randrange(0,2)
        if ((49 - x)>=size and (49 - y)>=size):
            for k in range(x,x+5):
                w = y
                for l in range(w,w+5):
                    
                    self.carte[k][l] = 1

                    if (k == x or k == x+4 or l == y or l == y+4):
                        self.carte[k][l] = 3
                    if (k == x and l == y + 2) or (k == x + 2 and l == y) or (k == x+2 and l == y+4) or (k == x+4 and l == y+2):
                        self.carte[k][l] = 2
                    n += 1
                
        x_moo = rand.randrange(x+1,x+4)
        y_moo = rand.randrange(y+1,y+4)
        if bool == 0:
            self.characterslist.addCharacter((x_moo,y_moo))
        if bool == 1:
            self.treasurelist.addTreasure((x_moo,y_moo))
        
        
        self.listeSalles[i][j] = Salle((x,y),size)
        

    def peutAller(self,pos,direction):
        x = pos[0]
        y = pos[1]
        if (x > 0 and direction == "sud" and self.carte[x-1][y] > 0):
            return True
        elif (x == 49 and direction == "nord" and self.carte[x+1][y] > 0):
            return True
        elif (y == 0 and direction == "ouest" and self.carte[x][y-1] > 0):
            return True
        elif (y == 49 and direction == "est" and self.carte[x][y+1] > 0):
            return True
        else:
            return False

    def relier_Salles(self, i1, j1, i2, j2,d):
            salle1 = self.listeSalles[i1][j1]
            salle2 = self.listeSalles[i2][j2]
            if d == "hb":
                x = salle1.pos[0] + 2
                y = salle1.pos[1]
                xf = salle2.pos[0] + 2
                yf = salle2.pos[1] + 4
                while y > j1*16:
                    y-=1
                    self.carte[x][y] = 2
                    
                if x > xf:
                    while x>xf:
                        x-=1
                        self.carte[x][y] = 2
                else:
                    while x<xf:
                        x+=1
                        self.carte[x][y] = 2
                while y > yf +1:
                    y-=1
                    self.carte[x][y] = 2

                
            if d == "gd":
                x = salle1.pos[0] 
                y = salle1.pos[1] +2
                xf = salle2.pos[0] +4
                yf = salle2.pos[1] + 2
                while x < i2*16:
                    x+=1
                    self.carte[x][y] = 2
                    
                if y > yf:
                    while y>yf:
                        y-=1
                        self.carte[x][y] = 2
                        
                else:
                    while y<yf:
                        y+=1
                        self.carte[x][y] = 2
                        
                while x < xf -1:
                    x+=1
                    self.carte[x][y] = 2
                    
        

    
    def creer_niveau(self):
        for i in range(3):
            for j in range(3):
                x = rand.randrange(i*16,(i+1)*16 - 5)
                y = rand.randrange(j*16,(j+1)*16 - 5)
                self.creer_salle(5,x,y,i, j)

        self.relier_Salles(1,2, 1, 1, "hb")
        self.relier_Salles(1,1, 1, 0, "hb")
        self.relier_Salles(0,1, 1, 1, "gd")
        self.relier_Salles(1,1, 2, 1, "gd")
        
        
        self.relier_Salles(0,2, 0, 1, "hb")
        self.relier_Salles(0,1, 0, 0, "hb")
        self.relier_Salles(2,2, 2, 1, "hb")
        self.relier_Salles(2,1, 2, 0, "hb")
                  
def test():
    map = Map()
    map.creer_niveau()
    print(map.carte)

    

    

    



