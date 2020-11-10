import math 
from calculator import area_of_circle

def test_area_of_circle():
    assert area_of_circle(5) == 25*math.pi
