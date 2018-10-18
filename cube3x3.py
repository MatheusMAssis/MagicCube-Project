import numpy as np
import random as rd

#--- auxiliar functions ---#

def cube_faces(arr):
    faces_dic = {}
    faces_dic['U'] = [arr[ 0], arr[ 1], arr[ 2], 
                      arr[ 5], arr[ 8], arr[ 7], 
                      arr[ 6], arr[ 3], arr[ 4]]
    faces_dic['L'] = [arr[ 9], arr[10], arr[11],
                      arr[23], arr[35], arr[34],
                      arr[33], arr[21], arr[22]]
    faces_dic['F'] = [arr[12], arr[13], arr[14],
                      arr[26], arr[38], arr[37],
                      arr[36], arr[24], arr[25]]
    faces_dic['R'] = [arr[15], arr[16], arr[17],
                      arr[29], arr[41], arr[40],
                      arr[39], arr[27], arr[28]]
    faces_dic['B'] = [arr[18], arr[19], arr[20],
                      arr[32], arr[44], arr[43],
                      arr[42], arr[30], arr[31]]
    faces_dic['D'] = [arr[45], arr[46], arr[47],
                      arr[50], arr[53], arr[52],
                      arr[51], arr[48], arr[49]]
    return faces_dic

def faces_to_array(dic, arr):
    arr[ 0: 9] = [dic['U'][0], dic['U'][1], dic['U'][2],
                  dic['U'][7], dic['U'][8], dic['U'][3],
                  dic['U'][6], dic['U'][5], dic['U'][4]]
    arr[ 9:21] = [dic['L'][0], dic['L'][1], dic['L'][2],
                  dic['F'][0], dic['F'][1], dic['F'][2],
                  dic['R'][0], dic['R'][1], dic['R'][2],
                  dic['B'][0], dic['B'][1], dic['B'][2]]
    arr[21:33] = [dic['L'][7], dic['L'][8], dic['L'][3],
                  dic['F'][7], dic['F'][8], dic['F'][3],
                  dic['R'][7], dic['R'][8], dic['R'][3],
                  dic['B'][7], dic['B'][8], dic['B'][3]]
    arr[33:45] = [dic['L'][6], dic['L'][5], dic['L'][4],
                  dic['F'][6], dic['F'][5], dic['F'][4],
                  dic['R'][6], dic['R'][5], dic['R'][4],
                  dic['B'][6], dic['B'][5], dic['B'][4]]
    arr[45:54] = [dic['D'][0], dic['D'][1], dic['D'][2],
                  dic['D'][7], dic['D'][8], dic['D'][3],
                  dic['D'][6], dic['D'][5], dic['D'][4]]
    return dic, arr

def turn_face(dic, movement):
    if len(movement) == 1:
        [aux1, aux2]       = dic[movement][6:8]
        dic[movement][2:8] = dic[movement][0:6]
        dic[movement][0:2] =       [aux1, aux2]
    else:
        [aux1, aux2]          = dic[movement[0]][0:2]
        dic[movement[0]][0:6] = dic[movement[0]][2:8]
        dic[movement[0]][6:8] =          [aux1, aux2]
    return dic

def change(n):
    color_dict = {0: 'W', 1: 'O', 2: 'G', 3: 'R', 4: 'B', 5: 'Y'}
    return color_dict[n]


class cube3:
    
    def __init__(self):
        self.state = np.array([0]*9 + ([1]*3 + [2]*3 + [3]*3 + [4] * 3)*3 + [5]*9)
        self.dic   = cube_faces(self.state)
    
    def show(self):
        up, down, front, back, right, left = [], [], [], [], [], []
        
        for i in range(len(self.state)):
            color = change(self.state[i])
            if i < 9:
                up.append(color)
            elif i < 12 or (i >= 21 and i < 24) or (i >= 33 and i < 36):
                left.append(color)
            elif i < 15 or (i >= 24 and i < 27) or (i >= 36 and i < 39):
                front.append(color)
            elif i < 18 or (i >= 27 and i < 30) or (i >= 39 and i < 42):
                right.append(color)
            elif i < 21 or (i >= 30 and i < 33) or (i >= 42 and i < 45):
                back.append(color)
            else:
                down.append(color)
                
        print('up    :',    up[:3], '\n', '      ',    up[3:6], '\n', '      ',    up[6:])
        print('front :', front[:3], '\n', '      ', front[3:6], '\n', '      ', front[6:])
        print('left  :',  left[:3], '\n', '      ',  left[3:6], '\n', '      ',  left[6:])
        print('right :', right[:3], '\n', '      ', right[3:6], '\n', '      ', right[6:])
        print('back  :',  back[:3], '\n', '      ',  back[3:6], '\n', '      ',  back[6:])
        print('down  :',  down[:3], '\n', '      ',  down[3:6], '\n', '      ',  down[6:])
                
    
    def move(self, movement):
        self.dic = turn_face(self.dic, movement)
        
        #--- up ---#
            
        #clockwise
        if movement == 'U':
            [aux1, aux2, aux3] = self.dic['L'][0:3]
            self.dic['L'][0:3] = self.dic['F'][0:3]
            self.dic['F'][0:3] = self.dic['R'][0:3]
            self.dic['R'][0:3] = self.dic['B'][0:3]
            self.dic['B'][0:3] = [aux1, aux2, aux3]
                        
        #counter clockwise
        elif movement == 'Ui': 
            [aux1, aux2, aux3] = self.dic['B'][0:3]
            self.dic['B'][0:3] = self.dic['R'][0:3]
            self.dic['R'][0:3] = self.dic['F'][0:3]
            self.dic['F'][0:3] = self.dic['L'][0:3]
            self.dic['L'][0:3] = [aux1, aux2, aux3]
            
        #--- down ---#
        
        #clockwise
        elif movement == 'D':
            [aux1, aux2, aux3] = self.dic['B'][4:7]
            self.dic['B'][4:7] = self.dic['R'][4:7]
            self.dic['R'][4:7] = self.dic['F'][4:7]
            self.dic['F'][4:7] = self.dic['L'][4:7]
            self.dic['L'][4:7] = [aux1, aux2, aux3]
        
        #counter clockwise
        elif movement == 'Di':
            [aux1, aux2, aux3] = self.dic['L'][4:7]
            self.dic['L'][4:7] = self.dic['F'][4:7]
            self.dic['F'][4:7] = self.dic['R'][4:7]
            self.dic['R'][4:7] = self.dic['B'][4:7]
            self.dic['B'][4:7] = [aux1, aux2, aux3]
            
        #--- left ---#
        
        #clockwise
        elif movement == 'L':
            [aux1, aux2, aux3]                   = self.dic['B'][2:5]
            self.dic['B'][4], self.dic['B'][2:4] = self.dic['D'][0], self.dic['D'][6:8]
            self.dic['D'][0], self.dic['D'][6:8] = self.dic['F'][0], self.dic['F'][6:8]
            self.dic['F'][0], self.dic['F'][6:8] = self.dic['U'][0], self.dic['U'][6:8]
            self.dic['U'][0], self.dic['U'][6:8] = aux3, [aux1, aux2]
        
        #counter clockwise
        elif movement == 'Li':
            [aux1, aux2, aux3]                   = self.dic['F'][:1] + self.dic['F'][6:8]
            self.dic['F'][0], self.dic['F'][6:8] = self.dic['D'][0], self.dic['D'][6:8]
            self.dic['D'][0], self.dic['D'][6:8] = self.dic['B'][4], self.dic['B'][2:4]
            self.dic['B'][4], self.dic['B'][2:4] = self.dic['U'][0], self.dic['U'][6:8]
            self.dic['U'][0], self.dic['U'][6:8] = aux1, [aux2, aux3]
            
        #--- right ---#
        
        #clockwise
        elif movement == 'R':
            [aux1, aux2, aux3]                   = self.dic['F'][2:5]
            self.dic['F'][2:5]                   = self.dic['D'][2:5]
            self.dic['D'][4], self.dic['D'][2:4] = self.dic['B'][0], self.dic['B'][6:8]
            self.dic['B'][0], self.dic['B'][6:8] = self.dic['U'][4], self.dic['U'][2:4]
            self.dic['U'][2:5]                   = [aux1, aux2, aux3]
        
        #counter clockwise
        elif movement == 'Ri':
            [aux1, aux2, aux3]                   = self.dic['U'][2:5]
            self.dic['U'][4], self.dic['U'][2:4] = self.dic['B'][0], self.dic['B'][6:8]
            self.dic['B'][0], self.dic['B'][6:8] = self.dic['D'][4], self.dic['D'][2:4]
            self.dic['D'][2:5]                   = self.dic['F'][2:5]
            self.dic['F'][2:5]                   = [aux1, aux2, aux3]
            
        #--- front ---#
        
        #clockwise
        elif movement == 'F':
            [aux1, aux2, aux3]                   = self.dic['L'][2:5]
            self.dic['L'][2:5]                   = self.dic['D'][0:3]
            self.dic['D'][2], self.dic['D'][0:2] = self.dic['R'][0], self.dic['R'][6:8]
            self.dic['R'][0], self.dic['R'][6:8] = self.dic['U'][6], self.dic['U'][4:6]
            self.dic['U'][4:7]                   = [aux1, aux2, aux3]
            
        #counter clockwise
        elif movement == 'Fi':
            [aux1, aux2, aux3]                   = self.dic['L'][2:5]
            self.dic['L'][2:5]                   = self.dic['U'][4:7]
            self.dic['U'][6], self.dic['U'][4:6] = self.dic['R'][0], self.dic['R'][6:8]
            self.dic['R'][0], self.dic['R'][6:8] = self.dic['D'][2], self.dic['D'][0:2]
            self.dic['D'][0:3]                   = [aux1, aux2, aux3]
            
        #--- back ---#
        
        #clockwise
        elif movement == 'B':
            [aux1, aux2, aux3]                   = self.dic['U'][0:3]
            self.dic['U'][0:3]                   = self.dic['R'][2:5]
            self.dic['R'][2:5]                   = self.dic['D'][4:7]
            self.dic['D'][6], self.dic['D'][4:6] = self.dic['L'][0], self.dic['L'][6:8]
            self.dic['L'][0], self.dic['L'][6:8] = aux3, [aux1, aux2]
            
        #counter clockwise
        elif movement == 'Bi':
            [aux1, aux2, aux3]                   = self.dic['U'][0:3]
            self.dic['U'][2], self.dic['U'][0:2] = self.dic['L'][0], self.dic['L'][6:8]
            self.dic['L'][0], self.dic['L'][6:8] = self.dic['D'][6], self.dic['D'][4:6]
            self.dic['D'][4:7]                   = self.dic['R'][2:5]
            self.dic['R'][2:5]                   = [aux1, aux2, aux3]
            
        #updating dic and state with the correct changes
        self.dic, self.state = faces_to_array(self.dic, self.state)
    
    def scramble(self, n):
        movement_list = ['U', 'Ui', 'D', 'Di', 'L', 'Li', 'R', 'Ri', 'F', 'Fi', 'B', 'Bi']
        scramble_list = []
        for i in range(n):
            movement = rd.choice(movement_list)
            scramble_list.append(movement)
            self.move(movement)
        self.show()
        return scramble_list
