def line_up(name, number):
    value=0
    if number%10==1:
        if number%100==11:
            value = 'th'
        else:
            value='st'
    elif number%10==2:
        if number%100==12:
            value = 'th'
        else:
            value='nd'
    elif number%10==3:
        if number%100==13:
            value = 'th'
        else:
            value='rd'
    else:
        value='th'
        
    return f"{name}, you are the {number}{value} customer we serve today. Thank you!"