

class Color():
    def __init__(self, hexa):
        self.hex = hexa
        self.rgb = tuple([int(hexa[i:i+2], 16) for i in (0,2,4)])
        self.luminance = self.luminance()
        
    def luminance(self):
        [r,g,b] = [self.get_value(channel) for channel in self.rgb]
        return 0.2126 * r + 0.7152 * g + 0.0722 * b
        
    def get_value(self, num):
        x = num/255
        if x <= 0.03928:
            return x/12.92
        else:
            return ((x+0.055)/1.055)**2.4
        
    def __str__(self):
        return '#' + str.upper(self.hex)
        
        
        