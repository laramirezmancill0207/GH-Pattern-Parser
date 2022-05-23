from asyncio.proactor_events import _ProactorDuplexPipeTransport
from msvcrt import kbhit
import pygame, random
import PIL.Image
import io
import time


pygame.init()


display_width = 640
display_height = 640

black = (0,0,0)
white = (255,255,255)
yellow = (255, 255, 0)
red = (255, 0, 0)
green = (0, 255, 0)

end = False;
clock = pygame.time.Clock()
inputString = ""

displayPage = []
count = 0;
state = 0;
prevState = -1;

def exit():
    gameDisplay.fill(black)

    font = pygame.font.Font('freesansbold.ttf', 32)
    font1 = pygame.font.Font('freesansbold.ttf', 15)
    text = font.render('String Not Accepted', True, white, black)
    text1 = font1.render('"'+ inputString + '"', True, red, black)
    textRect = text.get_rect()
    textRect.center = (320, 320)

    textRect1 = text1.get_rect()

    textRect1.center = (320, 360)

    gameDisplay.blit(text, textRect)
    gameDisplay.blit(text1, textRect1)
    pygame.display.update()

    time.sleep(5)
    pygame.quit()
    quit()

def drawDFA(stat):
    gameDisplay.fill(white)
    font = pygame.font.Font('freesansbold.ttf', 10)
    font1 = pygame.font.Font('freesansbold.ttf', 20)

    #arrows
    t = pygame.Surface((500, 500))

    t.fill(white)
    
    t1 = pygame.image.load("loop.png").convert()
    t1 = pygame.transform.scale(t1, (50, 50))
    t2 = pygame.image.load("yloop.png").convert()
    t2 = pygame.transform.scale(t2, (50, 50))



    if state == 0 and prevState == 0:
        gameDisplay.blit(t2, (12, 245))
    else:
        gameDisplay.blit(t1, (12, 245))
    

    

    text = font1.render('g', True, black, white)
    textRect = text.get_rect()
    textRect.center = (12, 270)
    gameDisplay.blit(text, textRect)

    if state == 0 and prevState == -1:
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (30, 20))
        gameDisplay.blit(t, (0, 315))

    else:
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (30, 20))
        gameDisplay.blit(t, (0, 315))




    #acc
    if state == -1:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (90, 25))
        t = pygame.transform.rotate(t, 270)
        gameDisplay.blit(t, (23, 345))

        

    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (90, 25))
        t = pygame.transform.rotate(t, 270)
        gameDisplay.blit(t, (23, 345))

    

    #ascend

    if state == 1 and prevState == 0:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (60, 210))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (60, 210))
    

    if state == 2 and prevState == 1:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (200, 140))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (200, 140))
    

    if state == 3 and prevState == 2:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (340, 70))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (340, 70))

    if state == 4 and prevState == 3:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (480, 0))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, 28)
        gameDisplay.blit(t, (480, 0))



    #descend

    if state == 5 and prevState == 0:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (50, 325))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (50, 325))

    if state == 6 and prevState == 5:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (190, 395))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (190, 395))

    if state == 7 and prevState == 6:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (330, 465))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (330, 465))

    if state == 8 and prevState == 7:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, yellow, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (470, 535))
    else:
        t = pygame.Surface((500, 500))
        t.fill(white)
        pygame.draw.polygon(t, black, ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
        t = pygame.transform.scale(t, (190, 25))
        t = pygame.transform.rotate(t, -28)
        gameDisplay.blit(t, (470, 535))


    
    if state == 6 and prevState == 0:
        gameDisplay.blit(pygame.image.load("ya.png"), (7, 23))
    else:
        gameDisplay.blit(pygame.image.load("a.png"), (7, 23))

    if state == 7 and prevState == 0:
        gameDisplay.blit(pygame.image.load("yar.png"), (7, 23))
    else:
        gameDisplay.blit(pygame.image.load("ar.png"), (7, 23))
    

    text = font1.render('y', True, black, white)
    textRect = text.get_rect()
    textRect.center = (260, 300)
    gameDisplay.blit(text, textRect)


    text = font1.render('b', True, black, white)
    textRect = text.get_rect()
    textRect.center = (180, 330)
    gameDisplay.blit(text, textRect)


    if state == 0 and prevState == 1:
        gameDisplay.blit(pygame.image.load("yarr.png"), (-10, -40))
    else:
        gameDisplay.blit(pygame.image.load("arr.png"), (-10, -40))

    if state == 0 and prevState == 2:
        gameDisplay.blit(pygame.image.load("yarro.png"), (-10, -40))
    else:
        gameDisplay.blit(pygame.image.load("arro.png"), (-10, -40))

    if state == 0 and prevState == 3:
        gameDisplay.blit(pygame.image.load("yaa.png"), (-10, -40))
    else:
        gameDisplay.blit(pygame.image.load("aa.png"), (-10, -40))

    if state == 0 and prevState == 4:
        gameDisplay.blit(pygame.image.load("yaaa.png"), (-10, -50))
    else:
        gameDisplay.blit(pygame.image.load("aaa.png"), (-10, -50))


    text = font1.render('g', True, black, white)
    textRect = text.get_rect()
    textRect.center = (400, 15)
    gameDisplay.blit(text, textRect)

    text = font1.render('g', True, black, white)
    textRect = text.get_rect()
    textRect.center = (280, 80)
    gameDisplay.blit(text, textRect)

    text = font1.render('g', True, black, white)
    textRect = text.get_rect()
    textRect.center = (210, 150)
    gameDisplay.blit(text, textRect)

    text = font1.render('g', True, black, white)
    textRect = text.get_rect()
    textRect.center = (150, 205)
    gameDisplay.blit(text, textRect)

    #letters asc
    
    text = font1.render('.', True, black, white)
    textRect = text.get_rect()
    textRect.center = (55, 365)
    gameDisplay.blit(text, textRect)

    text = font1.render('r', True, black, white)
    textRect = text.get_rect()
    textRect.center = (100, 260)
    gameDisplay.blit(text, textRect)


    text = font1.render('y', True, black, white)
    textRect = text.get_rect()
    textRect.center = (240, 190)
    gameDisplay.blit(text, textRect)


    text = font1.render('b', True, black, white)
    textRect = text.get_rect()
    textRect.center = (380, 120)
    gameDisplay.blit(text, textRect)
    
    text = font1.render('o', True, black, white)
    textRect = text.get_rect()
    textRect.center = (520, 50)
    gameDisplay.blit(text, textRect)

    #letters desc

    text = font1.render('o', True, black, white)
    textRect = text.get_rect()
    textRect.center = (100, 400)
    gameDisplay.blit(text, textRect)


    text = font1.render('b', True, black, white)
    textRect = text.get_rect()
    textRect.center = (240, 470)
    gameDisplay.blit(text, textRect)


    text = font1.render('y', True, black, white)
    textRect = text.get_rect()
    textRect.center = (380, 540)
    gameDisplay.blit(text, textRect)
    
    text = font1.render('r', True, black, white)
    textRect = text.get_rect()
    textRect.center = (520, 610)
    gameDisplay.blit(text, textRect)

    #circles
    if state == -1:
        pygame.draw.circle(gameDisplay, yellow, (40, 420), 20)
        text = font.render('qA', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (40, 420)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (40, 420), 20)
        text = font.render('qA', True, white, black)
        textRect = text.get_rect()
        textRect.center = (40, 420)
        gameDisplay.blit(text, textRect)


    if state == 0:
        pygame.draw.circle(gameDisplay, yellow, (40, 320), 20)
        text = font.render('q0', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (40, 320)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (40, 320), 20)
        text = font.render('q0', True, white, black)
        textRect = text.get_rect()
        textRect.center = (40, 320)
        gameDisplay.blit(text, textRect)
    



    if state == 1:
        pygame.draw.circle(gameDisplay, yellow, (180, 250), 20)
        text = font.render('q1', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (180, 250)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (180, 250), 20)
        text = font.render('q1', True, white, black)
        textRect = text.get_rect()
        textRect.center = (180, 250)
        gameDisplay.blit(text, textRect)


    if state == 2:
        pygame.draw.circle(gameDisplay, yellow, (320, 180), 20)
        text = font.render('q2', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (320, 180)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (320, 180), 20)
        text = font.render('q2', True, white, black)
        textRect = text.get_rect()
        textRect.center = (320, 180)
        gameDisplay.blit(text, textRect)


    if state == 3:
        pygame.draw.circle(gameDisplay, yellow, (460, 110), 20)
        text = font.render('q3', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (460, 110)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (460, 110), 20)
        text = font.render('q3', True, white, black)
        textRect = text.get_rect()
        textRect.center = (460, 110)
        gameDisplay.blit(text, textRect)


    if state == 4:
        pygame.draw.circle(gameDisplay, yellow, (600, 40), 20)
        text = font.render('q4', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (600, 40)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (600, 40), 20)
        text = font.render('q4', True, white, black)
        textRect = text.get_rect()
        textRect.center = (600, 40)
        gameDisplay.blit(text, textRect)


    if state == 5:
        pygame.draw.circle(gameDisplay, yellow, (180, 390), 20)
        text = font.render('q5', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (180, 390)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (180, 390), 20)
        text = font.render('q5', True, white, black)
        textRect = text.get_rect()
        textRect.center = (180, 390)
        gameDisplay.blit(text, textRect)


    if state == 6:
        pygame.draw.circle(gameDisplay, yellow, (320, 460), 20)
        text = font.render('q6', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (320, 460)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (320, 460), 20)
        text = font.render('q6', True, white, black)
        textRect = text.get_rect()
        textRect.center = (320, 460)
        gameDisplay.blit(text, textRect)


    if state == 7:
        pygame.draw.circle(gameDisplay, yellow, (460, 530), 20)
        text = font.render('q7', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (460, 530)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (460, 530), 20)
        text = font.render('q7', True, white, black)
        textRect = text.get_rect()
        textRect.center = (460, 530)
        gameDisplay.blit(text, textRect)
        
    if state == 8:
        pygame.draw.circle(gameDisplay, yellow, (600, 600), 20)
        text = font.render('q8', True, black, yellow)
        textRect = text.get_rect()
        textRect.center = (600, 600)
        gameDisplay.blit(text, textRect)
    else:
        pygame.draw.circle(gameDisplay, black, (600, 600), 20)
        text = font.render('q8', True, white, black)
        textRect = text.get_rect()
        textRect.center = (600, 600)
        gameDisplay.blit(text, textRect)

    

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('Guitar Hero DFA')

icon = pygame.image.load('logo.jpg').convert();
pygame.display.set_icon(icon);



notes = []
notes.append(pygame.image.load('green.png').convert())
notes.append(pygame.image.load('red.png').convert())
notes.append(pygame.image.load('yellow.png').convert())
notes.append(pygame.image.load('blue.png').convert())
notes.append(pygame.image.load('orange.png').convert())


noteImg = notes[random.randint(0, 4)]

def note(x,y):
    gameDisplay.blit(noteImg, (x,y))

x =  (0)
y = (display_height-64)

""""
base_font = pygame.font.Font(None, 32)
user_text = ''
  
input_rect = pygame.Rect(250, 288, 140, 32)
  
color_active = pygame.Color('lightskyblue3')
  
color_passive = pygame.Color('gray35')
color = color_passive
  
active = False

notEnter = False;

while not notEnter:
    for event in pygame.event.get():
  
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN and active == True:
  

            if event.key == pygame.K_BACKSPACE:
  
                user_text = user_text[:-1]

            else:
                user_text += event.unicode

      

    gameDisplay.fill(white)
  
    if active:
        color = color_active
    else:
        color = color_passive
          

    pygame.draw.rect(gameDisplay, color, input_rect)
  
    text_surface = base_font.render(user_text, True, white)
    
    gameDisplay.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    input_rect.w = max(100, text_surface.get_width()+10)
      
    pygame.display.flip()
      
    clock.tick(60)
"""
fail = True;
switch = False
temp = gameDisplay.copy()
while not end:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end = True

        
        
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                end = True;
            
            elif event.key == pygame.K_PERIOD:
                
                if state == 0:
                    inputString += "."
                    fail = False
                    state = -1
                elif state == -1:
                    end = True
                else:
                    inputString += "."
                    exit()
                

            elif event.key == pygame.K_SPACE:

                if switch == False:
                    temp = gameDisplay.copy()
                    drawDFA(state);
                else:
                    gameDisplay.blit(temp, (0, 0));

                switch = not switch
                


            elif event.key == pygame.K_g or event.key == pygame.K_r or event.key == pygame.K_y or event.key == pygame.K_b or event.key == pygame.K_o:
                if len(displayPage) == count:
                    if y == 0:

                        

                        if event.key == pygame.K_g:
                            noteImg = notes[0]
                            inputString += "g"

                            #ascendings
                            if state == 0:
                                state = 0
                                prevState = 0;
                            elif state == 1:
                                state = 0
                                prevState = 1
                            elif state == 2:
                                state = 0
                                prevState = 2
                            elif state == 3:
                                state = 0
                                prevState = 3
                            elif state == 4:
                                state = 0
                                prevState = 4

                            #descendings
                            elif state == 8:
                                state = 0
                                prevState = 8
                            
                            else:
                                exit()

                        elif event.key == pygame.K_r:
                            noteImg = notes[1]
                            inputString += "r"

                            if state == 0:
                                state = 1
                                prevState = 0;

                            #desc
                            elif state == 7:
                                state = 8
                                prevState = 7
                            else:
                                exit()

                        elif event.key == pygame.K_y:
                            noteImg = notes[2]
                            inputString += "y"

                            if state == 1:
                                state = 2
                                prevState = 1;

                            #desc
                            elif state == 0:
                                state = 7
                                prevState = 0
                            #desc
                            elif state == 6:
                                state = 7
                                prevState = 6
                            else:
                                exit()

                        elif event.key == pygame.K_b:
                            noteImg = notes[3]
                            inputString += "b"

                            if state == 2:
                                state = 3
                                prevState = 2;

                            #desc
                            elif state == 0:
                                state = 6
                                prevState = 0
                            #desc
                            elif state == 5:
                                state = 6
                                prevState = 5
                            else:
                                exit()

                        elif event.key == pygame.K_o:
                            noteImg = notes[4]
                            inputString += "o"

                            if state == 3:
                                state = 4
                                prevState = 3;

                            #desc
                            elif state == 0:
                                state = 5
                                prevState = 0
                            else:
                                exit()

                        note(x,y)
                        displayPage.append(gameDisplay.copy())
                        count +=1
                        gameDisplay.fill(black)
                        y = display_height-64
                        
                    else:
                        if event.key == pygame.K_g:
                            noteImg = notes[0]
                            inputString += "g"

                            if state == 0:
                                state = 0
                                prevState = 0;
                            elif state == 1:
                                state = 0
                                prevState = 1
                            elif state == 2:
                                state = 0
                                prevState = 2
                            elif state == 3:
                                state = 0
                                prevState = 3
                            elif state == 4:
                                state = 0
                                prevState = 4

                            #descendings
                            elif state == 8:
                                state = 0
                                prevState = 8
                            
                            else:
                                exit()

                        elif event.key == pygame.K_r:
                            noteImg = notes[1]
                            inputString += "r"

                            if state == 0:
                                state = 1
                                prevState = 0;
                            #desc
                            elif state == 7:
                                state = 8
                                prevState = 7
                            else:
                                exit()
                            

                        elif event.key == pygame.K_y:
                            noteImg = notes[2]
                            inputString += "y"

                            if state == 1:
                                state = 2
                                prevState = 1;

                            #desc
                            elif state == 0:
                                state = 7
                                prevState = 0
                            #desc
                            elif state == 6:
                                state = 7
                                prevState = 6
                            else:
                                exit()

                        elif event.key == pygame.K_b:
                            noteImg = notes[3]
                            inputString += "b"

                            if state == 2:
                                state = 3
                                prevState = 2;

                            #desc
                            elif state == 0:
                                state = 6
                                prevState = 0
                            #desc
                            elif state == 5:
                                state = 6
                                prevState = 5
                            else:
                                exit()
                            
                        elif event.key == pygame.K_o:
                            noteImg = notes[4]
                            inputString += "o"

                            if state == 3:
                                state = 4
                                prevState = 3;

                            #desc
                            elif state == 0:
                                state = 5
                                prevState = 0
                            else:
                                exit()
                            
                        note(x,y)
                        y -= 64
                        
                else:
                        count+=1;
                        gameDisplay.blit(displayPage[count], (0, 0))
                        if len(displayPage)-1 == count:
                            displayPage.pop(-1)
                            #count-=1
                
            if event.key == pygame.K_UP:

                if len(displayPage) != count:
                    count+=1
                    gameDisplay.blit(displayPage[count], (0, 0))
                    if len(displayPage)-1 == count:
                        displayPage.pop(-1)
                        #count-=1
                        



            elif event.key == pygame.K_DOWN:

                if len(displayPage) == count and count != 0:
                    displayPage.append(gameDisplay.copy());

                if count >= 1:
                    count-=1
                    gameDisplay.blit(displayPage[count], (0,0))


    pygame.display.update()
      
    clock.tick(60)


if fail != True:
    if switch == True:
        displayPage.append(temp)
    else:
        displayPage.append(gameDisplay)
    
    im = PIL.Image.new(mode="RGB", size=(640, 640*len(displayPage)))
    i = 1

    for image in displayPage:
        pil_string_image = pygame.image.tostring(image, "RGB", False)
        pli_image = PIL.Image.frombytes('RGB', image.get_size(), pil_string_image, 'raw')
        temp_io = io.BytesIO()
        pli_image.save(temp_io, format="JPEG")
        extrema = pli_image.convert("L").getextrema()
        if extrema[0] != extrema[1]:
            im.paste(pli_image, (0, 640*len(displayPage)-640*i))
        else:
            im = im.crop((0, 640, 640, 640*len(displayPage)))
        
        i+=1
    if inputString != "" and inputString != ".":
        im.save("out.jpg")
else:
    exit()


gameDisplay.fill(black)

font = pygame.font.Font('freesansbold.ttf', 32)
font1 = pygame.font.Font('freesansbold.ttf', 15)

text = font.render('String Accepted', True, white, black)
textRect = text.get_rect()
textRect.center = (320, 320)


text1 = font1.render('"'+ inputString + '"', True, green, black)
textRect1 = text.get_rect()
textRect1.center = (320, 360)

gameDisplay.blit(text, textRect)
gameDisplay.blit(text1, textRect1)

pygame.display.update()

time.sleep(5)

pygame.quit()
quit()