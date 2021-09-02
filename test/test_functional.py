import unittest
import sys
sys.path.append("..")
from mainclass import MainClass
class FuctionalTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open("output_revised.txt","w") as f:
            pass
    def test_is_candidate_qualified(self):
        obj=MainClass.calculate_result("Venu,92,98,96")
        if type(obj)!=type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateQualified=True\n")
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateQualified=False\n")
    def test_is_candidate_fail(self):
        obj=MainClass.calculate_result("Ravan,42,38,96")
        print(type(obj),type(None))
        if type(obj)==type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateFail=True\n")
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidateFail=False\n")
    def test_is_candidate_pass(self):
        obj=MainClass.calculate_result("Ravan,52,55,58")
        print(type(obj),type(None))
        if type(obj)==type(None):
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidatePass=True\n")
        else:
            with open("output_revised.txt","a") as f:
                f.write("TestIsCandidatePass=False\n")
