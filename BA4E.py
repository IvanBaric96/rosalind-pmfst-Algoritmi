def Expand(peptides):
    novi=[]
    for peptide in peptides:
        for masa in mase:
            novi.append(peptide+[masa])
    return novi
        
def Cyclospectrum(peptide):
    masa_cijelog_peptida=sum(peptide)
    niz=[0,masa_cijelog_peptida]

    tmp=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptid=tmp[j:(j+i)]
            niz.append(sum(subpeptid))
    niz.sort()
    return niz

def Consistent(peptide):
    theoretical_spectrum=[0,sum(peptide)]
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)-i+1):
            subpeptid=peptide[j:(j+i)]
            theoretical_spectrum.append(sum(subpeptid))

    rez=[]
    for el in theoretical_spectrum:
        if el in Spectrum:
            rez.append(True)
        else:
            rez.append(False)
    return rez

def CyclopeptideSequencing(Spectrum):
    peptides=[[]]
    rez=[]
    while len(peptides)>0:
        peptides=Expand(peptides)
        for peptide in peptides:
            if sum(peptide)==Spectrum[-1]:
                if Cyclospectrum(peptide)==Spectrum:
                    rez.append(peptide)
                peptides=[p for p in peptides if p!=peptide]
            elif False in Consistent(peptide):
                peptides=[p for p in peptides if p!=peptide]
    return rez

f=[0,71,71,87,97,101,103,113,115,156,158,168,172,184,186,186,218,255,255,257,259,269,283,289,289,299,326,328,356,370,370,386,402,404,415,427,441,441,455,473,475,512,517,528,542,544,556,558,572,583,588,625,627,645,659,659,673,685,696,698,714,730,730,744,772,774,801,811,811,817,831,841,843,845,845,882,914,914,916,928,932,942,944,985,987,997,999,1003,1013,1029,1029,1100]
Spectrum=[int(el) for el in f]
mase=[57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
rez=CyclopeptideSequencing(Spectrum)
for el in rez:
    print("-".join(map(str,el)),end=" ")