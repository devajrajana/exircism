def find_anagrams(word, candidates):
    anagrams=[]
    for i in candidates:
        if sorted(i.lower())== sorted(word.lower()) and i.lower()!=word.lower():
            anagrams.append(i)
    return anagrams
