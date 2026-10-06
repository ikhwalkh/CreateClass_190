from point import *
class Point3D(Point):
    z = 0
    def __init__(self,  x,y,z):
        Point.__init__(x,y)
        self.z = z
    def translate(self, dx, dy, dz):
        self.x4 = dx
        self.y4 = dy
        self.z4 = dz
    def __str__(self):
        return str(self.x)+","+str(self.y)+ \
        ","+str(self.z)