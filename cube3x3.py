import numpy as np

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
    arr[45:54] = [dic['D'][0], dic['D'][5], dic['D'][2],
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

  
class cube3:
    
    def __init__(self):
        self.state = np.array([0]*9 + ([1]*3 + [2]*3 + [3]*3 + [4] * 3)*3 + [5]*9)
        self.dic   = cube_faces(self.state)
        self.color_dict = {0: 'W',
                           1: 'O',
                           2: 'G',
                           3: 'R',
                           4: 'B',
                           5: 'Y'}
    
    def show(self):
        for i in self.state:
            ...
    
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
       
        #updating dic and state with the correct changes
        self.dic, self.state = faces_to_array(self.dic, self.state)   
