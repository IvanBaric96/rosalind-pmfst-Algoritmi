def Expand(leaderboard):
    rez=[]
    for el in leaderboard:
        for elem in mase:
            rez.append(el+[elem])
    return rez      
    
def CycloSpectrum(peptide,integerMassTable):
    masa_cijelog_peptida=sum(peptide)

    niz=[0,masa_cijelog_peptida]

    tmp=peptide+peptide
    for i in range(1,len(peptide)):
        for j in range(0,len(peptide)):
            subpeptide=tmp[j:(j+i)]
            masa=sum(subpeptide)
            niz.append(masa)
    niz.sort()
    return niz

def Score(peptide,Spectrum):
    cycloSpectrum=CycloSpectrum(peptide,integerMassTable)

    unikati=set(cycloSpectrum+Spectrum)
    
    count=0
    for el in unikati:
        count+=min(Spectrum.count(el),cycloSpectrum.count(el))
    return count

def Cut(leaderboard,Spectrum,N):
    if len(leaderboard)<=N:
        return leaderboard
    
    D=dict()
    for i,peptide in enumerate(leaderboard):
        D[i]=Score(peptide,Spectrum)

    sortirano=sorted(D.values(),reverse=True)
    
    rez=[leaderboard[key] for key,value in D.items() if value>=sortirano[N-1]]
    return rez
    

def LeaderboardCyclopeptideSequencing(Spectrum,N):
    leaderboard=[[]]
    leaderPeptide=[]

    while len(leaderboard)>0:
        leaderboard=Expand(leaderboard)
        for peptide in leaderboard:
            if sum(peptide)==Spectrum[-1]:
                if Score(peptide,Spectrum)> Score(leaderPeptide,Spectrum):
                    leaderPeptide=peptide
            elif sum(peptide)>Spectrum[-1]:
                leaderboard=[p for p in leaderboard if p!=peptide]
        leaderboard=Cut(leaderboard,Spectrum,N)
    return leaderPeptide



N=368
f=[0,97,97,103,113,131,131,147,156,156,156,163,186,186,228,244,250,253,253,259,260,269,287,287,333,349,356,372,384,384,391,400,400,400,406,409,436,446,497,497,503,512,519,531,535,540,547,556,577,592,622,628,632,643,653,653,659,660,682,687,689,733,756,763,778,779,784,784,785,790,791,809,845,846,875,881,882,903,910,912,919,940,941,947,976,977,1013,1031,1032,1037,1038,1038,1043,1044,1059,1066,1089,1133,1135,1140,1162,1163,1169,1169,1179,1190,1194,1200,1230,1245,1266,1275,1282,1287,1291,1303,1310,1319,1325,1325,1376,1386,1413,1416,1422,1422,1422,1431,1438,1438,1466,1473,1489,1535,1535,1553,1562,1563,1569,1569,1572,1578,1594,1636,1636,1659,1666,1666,1666,1675,1691,1691,1709,1719,1725,1725,1822]
Spectrum=[int(el) for el in f]
mase= [57, 71, 87, 97, 99, 101, 103, 113, 114, 115, 128, 129, 131, 137, 147, 156, 163, 186]
integerMassTable={'A': 71, 'C': 103, 'E': 129, 'D': 115, 'G': 57, 'F': 147, 'I': 113, 'H': 137, 'K': 128, 'M': 131,
         'L': 113, 'N': 114, 'Q': 128, 'P': 97, 'S': 87, 'R': 156, 'T': 101, 'W': 186, 'V': 99, 'Y': 163}
leaderPeptide=LeaderboardCyclopeptideSequencing(Spectrum,N)
for el in leaderPeptide:
    elem=str(el)
    print(elem+"-",end="")