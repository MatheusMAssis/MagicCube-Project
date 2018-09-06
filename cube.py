import numpy as np

#--- auxiliar function ---#

def change(n):
    color_dict = {0: 'white',
                  1: 'orange',
                  2: 'green',
                  3: 'red',
                  4: 'blue',
                  5: 'yellow'}
    return color_dict[n]

#--- cube class (in this case, a 2x2x2) ---#

class cube:
    
    #--- initializing the cube in it's solved form ---#
    
    def __init__(self):
        self.state = np.array([0, 0, 0, 0, #up
                               1, 1, 2, 2, 
                               3, 3, 4, 4,
                               1, 1, 2, 2,
                               3, 3, 4, 4,
                               5, 5, 5, 5]) #down
    
    #--- printing the colors of cube faces ---#
    
    def show(self):
        up, down, front, back, right, left = [], [], [], [], [], []
        
        for i in range(len(self.state)):
            if i < 4:
                color = change(self.state[i])
                up.append(color)
            elif i < 6 or (i < 14 and i >= 12):
                color = change(self.state[i])
                left.append(color)
            elif i < 8 or (i < 16 and i >= 14):
                color = change(self.state[i])
                front.append(color)
            elif i < 10 or (i < 18 and i >= 16):
                color = change(self.state[i])
                right.append(color)
            elif i < 12 or (i < 20 and i >= 18):
                color = change(self.state[i])
                back.append(color)
            else:
                color = change(self.state[i])
                down.append(color)
        
        print('up:', up)
        print('down:', down)
        print('front:', front)
        print('back:', back)
        print('right:', right)
        print('left:', left)
    
    #--- defining moves in clock or anticlock wise ---#
    
    def move(self, movement, direction):
        
        
    #--- up ---#
        #clock
        if movement == 'u' and direction == 'c':
            
            #up
            aux1, aux2 = self.state[0], self.state[1]
            self.state[0], self.state[1] = self.state[2], aux1
            self.state[2], self.state[3] = self.state[3], aux2
            
            #lateral
            [aux1, aux2] = self.state[4:6]
            self.state[4:10] = self.state[6:12]
            self.state[10:12] = [aux1, aux2]
        
        #anticlock
        elif movement == 'u' and direction == 'ac':
                
            #up
            aux1, aux2 = self.state[0], self.state[2]
            self.state[0], self.state[1] = self.state[1], self.state[3]
            self.state[2], self.state[3] = aux1, aux2
            
            #lateral
            [aux1, aux2] = self.state[10:12]
            self.state[6:12] = self.state[4:10]
            self.state[4:6] =  [aux1, aux2]
        
    #--- down ---#
        elif movement == 'd' and direction == 'c':
            
            #down
            aux1, aux2 = self.state[20], self.state[21]
            self.state[20], self.state[21] = self.state[22], aux1
            self.state[22], self.state[23] = self.state[23], aux2
            
            #lateral
            [aux1, aux2] = self.state[18:20]
            self.state[14:20] = self.state[12:18]
            self.state[12:14] =  [aux1, aux2]
            
        elif movement == 'd' and direction == 'ac':
            
            #down
            aux1, aux2 = self.state[20], self.state[22]
            self.state[20], self.state[21] = self.state[21], self.state[23]
            self.state[22], self.state[23] = aux1, aux2
            
            #lateral
            [aux1, aux2] = self.state[12:14]
            self.state[12:18] = self.state[14:20]
            self.state[18:20] = [aux1, aux2]
            
        elif movement == 'r' and direction == 'c':
            ...
            
        elif movement == 'r' and direction == 'ac':
            ...
            
        elif movement == 'l' and direction == 'c':
            ...
            
        elif movement == 'l' and direction == 'ac':
            ...
            
        elif movement == 'f' and direction == 'c':
            ...
            
        elif movement == 'f' and direction == 'ac':
            ...
            
        elif movement == 'b' and direction == 'c':
            ...
            
        elif movement == 'b' and direction == 'ac':
            ...
