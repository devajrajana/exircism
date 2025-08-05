def score(x, y):
    radius=(x**2+y**2)**0.5
    if radius<=1:
        s=10
    elif radius<=5:
        s=5
    elif radius<=10:
        s=1
    else:
        s=0
    return s