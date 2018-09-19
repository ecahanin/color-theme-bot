from itertools import combinations
from contrastratio import contrast_ratio


class Theme():
    def __init__(self, name, colors = []):
        self.name = name
        self.colors = colors
        self.good = []
        self.large_font = []
        self.avoid = []
        self.check_ratios()
        
    def check_ratios(self):
        for pair in combinations(self.colors, 2):
            (light, dark) = sorted(pair, key=lambda x: x.luminance, reverse=True)
            ratio = contrast_ratio(light, dark)
            color_pair = (light, dark, ratio)
            if ratio >= 4.5:
                self.good.append(color_pair)
            elif ratio >= 3:
                self.large_font.append(color_pair)
            else:
                self.avoid.append(color_pair)
    
    
            
            
        
        
            
        
        