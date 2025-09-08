def flatten(iterable):
    final=[]
    for i in iterable:
        if isinstance(i,list):
            final.extend(flatten(i))
        else:
            final.append(i)
    return [i for i in final if i!=None]
