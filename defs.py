class Color:
    r:int = 0
    g:int = 0
    b:int = 0
    def __init__(self, col: tuple[int, int, int]):
        self.r = col[0]
        self.g = col[0]
        self.b = col[0]
    
    def __add__(self, c2):
        return Color((self.r + c2.r, self.g + c2.g, self.b + c2.b))
    
    def __iadd__(self, c2):
        self.r += c2.r
        self.g += c2.g
        self.b += c2.b
        return self
    
    def __truediv__(self, k:int):
        r = self.r/k
        g = self.g/k
        b = self.b/k
        return Color((int(r), int(g), int(b)))
    
    def distsq(self, col) -> int:
        return (self.r - col.r)*(self.r - col.r) + (self.g - col.g)*(self.g - col.g) + (self.b - col.b)*(self.b - col.b)
