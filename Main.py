import pygame
import time as t
pygame.init()
x=0
win = pygame.display.set_mode((640,640))

pygame.display.set_caption("Main Menu")
Background = [pygame.image.load('cavemen.png'),pygame.image.load("Medieval.png"),pygame.image.load('modern.png'),pygame.image.load('future.png')]


def loadBG ():
    #x=0
    #if x > 3:
        x = 0

    #else:
        win.blit(Background[x],(0,0))
        #x =x +1
        pygame.display.update()
        #t.sleep(1)
def title ():
    
    title = pygame.image.load('time heist.png')
    win.blit(title, (175, 50))
    
    pygame.display.update()




class button ():
    def __init__(self, color, width, height, x, y, text = ''):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.text = text


    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
        if self.text == 'START':
            font = pygame.font.SysFont('comicsans', 40)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))


        else:
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (255,255,255))
            win.blit(text, (self.x + int(self.width/2 - text.get_width()/2), self.y + int(self.height/2 - text.get_height()/2)))


    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False


        
def desc():
    Exit = button((255,0,0),30,30,500,103)
    txt1 = 'In this game you have to progress'
    txt2 = 'through the level killing'
    txt3 = 'the enimies and avoiding'
    txt4 = 'the obstacles as fast as you'
    txt5 = 'can to score the highest amount of points.'
    txt6 = 'Enimies left alive will deduct points'
    txt7 = 'from your total score!!'
    
    pygame.draw.rect(win,(255,187,13), (105,100,430,250),0)
    font = pygame.font.SysFont('comicsans',30)
    text = font.render(txt1, 1, (255,255,255))
    text1 = font.render(txt2, 1, (255,255,255))
    text2 = font.render(txt3, 1, (255,255,255))
    text3 = font.render(txt4, 1, (255,255,255))
    text4 = font.render(txt5, 1, (255,255,255))
    text5 = font.render(txt6, 1, (255,255,255))
    text6 = font.render(txt7, 1, (255,255,255))
    win.blit(text, (120,150))
    win.blit(text1, (120,170))
    win.blit(text2, (120,190))
    win.blit(text3, (120,210))
    win.blit(text4, (120,230))
    win.blit(text5, (120,250))
    win.blit(text6, (120,270))
    Exit.draw(win, (0,0,0))   

clock = pygame.time.Clock()
FPS = 120
gamerun = True
startbutton = button((255,187,13),100,60,260,320,'START')
Description = button((255,187,13),100,60,260,420,'DESCRIPTION')
pos = pygame.mouse.get_pos()
x=0
while gamerun == True:
    pos = pygame.mouse.get_pos()

    
    clock.tick(FPS)
   


    if x > 3:
       x = 0

    else:
        win.blit(Background[x], (0,0))
        x = x+1

    #loadBG()    
    startbutton.draw(win, (0,0,0))
    Description.draw(win, (0,0,0))
    title()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False
            pygame.quit()
            quit()


        if event.type == pygame.MOUSEBUTTONDOWN:
            if startbutton.isOver(pos):
                startbutton.color = (255,0,0)
                pygame.display.quit()
                exec(open('game.py').read())
                
                

        if event.type == pygame.MOUSEMOTION:
            if startbutton.isOver(pos):
                startbutton.color = (14,204,176)
            else:
                startbutton.color = (255,187,13)


        if event.type == pygame.MOUSEBUTTONDOWN:
            if Description.isOver(pos):
                Description.color = (255,0,0)
                display = True
                while display:
                    desc()
                    pygame.display.update()
                
                

        if event.type == pygame.MOUSEMOTION:
            if Description.isOver(pos):
                Description.color = (14,204,176)
            else:
                Description.color = (255,187,13)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if Exit.isOver(pos):
                gamerun = false
                gamerun = True
                
    pygame.time.wait(150)




pygame.display.update()














        
