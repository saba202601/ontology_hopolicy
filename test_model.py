import unittest
from model import hurricane_deductible
class DeductibleTests(unittest.TestCase):
    def test_first(self): self.assertEqual(hurricane_deductible(400000,.02,2500),8000)
    def test_remaining(self): self.assertEqual(hurricane_deductible(400000,.02,2500,3000,True),5000)
    def test_aop_floor(self): self.assertEqual(hurricane_deductible(400000,.02,2500,8000,True),2500)
    def test_invalid_credit(self):
        with self.assertRaises(ValueError): hurricane_deductible(400000,.02,2500,9000,True)
    def test_credit_on_first(self):
        with self.assertRaises(ValueError): hurricane_deductible(400000,.02,2500,1000,False)
if __name__=='__main__': unittest.main()
