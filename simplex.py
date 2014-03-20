from pyplasm import *

s0,s1,s2,s3 = [SIMPLEX(d) for d in range(4)]

VIEW(s1);VIEW(s2),VIEW(s3);

points = [[1,1,1],[0,1,1],[1,0,0],[1,1,0]]
tetra = JOIN(AA(MK)(points))
VIEW(tetra)
