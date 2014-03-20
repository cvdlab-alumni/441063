from pyplasm import *

#definisci un array di punti
pts = [[0,0],[.5,0],[0,.5],[.5,.5],[1,.5],[1.5,.5],[1.5,1],[.25,1]]

# crea un poligono 0-dimensionale con i punti definiti
P = AA(MK)(pts)

# applica la funzione JOIN ai tre subset di P
# involucro convesso di P
S = AA(JOIN)([P[0:4],P[4:7],P[5:7]])


# unisce i poligoni presenti in S, 2 in questo caso
# il terzo elemento di S e' un punto
H = JOIN(S)

#unisce i punti nel poligono creato
PP = JOIN(P)

VIEW(H)
