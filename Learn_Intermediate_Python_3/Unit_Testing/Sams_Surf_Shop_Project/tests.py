import surfshop
import unittest

class TestCases(unittest.TestCase):
    
    def setUp(self):
        self.cart = surfshop.ShoppingCart()

    def test_add_one_surfboard_to_cart(self):
        self.assertEqual(self.cart.add_surfboards(1), 'Successfully added 1 surfboard to cart!')

    def test_add_two_surfboards_to_cart(self):
        self.assertEqual(self.cart.add_surfboards(2), 'Successfully added 2 surfboards to cart!')

    #@unittest.skip
    def test_too_many_surfboards_in_cart(self):
        self.assertRaises(surfshop.TooManyBoardsError)

    def test_local_discount(self):
        self.cart.apply_locals_discount()
        self.assertTrue(self.cart.locals_discount, True)

    def test_multiple_surfboard_cart(self):
        test_cases = [2, 3, 4]
        for board in test_cases:
            with self.subTest(board):
                self.cart = surfshop.ShoppingCart()
                self.assertEqual(self.cart.add_surfboards(board), 'Successfully added '+str(board)+' surfboards to cart!')

unittest.main()