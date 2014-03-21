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


colwest1 = T([1,2])([10.16, 12.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest2 = T([1,2])([10.16, 16.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest3 = T([1,2])([10.16, 20.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest4 = T([1,2])([10.16, 24.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest5 = T([1,2])([10.16, 28.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))
colwest6 = T([1,2])([10.16, 8.88])(MAP(circle(0.83))(INTERVALS(2*PI)(32)))

cols_sud = [colsud1,colsud2,colsud3,colsud4,colsud5,colsud6,colsud7,colsud8,colsud9,colsud10,colsud11,colsud12,colsud13,colsud14,colsud15]
cols_nord = [colnord1,colnord2,colnord3,colnord4,colnord5,colnord6,colnord7,colnord8,colnord9,colnord10,colnord11,colnord12,colnord13,colnord14,colnord15]
cols_est = [colest1,colest2,colest3,colest4,colest5,colest6]
cols_west = [colwest1,colwest2,colwest3,colwest4,colwest5,colwest6]
S = AA(JOIN)([EXT,CENTER,IN] + cols_sud + cols_nord + cols_est + cols_west)


VIEW(STRUCT(AA(SKELETON(1))(S)))