'''     RUBIK's CUBE

Rubik's cube interface, with a
scramble  mode to  start  your
cube in a random state     '''

import Cube3 as c
import Piece as p
import Button as b
start_game = False


#--- starting cube and scrambling it ---#
c3 = c.Cube3()
scramble_list = c3.scramble(15)
 

#--- plotting cube on the screen ---#
faces_list = c3.show()
arr = []
t = 0

#up
for j in range(3):
    for i in range(3):
        arr.append(p.Piece(200 + i*50, 55 + j*50, faces_list[0][t]))
        t += 1
t = 0

#left - front - right - back
for k in range(4):
    for j in range(3):
        for i in range(3):
            arr.append(p.Piece(50 + k*150 + i*50, 205 + j*50, faces_list[k + 1][t]))
            t += 1
    t = 0

#down
for j in range(3):
    for i in range(3):
        arr.append(p.Piece(200 + i*50, 355 + j*50, faces_list[5][t]))
        t += 1
t = 0


#--- creating buttons to realize movements ---#
movement_list = ['U', 'Ui', 'D', 'Di', 'L', 'Li', 'R', 'Ri', 'F', 'Fi', 'B', 'Bi']
buttons = [b.Button(50*(1+i), 0, movement_list[i]) for i in range(len(movement_list))]


def setup():
    size(700, 550)
    

def draw():
    global scramble_list, buttons, start_game
    background(0)
    
    if not start_game:
        textSize(40)
        textAlign(CENTER)
        text('RUBIKS CUBE', width/2, height/2 - 10)
        textSize(16)
        text('Matheus de Moncada Assis', width/2, height/2 + 15)
        text('CLICK TO START', width/2, height - 40)
        if mousePressed:
            delay(20)
            start_game = True
    else:
        
        #--- updating the movements on the cube ---#
        faces_list = c3.show()
        arr = []
        t = 0
        
        #up
        for j in range(3):
            for i in range(3):
                arr.append(p.Piece(200 + i*50, 55 + j*50, faces_list[0][t]))
                t += 1
        t = 0
        
        #left - front - right - back
        for k in range(4):
            for j in range(3):
                for i in range(3):
                    arr.append(p.Piece(50 + k*150 + i*50, 205 + j*50, faces_list[k + 1][t]))
                    t += 1
            t = 0
        
        #down
        for j in range(3):
            for i in range(3):
                arr.append(p.Piece(200 + i*50, 355 + j*50, faces_list[5][t]))
                t += 1
        t = 0
    
    
        #--- drawing pieces, screen and buttons ---#
        for i in arr:
            i.show()
        
        for i in range(5):
            strokeWeight(6)
            stroke(0)
            line(50 + i*600/4, 0, 50 + i*600/4, 550)
            line(0 , 55 + i*450/3, 700, 55 + i*450/3)
        
        for i in buttons:
            i.show(i.col)
            i.touch(c3)
        
        textSize(13)
        textAlign(CENTER, CENTER)
        fill(0)
        text('UP', 275, 125)
        text('LEFT', 125, 275)
        text('FRONT', 275, 275)
        text('RIGHT', 425, 275)
        text('BACK', 575, 275)
        text('DOWN', 275, 425)
    
        fill(255)
        textSize(15)
        text('SCRAMBLE: {}'.format(scramble_list), 350, 520)
