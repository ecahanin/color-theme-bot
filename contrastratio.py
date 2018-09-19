
def contrast_ratio(color1, color2, decimal_precision=1):
    return round((color1.luminance + 0.05)/(color2.luminance + 0.05), decimal_precision)


