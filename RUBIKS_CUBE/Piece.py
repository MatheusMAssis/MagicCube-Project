class Piece:
    
    def __init__(self, x, y, n):
        self.x = x
        self.y = y
        self.n = n
    
    def show(self):
        if self.n == 'W':
            fill(230)
        elif self.n == 'O':
            fill(255,165,0)
        elif self.n == 'G':
            fill(124,252,0)
        elif self.n == 'R':
            fill(255,0,0)
        elif self.n == 'B':
            fill(65,105,225)
        elif self.n == 'Y':
            fill(255,255,0)
        strokeWeight(1)
        stroke(0)
        rect(self.x, self.y, 50, 50)
