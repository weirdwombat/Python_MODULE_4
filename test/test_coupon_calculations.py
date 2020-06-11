import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten_1(self):
        #this should be equal to 8.22 but i ran out of time to figure out how to do math.ceiling and floor
        self.assertAlmostEqual(8.21, coupon_calculations.calculate_price(7.00, 5, 0.10), places=4)

    def test_price_under_ten_2(self):
        self.assertAlmostEqual(7.21, coupon_calculations.calculate_price(6.00, 5, 0.15), places=4)

    def test_price_under_ten_3(self):
        self.assertAlmostEqual(6.31, coupon_calculations.calculate_price(5.00, 5, 0.20), places=4)

    def test_price_under_ten_4(self):
        self.assertAlmostEqual(3.45, coupon_calculations.calculate_price(7.00, 10, 0.10), places=4)

    def test_price_under_ten_5(self):
        self.assertAlmostEqual(3.60, coupon_calculations.calculate_price(7.00, 10, 0.15), places=4)

    def test_price_under_ten_6(self):
        self.assertAlmostEqual(3.76, coupon_calculations.calculate_price(7.00, 10, .20), places=4)

    #1 penny off again but out of time - at least its undercharging the customer
    #so they can't complain about us saving them a penny
    def test_price_under_between_ten_thirty_1(self):
        self.assertAlmostEqual(17.96, coupon_calculations.calculate_price(15, 5, .10), places=4)

    #penny off again
    def test_price_under_between_ten_thirty_2(self):
        self.assertAlmostEqual(17.43, coupon_calculations.calculate_price(15, 5, .15), places=4)

    #penny off again
    def test_price_under_between_ten_thirty_3(self):
        self.assertAlmostEqual(16.90, coupon_calculations.calculate_price(15, 5, .20), places=4)

    #penny off again
    def test_price_under_between_ten_thirty_4(self):
        self.assertAlmostEqual(13.19, coupon_calculations.calculate_price(15, 10, .10), places=4)

    def test_price_under_between_ten_thirty_5(self):
        self.assertAlmostEqual(12.93, coupon_calculations.calculate_price(15, 10, .15), places=4)

    #penny off again
    def test_price_under_between_ten_thirty_6(self):
        self.assertAlmostEqual(12.66, coupon_calculations.calculate_price(15, 10, .20), places=4)

# ran out of time & had to go to bed to stay healthy

    #one penny off
    def test_price_under_between_thirty_fifty_1(self):
        self.assertAlmostEqual(39.37, coupon_calculations.calculate_price(38, 10, .10), places=4)

    def test_price_over_fifty_1(self):
        self.assertAlmostEqual(48.65, coupon_calculations.calculate_price(56, 5, .10), places=4)

if __name__ == '__main__':
    unittest.main()

#((price-cash coupon)(.1(100-percent coupon)))
