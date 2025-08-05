def is_isogram(string):
    l=[]
    for i in string.lower():
        if i.isalpha():
            if i not in l:
                l.append(i)
            else:
                return False
    return True
