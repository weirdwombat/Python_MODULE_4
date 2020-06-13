import unittest
from store import coupon_calculations


class MyTestCase(unittest.TestCase):

    def test_price_under_ten_1(self):
        self.assertAlmostEqual(8.21, coupon_calculations.calculate_price(7.00, 5, 0.10), places=2)

    def test_price_under_ten_2(self):
        self.assertAlmostEqual(7.21, coupon_calculations.calculate_price(6.00, 5, 0.15), places=2)

    def test_price_under_ten_3(self):
        self.assertAlmostEqual(6.31, coupon_calculations.calculate_price(5.00, 5, 0.20), places=2)

    def test_price_under_ten_4(self):
        self.assertAlmostEqual(3.45, coupon_calculations.calculate_price(7.00, 10, 0.10), places=2)

    def test_price_under_ten_5(self):
        self.assertAlmostEqual(3.60, coupon_calculations.calculate_price(7.00, 10, 0.15), places=2)

    def test_price_under_ten_6(self):
        self.assertAlmostEqual(3.76, coupon_calculations.calculate_price(7.00, 10, .20), places=2)

    def test_price_under_between_ten_thirty_1(self):
        self.assertAlmostEqual(17.97, coupon_calculations.calculate_price(15, 5, .10), places=2)

    def test_price_under_between_ten_thirty_2(self):
        self.assertAlmostEqual(17.44, coupon_calculations.calculate_price(15, 5, .15), places=2)

    def test_price_under_between_ten_thirty_3(self):
        self.assertAlmostEqual(16.91, coupon_calculations.calculate_price(15, 5, .20), places=2)

    def test_price_under_between_ten_thirty_4(self):
        self.assertAlmostEqual(13.20, coupon_calculations.calculate_price(15, 10, .10), places=2)

    def test_price_under_between_ten_thirty_5(self):
        self.assertAlmostEqual(12.93, coupon_calculations.calculate_price(15, 10, .15), places=2)

    def test_price_under_between_ten_thirty_6(self):
        self.assertAlmostEqual(12.67, coupon_calculations.calculate_price(15, 10, .20), places=2)

    def test_price_under_between_thirty_fifty_1(self):
        self.assertAlmostEqual(44.15, coupon_calculations.calculate_price(38, 5, .10), places=2)

    def test_price_under_between_thirty_fifty_2(self):
        self.assertAlmostEqual(44.20, coupon_calculations.calculate_price(40, 5, .15), places=2)

    def test_price_under_between_thirty_fifty_3(self):
        self.assertAlmostEqual(34.72, coupon_calculations.calculate_price(31, 5, .20), places=2)

    def test_price_under_between_thirty_fifty_4(self):
        self.assertAlmostEqual(39.38, coupon_calculations.calculate_price(38, 10, .10), places=2)

    def test_price_under_between_thirty_fifty_5(self):
        self.assertAlmostEqual(41.50, coupon_calculations.calculate_price(42, 10, .15), places=2)

    def test_price_under_between_thirty_fifty_6(self):
        self.assertAlmostEqual(34.72, coupon_calculations.calculate_price(36, 10, .20), places=2)

    def test_price_over_fifty_1(self):
        self.assertAlmostEqual(48.65, coupon_calculations.calculate_price(56, 5, .10), places=2)

    def test_price_over_fifty_2(self):
        self.assertAlmostEqual(85.60, coupon_calculations.calculate_price(100, 5, .15), places=2)

    def test_price_over_fifty_3(self):
        self.assertAlmostEqual(43.25, coupon_calculations.calculate_price(56, 5, .20), places=2)

    def test_price_over_fifty_4(self):
        self.assertAlmostEqual(64.87, coupon_calculations.calculate_price(78, 10, .10), places=2)

    def test_price_over_fifty_5(self):
        self.assertAlmostEqual(63.07, coupon_calculations.calculate_price(80, 10, .15), places=2)

    def test_price_over_fifty_6(self):
        self.assertAlmostEqual(57.66, coupon_calculations.calculate_price(78, 10, .20), places=2)


if __name__ == '__main__':
    unittest.main()


