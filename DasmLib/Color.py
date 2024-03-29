class HSV():
    hue = 0
    saturation = 0
    value = 0
    
    def __init__(self, h, s, v):
        self.hue = h
        self.saturation = s
        self.value = v

class RGB():
    red = 0
    green = 0
    blue = 0
    
    def __init__(self, r, g, b):
        self.red = r
        self.green = g
        self.blue = b
        
    def __repr__(self):
        return repr({"R": self.red, "G": self.green, "B": self.blue})
        
    def toHSV(self):
        r = self.red / 255
        g = self.green / 255
        b = self.blue / 255
        
        Cmax = max(r, g, b)
        Cmin = min(r, g, b)
        
        delta = Cmax - Cmin
        
        # H
        if delta == 0:
            H = 0
        elif Cmax == r:
            H = 60*(((g-b) / delta) % 6)
        elif Cmax == g:
            H = 60*(((b-r) / delta) + 2)
        elif Cmax == b:
            H = 60*(((r-g) / delta) + 4) 
        
        # S
        if Cmax == 0:
            S = 0
        else:
            S = delta / Cmax
        
        # V
        V = Cmax
        
        return HSV(round(H, 0),round(S*100, 2),round(V*100, 2))