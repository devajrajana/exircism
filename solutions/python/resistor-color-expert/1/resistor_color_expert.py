COLORS =['black','brown','red','orange','yellow','green','blue','violet','grey','white']
TOLERENCE= {'grey':0.05,'violet':0.1,'blue': 0.25,'green':0.5,'brown':1,'red': 2,'gold':5,'silver': 10}
def resistor_label(colors):
    if len(colors)==1:
        resistance = COLORS.index(colors[0])
        return f'{str(resistance)} ohms'
    elif len(colors)==4:
        resistance = (COLORS.index(colors[0])*10+COLORS.index(colors[1]))*(10**COLORS.index(colors[2]))
        tolerance = TOLERENCE[colors[3]]
    elif len(colors)==5:
        resistance = (COLORS.index(colors[0])*100+COLORS.index(colors[1])*10+COLORS.index(colors[2]))*(10**COLORS.index(colors[3]))
        tolerance = TOLERENCE[colors[4]]
        
    #converting resistance and tolerance into strings
    if resistance < 1000:
        return f"{resistance} ohms ±{tolerance}%"
    elif resistance < 1000000:
        return f"{(int(v) if (v := resistance / 1000) % 1 == 0 else v)} kiloohms ±{tolerance}%"
    else:
        return f"{resistance/1000000} megaohms ±{tolerance}%"
        
    
