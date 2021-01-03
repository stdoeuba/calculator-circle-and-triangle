
from foo import foo
from calculator import area, circle_of_area
from math import pi

def test_foo():
	assert foo(5) == 6


def test_area ():
	assert area(3, 4) == 6

def test_area_of_circle():
    assert area_of_circle(5) == 25 * pi
	
	

	

