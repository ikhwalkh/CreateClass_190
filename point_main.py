from point import *
from point3 import *
p1 = Point()
p1.set_location(3,4)
jarak = p1.distance_from_origin()
print("Jarak dari titik asal ", jarak)
p1_lain = Point()
p1_lain.set_location(10,10)
jarak_dua_titik = p1.distance(p1_lain)
print("Jarak:", jarak_dua_titik)
p13D = Point3D(10, -12, 3)
print (p13D)