def to_rna(dna_strand):
    final=''
    for i in dna_strand:
        if i=='G':
            final+="C"
        elif i=='C':
            final+="G"
        elif i=='T':
            final+="A"
        elif i=='A':
            final+="U"
        
    return final
