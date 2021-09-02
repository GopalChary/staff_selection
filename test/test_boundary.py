import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
from boundary import OutOfBoundaryMarksError
class BoundaryTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_boundary_revised.txt","w") as f:
            pass
    def test_negative_marks(self):
        try:
            MainClass.calculate_result("Venu,-80,98,90")
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestNegativeMarks=False\n")
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestNegativeMarks=True\n")

    def test_marks_boundary(self):
        try:
            MainClass.calculate_result("Venu,192,98,90")
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestMarksBoundary=False\n")
        except (ValueError,OutOfBoundaryMarksError):
            with open("output_boundary_revised.txt","a") as f:
                f.write("TestMarksBoundary=True\n")
