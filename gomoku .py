from pygame import *

''' UI & deep learning & rules '''



#import packages
import pygame 
from pygame.locals import *


#about screen
Screen= width, height = 1440,960


#init the game
pygame.init()

#setup screen
Screen = pygame.display.set_mode(Screen)
pygame.display.set_caption("Gomoku")

#define colors
BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = ( 0, 255, 0)
BLUE = ( 0, 0, 255)
Screen.fill(WHITE)

#background photo
boardImage = pygame.image.load('boardphoto.jpg')
Screen.blit(boardImage, (0,0))

#pygame.draw.line(Screen, Color, Start_position, End_position, Width)
#Draw the board
for i in range (50):
    pygame.draw.line(Screen, BLACK, [25*i, 0], [25*i,950], 1)
    pygame.draw.line(Screen, BLACK, [0,25*i], [1225, 25*i], 1)
pygame.display.update()


#计算线的交点 compute the line intersection
#def line_intersection(line_1, line_2):


#所有的空的交点
empty_intersection=[]
for i in range(50):
    for a in range(39):
        empty_intersection.append([25*i,25*a])

#print(empty_intersection)

n=0 #n 用于判断谁改下了 当n为单数时 后手下子  n为偶数时 先手下子
all_red=[]
all_green=[]

time_to_quit = False
while not time_to_quit:
    for new_event in pygame.event.get():
        if new_event.type == pygame.QUIT:
            time_to_quit = True
        if new_event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            #print(pos)
            pos_position = [round(x / 25) for x in pos]
            #print(pos_position)
            intersection_position = [pos_position[i] * 25 for i in range(len(pos_position))]
            #print(intersection_position)
            if intersection_position in empty_intersection:
                if n%2 == 0:
                    n+=1
                    pygame.draw.circle(Screen, RED, intersection_position, 7, 0)
                    all_red.append(intersection_position)
                    empty_intersection.remove(intersection_position)
                elif n%2 == 1:
                    n+=1
                    pygame.draw.circle(Screen, GREEN, intersection_position, 7, 0)
                    all_green.append(intersection_position)
                    empty_intersection.remove(intersection_position)
    
    #获取鼠标位置 get mouse position          
    x, y = pygame.mouse.get_pos()
    #print(x,y)
    

pygame.quit()

"""
p1 = sorted(empty__intersection.append(pos))
p2 = sorted(empty__intersection.append(pos), key=lambda x: x[1])
px = p1.index(pos)
py = p2.index(pos)
first_x = p1[px-1]
second_x = p1[px+1]
first_y = p2[py-1]
second-y = p2[py+1]
"""
