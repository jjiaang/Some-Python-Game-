import pygame

pygame.init()

pygame.font.init()

class Counter():

    def __init__(self,xpos,ypos):
        self.x = xpos
        self.y = ypos

        self.newFont = pygame.font.SysFont("Arial",12)

    # Displays the X position counter
    def printXPOS(self,window,player):
        text = self.newFont.render("x = " + str(int(player.x)),1,(255,255,255))
        window.blit(text,(self.x,self.y))

    # Displays the Y position counter
    def printYPOS(self,window,player):
        text = self.newFont.render("y = " + str(player.y),1,(255,255,255))
        window.blit(text,(self.x,self.y+15))

    # Displays whether or not you got the Key
    def printKey(self,window,keyValue):
        text = self.newFont.render("Recieved key = " + str(keyValue),1,(255,255,255))
        window.blit(text,(self.x,self.y+30))