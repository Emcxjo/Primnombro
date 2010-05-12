#coding=UTF-8
prim=[2,3]
a=5
from math import *
print 'Bonvolu entajpi limon ĝis kiu ni kalkulos primnombrojn, ekz 50:'
limo=input()

while limo:

# tuta while-funkcio

    while a<limo:
        indico=0
        listo=[]
        radiko=sqrt(a)

 #ĉar ni ne volas testi la nombron a per primnombro kiu superas ties radikon. Tute ne utilas, tia nombro ne povus esti eblo de a.

        fusxa=[-1] 	#utilas por forlasi la testadon kaze de obleco

# testofunkcio kiu provas dividi a per ĉiu elemento de la jam ekzistanta primlisto

        while listo!=fusxa and prim[indico]<=radiko:
            if a%prim[indico]!=0:
                listo.append(prim[indico])
	    else:
	        fusxa=[]
	        listo=fusxa  #tio nuligas la while-funkcion kaj ŝparas kalkulojn neutilajn
	    indico=indico+1

# testo de la provizora listo montras ĉu ĝi nulas (la testo montris oblecon) aŭ ĉu ĝi sufiĉe longas ke ĝia longeco samas la b-indicon.

        if len(listo)==indico and indico!=0:
	    prim.append(a)
	    print a
        a=a+2
        f=a+1
   # if f%10000==0:
#	print f

# rezultanonco

    print prim
    print 'estas', len(prim), 'primnombroj ĝis', limo
# Ĝoju!

    limo=input('bv denove tajpi, se vi ŝatas:')
print 'nun finiĝis!'







