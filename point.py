import math


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    
    @staticmethod
    def distance(p1,p2):
        x = abs(p1.x-p2.x)
        y = abs(p1.y-p2.y)
        return math.sqrt(math.pow(x,2)+math.pow(y,2))
    
    @staticmethod
    def is_collinear(p1,p2,p3):
        return Point.slope(p1,p2) == Point.slope(p2,p3) == Point.slope(p3,p1)
        #return (p1.x-p2.x)/(p1.x-p3.x) == (p1.y-p2.y)/(p1.y-p3.y)
    
    @staticmethod
    def slope(p1,p2):
        y = p1.y - p2.y
        x = p1.x - p2.x
        try : 
            return y/x
        except ZeroDivisionError:
            return 0

    
    @staticmethod
    def is_triangle(p1,p2,p3):
        return False if Point.is_collinear(p1,p2,p3) else True
    
    @staticmethod
    def is_equilateral_triangle(p1,p2,p3):
        return True if Point.distance(p1,p2) == Point.distance(p2,p3) == Point.distance(p3,p1) else False
    
    @staticmethod
    def is_isosceles_triangle(A,B,C):
        AB = Point.distance(A,B)
        BC = Point.distance(B,C)
        CA = Point.distance(C,A)        
        if AB==BC==CA:
            return False
        return True if AB==BC or BC==CA or CA==AB else False
    
    @staticmethod
    def is_right_angle_triangle(A,B,C):
        AB = math.pos(Point.distance(A,B),2)
        BC = math.pow(Point.distance(B,C),2)
        CA = math.pow(Point.distance(C,A),2)
        return True if AB+BC==CA or BC+CA==AB or AB+CA==BC else False
    
    @staticmethod
    def centroid(p1,p2,p3):
        pass
    
    @staticmethod
    def incenter(p1,p2,p3):
        pass
    
    @staticmethod
    def circumcenter(p1,p2,p3):
        pass
    
    @staticmethod
    def orthocenter(p1,p2,p3):
        pass
    
    @staticmethod
    def area_of_triangel(p1,p2,p3):
        pass
    
     
            
            
    
    def __str__(self):
        return f"( {self.x} , {self.y} )"
    
    
    
    
p1 = Point(1,0)
p2 = Point(2,1)
p3 = Point(3,0)
print(Point.is_collinear(p1,p2,p3))