class Button:
    
    def __init__(self, x, y, move):
        self.x = x
        self.y = y
        self.move = move
        self.col = 255
        
    def show(self, col):
        fill(col)
        rect(self.x, self.y, 50, 50)
        textSize(15)
        fill(0)
        textAlign(CENTER)
        text(self.move, self.x + 25, self.y + 30)
        

    #--- touch the button to realize movements on the cube ---#
    def touch(self, cube):
        if mousePressed:
            delay(10)
            if (mouseX >= self.x and mouseX <= self.x + 50) and (mouseY >= self.y and mouseY <= self.y + 50):
                self.col = 162
                cube.move(self.move)
            else:
                self.col = 255
        else:
            self.col = 255
