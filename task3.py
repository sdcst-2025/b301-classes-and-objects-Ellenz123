"""
Rectangular Prism Object
Create a class that creates a rectangular prism.  You should be able to set all of the important measurements (l,w,h) when the object is instantiated in the constructor and you should have class methods that determine the surface area and volume.
You should have class methods that also allow you to change the dimensions of the object.
Instantiate 3 separate rectangular prisms with the test data given, and check the assertions are correct.
"""

class rectPrism:

    def __init__(self,l,w,h):
        # note you will need to specify more input parameters
        self.l=l
        self.w=w
        self.h=h
        pass

    def volume(self):
        if self.l<=0 or self.h<=0 or self.w<=0:
            return None
        return self.l*self.w*self.h
    
    def surfaceArea(self):
        if self.l<=0 or self.h<=0 or self.w<=0:
            return None
        return (self.l*self.w + self.l*self.h + self.w*self.h)*2
    
    def dimemsion(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h

# class instances and assertions below:

a = rectPrism(l=10,w=2,h=5)
assert a.volume() == 100
assert a.surfaceArea() == 160

b = rectPrism(l=1,w=1,h=1)
assert b.volume() == 1
assert b.surfaceArea() == 6

c = rectPrism(l=2,w=0,h=10)
# note the invalid width
assert c.volume() == None
assert c.surfaceArea() == None

print("All tests passed")