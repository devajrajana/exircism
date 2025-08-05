COLORS ={'black': 0,'brown': 1,'red': 2,'orange': 3,'yellow': 4,'green': 5,'blue': 6,'violet': 7,'grey': 8,'white': 9}

def label(colors):
    resistance = (COLORS[colors[0]]*10+COLORS[colors[1]])*(10**COLORS[colors[2]])
    if len(str(resistance))>9 and str(resistance)[-9:]=='000000000':
        return f"{str(resistance)[0:-9]} gigaohms"
    elif len(str(resistance))>6 and str(resistance)[-6:]=='000000':
        return f"{str(resistance)[0:-6]} megaohms" 
    elif len(str(resistance))>3 and str(resistance)[-3:]=='000':
        return f"{str(resistance)[0:-3]} kiloohms"
    else:
        return f"{resistance} ohms"
    
    