class Graphic2D:
    x = 0
    y = 0
    
    def GraphicPrint(self):
        return '{},{}'.format(self.x,self.y)
        

class Graphic3D(Graphic2D):
    z = 0
    def GraphicPrint(self):
        return '{},{}'.format(super().GraphicPrint(),self.z)
        


a2 = Graphic2D()
print(a2.GraphicPrint())

a3=Graphic3D()
print(a3.GraphicPrint())
