from pyplasm import *

def circle(r):
  def circle0(p):
    alpha = p[0]
    return [r*COS(alpha), r*SIN(alpha)]
  return circle0


colversud1 = [[9.33,33.02],[10.99,33.02],[9.546,33.02,10],[10.774,33.02,10]]
colversud2 = [[13.33,33.02],[14.99,33.02],[13.546,33.02,10],[14.774,33.02,10]]
colversud3 = [[17.33,33.02],[18.99,33.02],[17.546,33.02,10],[18.774,33.02,10]]
colversud4 = [[21.33,33.02],[22.99,33.02],[21.546,33.02,10],[22.774,33.02,10]]
colversud5 = [[25.33,33.02],[26.99,33.02],[25.546,33.02,10],[26.774,33.02,10]]
colversud6 = [[29.33,33.02],[30.99,33.02],[29.546,33.02,10],[30.774,33.02,10]]
colversud7 = [[33.33,33.02],[34.99,33.02],[33.546,33.02,10],[34.774,33.02,10]]
colversud8 = [[37.33,33.02],[38.99,33.02],[37.546,33.02,10],[38.774,33.02,10]]
colversud9 = [[41.33,33.02],[42.99,33.02],[41.546,33.02,10],[42.774,33.02,10]]
colversud10 = [[45.33,33.02],[46.99,33.02],[45.546,33.02,10],[46.774,33.02,10]]
colversud11 = [[49.33,33.02],[50.99,33.02],[49.546,33.02,10],[50.774,33.02,10]]
colversud12 = [[53.33,33.02],[54.99,33.02],[53.546,33.02,10],[54.774,33.02,10]]
colversud13 = [[57.33,33.02],[58.99,33.02],[57.546,33.02,10],[58.774,33.02,10]]
colversud14 = [[61.33,33.02],[62.99,33.02],[61.546,33.02,10],[62.774,33.02,10]]
colversud15 = [[65.33,33.02],[66.99,33.02],[65.546,33.02,10],[66.774,33.02,10]]

COLVERSUD1 = AA(MK)(colversud1)
COLVERSUD2 = AA(MK)(colversud2)
COLVERSUD3 = AA(MK)(colversud3)
COLVERSUD4 = AA(MK)(colversud4)
COLVERSUD5 = AA(MK)(colversud5)
COLVERSUD6 = AA(MK)(colversud6)
COLVERSUD7 = AA(MK)(colversud7)
COLVERSUD8 = AA(MK)(colversud8)
COLVERSUD9 = AA(MK)(colversud9)
COLVERSUD10 = AA(MK)(colversud10)
COLVERSUD11 = AA(MK)(colversud11)
COLVERSUD12 = AA(MK)(colversud12)
COLVERSUD13 = AA(MK)(colversud13)
COLVERSUD14 = AA(MK)(colversud14)
COLVERSUD15 = AA(MK)(colversud15)


colvernord1 = [[9.33,8.88],[10.99,8.88],[9.546,8.88,10],[10.774,8.88,10]]
colvernord2 = [[13.33,8.88],[14.99,8.88],[13.546,8.88,10],[14.774,8.88,10]]
colvernord3 = [[17.33,8.88],[18.99,8.88],[17.546,8.88,10],[18.774,8.88,10]]
colvernord4 = [[21.33,8.88],[22.99,8.88],[21.546,8.88,10],[22.774,8.88,10]]
colvernord5 = [[25.33,8.88],[26.99,8.88],[25.546,8.88,10],[26.774,8.88,10]]
colvernord6 = [[29.33,8.88],[30.99,8.88],[29.546,8.88,10],[30.774,8.88,10]]
colvernord7 = [[33.33,8.88],[34.99,8.88],[33.546,8.88,10],[34.774,8.88,10]]
colvernord8 = [[37.33,8.88],[38.99,8.88],[37.546,8.88,10],[38.774,8.88,10]]
colvernord9 = [[41.33,8.88],[42.99,8.88],[41.546,8.88,10],[42.774,8.88,10]]
colvernord10 = [[45.33,8.88],[46.99,8.88],[45.546,8.88,10],[46.774,8.88,10]]
colvernord11 = [[49.33,8.88],[50.99,8.88],[49.546,8.88,10],[50.774,8.88,10]]
colvernord12 = [[53.33,8.88],[54.99,8.88],[53.546,8.88,10],[54.774,8.88,10]]
colvernord13 = [[57.33,8.88],[58.99,8.88],[57.546,8.88,10],[58.774,8.88,10]]
colvernord14 = [[61.33,8.88],[62.99,8.88],[61.546,8.88,10],[62.774,8.88,10]]
colvernord15 = [[65.33,8.88],[66.99,8.88],[65.546,8.88,10],[66.774,8.88,10]]

COLVERNORD1 = AA(MK)(colvernord1)
COLVERNORD2 = AA(MK)(colvernord2)
COLVERNORD3 = AA(MK)(colvernord3)
COLVERNORD4 = AA(MK)(colvernord4)
COLVERNORD5 = AA(MK)(colvernord5)
COLVERNORD6 = AA(MK)(colvernord6)
COLVERNORD7 = AA(MK)(colvernord7)
COLVERNORD8 = AA(MK)(colvernord8)
COLVERNORD9 = AA(MK)(colvernord9)
COLVERNORD10 = AA(MK)(colvernord10)
COLVERNORD11 = AA(MK)(colvernord11)
COLVERNORD12 = AA(MK)(colvernord12)
COLVERNORD13 = AA(MK)(colvernord13)
COLVERNORD14 = AA(MK)(colvernord14)
COLVERNORD15 = AA(MK)(colvernord15)


COLS_VERT_SUD = [COLVERSUD1,COLVERSUD2,COLVERSUD3,COLVERSUD4,COLVERSUD5,COLVERSUD6,COLVERSUD7,COLVERSUD8,COLVERSUD9,COLVERSUD10,COLVERSUD11,COLVERSUD12,COLVERSUD13,COLVERSUD14,COLVERSUD15]
COLS_VERT_NORD = [COLVERNORD1,COLVERNORD2,COLVERNORD3,COLVERNORD4,COLVERNORD5,COLVERNORD6,COLVERNORD7,COLVERNORD8,COLVERNORD9,COLVERNORD10,COLVERNORD11,COLVERNORD12,COLVERNORD13,COLVERNORD14,COLVERNORD15]
SOUTH = AA(JOIN)(COLS_VERT_SUD)
south = AA(SKELETON(1))(SOUTH)
NORTH = AA(JOIN)(COLS_VERT_NORD)
north = AA(SKELETON(1))(NORTH)
VIEW(STRUCT(south + north))

#########TEST
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

