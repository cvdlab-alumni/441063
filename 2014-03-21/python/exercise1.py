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
trave_centrale = [[32.12,28.33],[33.14,28.33],[33.14,13.38],[32.12,13.38]]
supporto_sud_est = [[52.71,28.33],[52.71,23.97],[54.72,23.97],[54.72,28.33]]
finale_sud_est = [[54.26,23.97],[54.26,22.44],[52.71,22.44],[52.71,23.97]]
supporto_nord_est = [[52.71,13.38],[52.71,17.73],[54.72,17.73],[54.72,13.38]]
finale_nord_est = [[54.26,17.73],[54.26,19.25],[52.71,19.25],[52.71,17.73]]

BLOCK1 = AA(MK)(travelunga_sud)
BLOCK2 = AA(MK)(travelunga_nord)
BLOCK3 = AA(MK)(supporto_travelunga_nord)
BLOCK4 = AA(MK)(finale_travelunga_nord)
BLOCK5 = AA(MK)(supporto_travelunga_sud)
BLOCK6 = AA(MK)(finale_travelunga_sud)
BLOCK7 = AA(MK)(trave_centrale)
BLOCK8 = AA(MK)(supporto_sud_est)
BLOCK9 = AA(MK)(finale_sud_est)
BLOCK10 = AA(MK)(supporto_nord_est)
BLOCK11 = AA(MK)(finale_nord_est)

B1 = JOIN(BLOCK1)
B2 = JOIN(BLOCK2)
B3 = JOIN(BLOCK3)
B4 = JOIN(BLOCK4)
B5 = JOIN(BLOCK5)
B6 = JOIN(BLOCK6)
B7 = JOIN(BLOCK7)
B8 = JOIN(BLOCK8)
B9 = JOIN(BLOCK9)
B10 = JOIN(BLOCK10)
B11 = JOIN(BLOCK11)

colcentro1 = T([1,2])([23.38, 23.41])(MAP(circle(0.75))(INTERVALS(2*PI)(32)))
colcentro2 = T([1,2])([28.50, 23.41])(MAP(circle(0.75))(INTERVALS(2*PI)(32)))
colcentro3 = T([1,2])([28.50, 18.28])(MAP(circle(0.75))(INTERVALS(2*PI)(32)))
colcentro4 = T([1,2])([23.38, 18.28])(MAP(circle(0.75))(INTERVALS(2*PI)(32)))

colonneminisud1 = T([1,2])([37.08, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud2 = T([1,2])([38.88, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud3 = T([1,2])([40.68, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud4 = T([1,2])([42.48, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud5 = T([1,2])([44.28, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud6 = T([1,2])([46.08, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud7 = T([1,2])([47.88, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud8 = T([1,2])([49.68, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminisud9 = T([1,2])([51.48, 24.31])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))

colonnemininord1 = T([1,2])([37.08, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord2 = T([1,2])([38.88, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord3 = T([1,2])([40.68, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord4 = T([1,2])([42.48, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord5 = T([1,2])([44.28, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord6 = T([1,2])([46.08, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord7 = T([1,2])([47.88, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord8 = T([1,2])([49.68, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonnemininord9 = T([1,2])([51.48, 17.41])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))

colonneminiwest1 = T([1,2])([35.46, 19])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminiwest2 = T([1,2])([35.46, 20.8])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))
colonneminiwest3 = T([1,2])([35.46, 22.6])(MAP(circle(0.50))(INTERVALS(2*PI)(32)))


blocks =[B1,B2,B3,B4,B5,B6,B7,B8,B9,B10,B11]
cols_sud = [colsud1,colsud2,colsud3,colsud4,colsud5,colsud6,colsud7,colsud8,colsud9,colsud10,colsud11,colsud12,colsud13,colsud14,colsud15]
cols_nord = [colnord1,colnord2,colnord3,colnord4,colnord5,colnord6,colnord7,colnord8,colnord9,colnord10,colnord11,colnord12,colnord13,colnord14,colnord15]
cols_est = [colest1,colest2,colest3,colest4,colest5]
cols_west = [colwest1,colwest2,colwest3,colwest4,colwest5]
cols_small_est = [colestsmall1,colestsmall2,colestsmall3,colestsmall4,colestsmall5,colestsmall6]
cols_small_west = [colwestsmall1,colwestsmall2,colwestsmall3,colwestsmall4,colwestsmall5,colwestsmall6]
cols_centro = [colcentro1,colcentro2,colcentro3,colcentro4]
cols_mini_sud = [colonneminisud1,colonneminisud2,colonneminisud3,colonneminisud4,colonneminisud5,colonneminisud6,colonneminisud7,colonneminisud8,colonneminisud9]
cols_mini_nord = [colonnemininord1,colonnemininord2,colonnemininord3,colonnemininord4,colonnemininord5,colonnemininord6,colonnemininord7,colonnemininord8,colonnemininord9]
cols_mini_west = [colonneminiwest1,colonneminiwest2,colonneminiwest3]
S = AA(JOIN)([EXT,CENTER,IN] + cols_sud + cols_nord + cols_est + cols_west + cols_small_est + cols_small_west + blocks + cols_centro + cols_mini_sud + cols_mini_nord + cols_mini_west)
floor0 = AA(SKELETON(1))(S)










################################################################################################
################################## UPPER LEVEL #################################################
################################################################################################
uborder_ext = [[6.08,6.87,10],[69.51,6.87,10],[69.51,35.32,10],[6.08,35.32,10]]
UEXT = AA(MK)(uborder_ext)


ucolsud1 = T([1,2,3])([10.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud2 = T([1,2,3])([14.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud3 = T([1,2,3])([18.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud4 = T([1,2,3])([22.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud5 = T([1,2,3])([26.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud6 = T([1,2,3])([30.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud7 = T([1,2,3])([34.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud8 = T([1,2,3])([38.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud9 = T([1,2,3])([42.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud10 = T([1,2,3])([46.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud11 = T([1,2,3])([50.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud12 = T([1,2,3])([54.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud13 = T([1,2,3])([58.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud14 = T([1,2,3])([62.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolsud15 = T([1,2,3])([66.16, 33.02,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))

ucolnord1 = T([1,2,3])([10.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord2 = T([1,2,3])([14.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord3 = T([1,2,3])([18.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord4 = T([1,2,3])([22.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord5 = T([1,2,3])([26.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord6 = T([1,2,3])([30.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord7 = T([1,2,3])([34.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord8 = T([1,2,3])([38.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord9 = T([1,2,3])([42.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord10 = T([1,2,3])([46.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord11 = T([1,2,3])([50.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord12 = T([1,2,3])([54.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord13 = T([1,2,3])([58.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord14 = T([1,2,3])([62.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolnord15 = T([1,2,3])([66.16, 8.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))

ucolest1 = T([1,2,3])([66.16, 12.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolest2 = T([1,2,3])([66.16, 16.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolest3 = T([1,2,3])([66.16, 20.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolest4 = T([1,2,3])([66.16, 24.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolest5 = T([1,2,3])([66.16, 28.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))

ucolestsmall6 = T([1,2,3])([62.68, 12.53,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolestsmall1 = T([1,2,3])([62.68, 15.55,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolestsmall2 = T([1,2,3])([62.68, 18.95,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolestsmall3 = T([1,2,3])([62.68, 22.35,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolestsmall4 = T([1,2,3])([62.68, 25.75,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolestsmall5 = T([1,2,3])([62.68, 28.98,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))


ucolwest1 = T([1,2,3])([10.16, 12.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolwest2 = T([1,2,3])([10.16, 16.85,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolwest3 = T([1,2,3])([10.16, 20.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolwest4 = T([1,2,3])([10.16, 24.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))
ucolwest5 = T([1,2,3])([10.16, 28.88,10])(MAP(circle(0.614))(INTERVALS(2*PI)(32)))

ucolwestsmall6 = T([1,2,3])([13.16, 12.53,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolwestsmall1 = T([1,2,3])([13.16, 15.55,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolwestsmall2 = T([1,2,3])([13.16, 18.95,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolwestsmall3 = T([1,2,3])([13.16, 22.35,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolwestsmall4 = T([1,2,3])([13.16, 25.75,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))
ucolwestsmall5 = T([1,2,3])([13.16, 28.98,10])(MAP(circle(0.54))(INTERVALS(2*PI)(32)))

utravelunga_sud = [[16.19,28.33,10],[16.19,29.87,10],[59.67,28.34,10],[59.67,29.87,10]]
utravelunga_nord = [[16.19,11.8,10],[16.19,13.38,10],[59.67,11.80,10],[59.67,13.38,10]]
usupporto_travelunga_nord = [[17.56,13.38,10],[17.56,18.03,10],[19.33,18.03,10],[19.33,13.38,10]]
ufinale_travelunga_nord = [[17.85,18.03,10],[17.85,19.20,10],[19.33,19.20,10],[19.33,18.03,10]]
usupporto_travelunga_sud = [[17.56,28.33,10],[17.56,23.68,10],[19.33,23.68,10],[19.33,28.33,10]]
ufinale_travelunga_sud = [[17.85,23.68,10],[17.85,22.41,10],[19.33,22.41,10],[19.33,23.68,10]]
utrave_centrale = [[32.12,28.33,10],[33.14,28.33,10],[33.14,13.38,10],[32.12,13.38,10]]
usupporto_sud_est = [[52.71,28.33,10],[52.71,23.97,10],[54.72,23.97,10],[54.72,28.33,10]]
ufinale_sud_est = [[54.26,23.97,10],[54.26,22.44,10],[52.71,22.44,10],[52.71,23.97,10]]
usupporto_nord_est = [[52.71,13.38,10],[52.71,17.73,10],[54.72,17.73,10],[54.72,13.38,10]]
ufinale_nord_est = [[54.26,17.73,10],[54.26,19.25,10],[52.71,19.25,10],[52.71,17.73,10]]


ucolcentro1 = T([1,2,3])([23.38, 23.41,10])(MAP(circle(0.555))(INTERVALS(2*PI)(32)))
ucolcentro2 = T([1,2,3])([28.50, 23.41,10])(MAP(circle(0.555))(INTERVALS(2*PI)(32)))
ucolcentro3 = T([1,2,3])([28.50, 18.28,10])(MAP(circle(0.555))(INTERVALS(2*PI)(32)))
ucolcentro4 = T([1,2,3])([23.38, 18.28,10])(MAP(circle(0.555))(INTERVALS(2*PI)(32)))

ucolonneminisud1 = T([1,2,3])([37.08, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud2 = T([1,2,3])([38.88, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud3 = T([1,2,3])([40.68, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud4 = T([1,2,3])([42.48, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud5 = T([1,2,3])([44.28, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud6 = T([1,2,3])([46.08, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud7 = T([1,2,3])([47.88, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud8 = T([1,2,3])([49.68, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminisud9 = T([1,2,3])([51.48, 24.31,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))

ucolonnemininord1 = T([1,2,3])([37.08, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord2 = T([1,2,3])([38.88, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord3 = T([1,2,3])([40.68, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord4 = T([1,2,3])([42.48, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord5 = T([1,2,3])([44.28, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord6 = T([1,2,3])([46.08, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord7 = T([1,2,3])([47.88, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord8 = T([1,2,3])([49.68, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonnemininord9 = T([1,2,3])([51.48, 17.41,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))

ucolonneminiwest1 = T([1,2,3])([35.46, 19,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminiwest2 = T([1,2,3])([35.46, 20.8,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))
ucolonneminiwest3 = T([1,2,3])([35.46, 22.6,10])(MAP(circle(0.37))(INTERVALS(2*PI)(32)))


UBLOCK1 = AA(MK)(utravelunga_sud)
UBLOCK2 = AA(MK)(utravelunga_nord)
UBLOCK3 = AA(MK)(usupporto_travelunga_nord)
UBLOCK4 = AA(MK)(ufinale_travelunga_nord)
UBLOCK5 = AA(MK)(usupporto_travelunga_sud)
UBLOCK6 = AA(MK)(ufinale_travelunga_sud)
UBLOCK7 = AA(MK)(utrave_centrale)
UBLOCK8 = AA(MK)(usupporto_sud_est)
UBLOCK9 = AA(MK)(ufinale_sud_est)
UBLOCK10 = AA(MK)(usupporto_nord_est)
UBLOCK11 = AA(MK)(ufinale_nord_est)

UB1 = JOIN(UBLOCK1)
UB2 = JOIN(UBLOCK2)
UB3 = JOIN(UBLOCK3)
UB4 = JOIN(UBLOCK4)
UB5 = JOIN(UBLOCK5)
UB6 = JOIN(UBLOCK6)
UB7 = JOIN(UBLOCK7)
UB8 = JOIN(UBLOCK8)
UB9 = JOIN(UBLOCK9)
UB10 = JOIN(UBLOCK10)
UB11 = JOIN(UBLOCK11)


ublocks =[UB1,UB2,UB3,UB4,UB5,UB6,UB7,UB8,UB9,UB10,UB11]
ucols_sud = [ucolsud1,ucolsud2,ucolsud3,ucolsud4,ucolsud5,ucolsud6,ucolsud7,ucolsud8,ucolsud9,ucolsud10,ucolsud11,ucolsud12,ucolsud13,ucolsud14,ucolsud15]
ucols_nord = [ucolnord1,ucolnord2,ucolnord3,ucolnord4,ucolnord5,ucolnord6,ucolnord7,ucolnord8,ucolnord9,ucolnord10,ucolnord11,ucolnord12,ucolnord13,ucolnord14,ucolnord15]
ucols_est = [ucolest1,ucolest2,ucolest3,ucolest4,ucolest5]
ucols_west = [ucolwest1,ucolwest2,ucolwest3,ucolwest4,ucolwest5]
ucols_small_est = [ucolestsmall1,ucolestsmall2,ucolestsmall3,ucolestsmall4,ucolestsmall5,ucolestsmall6]
ucols_small_west = [ucolwestsmall1,ucolwestsmall2,ucolwestsmall3,ucolwestsmall4,ucolwestsmall5,ucolwestsmall6]
ucols_centro = [ucolcentro1,ucolcentro2,ucolcentro3,ucolcentro4]
ucols_mini_sud = [ucolonneminisud1,ucolonneminisud2,ucolonneminisud3,ucolonneminisud4,ucolonneminisud5,ucolonneminisud6,ucolonneminisud7,ucolonneminisud8,ucolonneminisud9]
ucols_mini_nord = [ucolonnemininord1,ucolonnemininord2,ucolonnemininord3,ucolonnemininord4,ucolonnemininord5,ucolonnemininord6,ucolonnemininord7,ucolonnemininord8,ucolonnemininord9]
ucols_mini_west = [ucolonneminiwest1,ucolonneminiwest2,ucolonneminiwest3]
US = AA(JOIN)( [UEXT] + ucols_sud + ucols_nord + ucols_est + ucols_west + ucols_small_est + ucols_small_west + ublocks + ucols_centro + ucols_mini_sud + ucols_mini_nord + ucols_mini_west)
floor1 = AA(SKELETON(1))(US)



two_and_half_model = floor1 + floor0

VIEW(STRUCT(two_and_half_model))


