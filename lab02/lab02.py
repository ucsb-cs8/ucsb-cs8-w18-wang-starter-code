import pytest

def perimRect(length,width):
  """ Compute perimeter of a rectangle """
  return -42.0 # stub  @@@ replace this stub with the correct code @@@

def test_perimRect_1():
  assert perimRect(4,5)==18

def test_perimRect_2():
  assert perimRect(7,3)==20

def test_perimRect_3():
  assert perimRect(2.1,4.3)==pytest.approx(12.8)

def test_areaTriangle_1():
  assert areaTriangle(4,5) == 10
    
from collections import namedtuple

Book = namedtuple("Book", "title author price")
b1 = Book("Ready Player One", "Ernest Cline", 16)

def test_computePrice_1():
  assert computePrice(0, b1) == 0
    
