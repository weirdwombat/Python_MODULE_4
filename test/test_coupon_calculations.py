import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten_1(self):
        #this is calling the above calculate_price(price, cash_coupon, percent_coupon) with price 7, coupon 5, etc
        self.assertAlmostEqual(5.89, coupon_calculations.calculate_price(7.00, 5, .10), places=4)
        #note you will want to change price, the 7.00, to an actual value, and 5.89 to what it should calculate to
        #the unit tests can't run every number under 10, so you have to pick and choose

    def test_price_under_ten_2(self):
        self.assertAlmostEqual(4.99, coupon_calculations.calculate_price(6.00, 5, .15), places=4)
        #note above uses almost equal and passes in places, as there could be minor rounding differences
        #from computers, could be comparing 4.9900000001 and 4.99; so above is best

    def test_price_under_ten_3(self):
        self.assertAlmostEqual(6.31, coupon_calculations.calculate_price(5.00, 5, .20), places=4)

    def test_price_under_ten_4(self):
        self.assertAlmostEqual(3.45, coupon_calculations.calculate_price(7.00, 10, .10), places=4)

    def test_price_under_ten_5(self):
        self.assertAlmostEqual(3.60, coupon_calculations.calculate_price(7.00, 10, .15), places=4)

    def test_price_under_ten_6(self):
        self.assertAlmostEqual(3.76, coupon_calculations.calculate_price(7.00, 10, .20), places=4)


if __name__ == '__main__':
    unittest.main()

#((price-cash coupon)(.1(100-percent coupon)))
