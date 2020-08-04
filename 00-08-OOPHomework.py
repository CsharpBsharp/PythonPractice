'''Problem 1
Fill in the Line class methods to accept coordinates as a pair of tuples and return the slope and distance of the line.

class Line:

    def __init__(self,coor1,coor2):
        pass

    def distance(self):
        pass

    def slope(self):
        pass
# EXAMPLE OUTPUT
​
coordinate1 = (3,2)
coordinate2 = (8,10)
​
li = Line(coordinate1,coordinate2)
li.distance()
9.433981132056603
li.slope()
1.6
'''

#Line distance formula:
#d=√((x_2-x_1)²+(y_2-y_1)²)

#Line slope formula:
#m = rise/run = (y_2 - y_1) / (x_2 - x_1)

class Line:

    def __init__(self, coor1, coor2):
        self.coor1=coor1
        self.coor2=coor2

    def distance(self):
        from math import sqrt, pow
        return sqrt(pow(self.coor2[0]-self.coor1[0],2)+pow(self.coor2[1]-self.coor1[1],2))


    def slope(self):
        return (self.coor2[1]-self.coor1[1])/(self.coor2[0]-self.coor1[0])

#Declaring Tuples
coordinate1 = (3,2)
coordinate2 = (8,10)
#Creating new line object nad passing Tuples
li = Line(coordinate1,coordinate2)
print('Distance of the line is : {}'.format(li.distance()))
print('Slope of the line is : {}'.format(li.slope()))


'''
Problem 2
Fill in the class

class Cylinder:
    
    def __init__(self,height=1,radius=1):
        pass
        
    def volume(self):
        pass
    
    def surface_area(self):
        pass
# EXAMPLE OUTPUT
c = Cylinder(2,3)
c.volume()
56.52
c.surface_area()
94.2
'''

#Cylinder volume formula
#V=π*r**2*h

#Cylinder surface area formula
#A=2πrh+2πr**2

class Cylinder:

    def __init__(self, height=1, radius=1):
        self.height=height
        self.radius=radius

    def volume(self):
        from math import pi,pow
        return pi*pow(self.radius,2)*self.height

    def surface_area(self):
        from math import pi,pow
        return (2*pi*self.radius*self.height)+(2*pi*pow(self.radius,2))

c = Cylinder(2,3)
print('Volume of Cylinder is : {}'.format(c.volume()))
print('Surface Area of the Cylinder is : {}'.format(c.surface_area()))