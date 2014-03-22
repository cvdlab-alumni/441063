from pyplasm import *


def circle(r):
  def circle0(p):
    alpha = p[0]
    return [r*COS(alpha), r*SIN(alpha)]
  return circle0


border_ext = [[6.08,6.87],[69.51,6.87],[69.51,35.32],[6.08,35.32]]
border_center = [[6.6,7.38],[68.75,7.38],[68.75,34.57],[6.6,34.57]]
border_in = [[7.24,7.79],[68.33,7.79],[68.33,34.15],[7.24,34.15]]

EXT = AA(MK)(border_ext)
CENTER = AA(MK)(border_center)
IN = AA(MK)(border_in)

colsud1 = T([1,2])([10.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud2 = T([1,2])([14.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud3 = T([1,2])([18.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud4 = T([1,2])([22.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud5 = T([1,2])([26.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud6 = T([1,2])([30.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud7 = T([1,2])([34.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud8 = T([1,2])([38.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud9 = T([1,2])([42.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud10 = T([1,2])([46.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud11 = T([1,2])([50.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud12 = T([1,2])([54.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud13 = T([1,2])([58.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud14 = T([1,2])([62.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colsud15 = T([1,2])([66.16, 33.02])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))

colnord1 = T([1,2])([10.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord2 = T([1,2])([14.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord3 = T([1,2])([18.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord4 = T([1,2])([22.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord5 = T([1,2])([26.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord6 = T([1,2])([30.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord7 = T([1,2])([34.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord8 = T([1,2])([38.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord9 = T([1,2])([42.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord10 = T([1,2])([46.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord11 = T([1,2])([50.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord12 = T([1,2])([54.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord13 = T([1,2])([58.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord14 = T([1,2])([62.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colnord15 = T([1,2])([66.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))

colest1 = T([1,2])([66.16, 12.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colest2 = T([1,2])([66.16, 16.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colest3 = T([1,2])([66.16, 20.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colest4 = T([1,2])([66.16, 24.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colest5 = T([1,2])([66.16, 28.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colest6 = T([1,2])([66.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))

colestsmall6 = T([1,2])([62.68, 12.53])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colestsmall1 = T([1,2])([62.68, 15.55])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colestsmall2 = T([1,2])([62.68, 18.95])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colestsmall3 = T([1,2])([62.68, 22.35])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colestsmall4 = T([1,2])([62.68, 25.75])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colestsmall5 = T([1,2])([62.68, 28.98])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))


colwest1 = T([1,2])([10.16, 12.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest2 = T([1,2])([10.16, 16.85])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest3 = T([1,2])([10.16, 20.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest4 = T([1,2])([10.16, 24.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest5 = T([1,2])([10.16, 28.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest6 = T([1,2])([10.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))

colwestsmall6 = T([1,2])([13.16, 12.53])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colwestsmall1 = T([1,2])([13.16, 15.55])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colwestsmall2 = T([1,2])([13.16, 18.95])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colwestsmall3 = T([1,2])([13.16, 22.35])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colwestsmall4 = T([1,2])([13.16, 25.75])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))
colwestsmall5 = T([1,2])([13.16, 28.98])(MAP(circle(0.73))(INTERVALS(2*PI)(32)))

travelunga_sud = [[16.19,28.33],[16.19,29.87],[59.67,28.34],[59.67,29.87]]
travelunga_nord = [[16.19,11.8],[16.19,13.38],[59.67,11.80],[59.67,13.38]]
supporto_travelunga_nord = [[17.56,13.38],[17.56,18.03],[19.33,18.03],[19.33,13.38]]
finale_travelunga_nord = [[17.85,18.03],[17.85,19.20],[19.33,19.20],[19.33,18.03]]
supporto_travelunga_sud = [[17.56,28.33],[17.56,23.68],[19.33,23.68],[19.33,28.33]]
finale_travelunga_sud = [[17.85,23.68],[17.85,22.41],[19.33,22.41],[19.33,23.68]]

BLOCK1 = AA(MK)(travelunga_sud)
BLOCK2 = AA(MK)(travelunga_nord)
BLOCK3 = AA(MK)(supporto_travelunga_nord)
BLOCK4 = AA(MK)(finale_travelunga_nord)
BLOCK5 = AA(MK)(supporto_travelunga_sud)
BLOCK6 = AA(MK)(finale_travelunga_sud)

B1 = JOIN(BLOCK1)
B2 = JOIN(BLOCK2)
B3 = JOIN(BLOCK3)
B4 = JOIN(BLOCK4)
B5 = JOIN(BLOCK5)
B6 = JOIN(BLOCK6)
blocks =[B1,B2,B3,B4,B5,B6]
cols_sud = [colsud1,colsud2,colsud3,colsud4,colsud5,colsud6,colsud7,colsud8,colsud9,colsud10,colsud11,colsud12,colsud13,colsud14,colsud15]
cols_nord = [colnord1,colnord2,colnord3,colnord4,colnord5,colnord6,colnord7,colnord8,colnord9,colnord10,colnord11,colnord12,colnord13,colnord14,colnord15]
cols_est = [colest1,colest2,colest3,colest4,colest5,colest6]
cols_west = [colwest1,colwest2,colwest3,colwest4,colwest5,colwest6]
cols_small_est = [colestsmall1,colestsmall2,colestsmall3,colestsmall4,colestsmall5,colestsmall6]
cols_small_west = [colwestsmall1,colwestsmall2,colwestsmall3,colwestsmall4,colwestsmall5,colwestsmall6]

S = AA(JOIN)([EXT,CENTER,IN] + cols_sud + cols_nord + cols_est + cols_west + cols_small_est + cols_small_west + blocks)


VIEW(STRUCT(AA(SKELETON(1))(S)))