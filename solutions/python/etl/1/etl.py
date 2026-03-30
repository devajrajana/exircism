def transform(legacy_data):
    data={}
    for score,letter in legacy_data.items():
        for i in letter:
            data[i.lower()]=score
    return data
