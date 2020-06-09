import unittest
import store
from store import coupon_calculations
from coupon_calculations import calculate_price
from coupon_calculations import shipping
from coupon_calculations import tax

class MyTestCase(unittest.TestCase):
    def test_price_under_ten_1(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 5:
                if coupon_calculations.discount == .10:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))

    def test_price_under_ten_2(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 5:
                if store.coupon_calculations.discount == .15:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))
    def test_price_under_ten_3(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 5:
                if coupon_calculations.discount == .20:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))
    def test_price_under_ten_4(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 10:
                if coupon_calculations.discount == .10:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))
    def test_price_under_ten_5(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 10:
                if coupon_calculations.discount == .15:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))
    def test_price_under_ten_6(self):
        if coupon_calculations.price < 10:
            if coupon_calculations.cash_coupon == 10:
                if coupon_calculations.discount == .20:
                    self.assertEqual(True, ((calculate_price + shipping)(tax)))


if __name__ == '__main__':
    unittest.main()

#((price-cash coupon)(.1(100-percent coupon)))
