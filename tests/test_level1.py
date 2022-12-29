import unittest
from level1.main import Solution1


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution1()

    def test_init_readfile(self):
        first_car_object = {"id": 1, "price_per_day": 2000, "price_per_km": 10}
        self.assertEqual(self.solution.cars[0], first_car_object)  # add assertion here

    def test_get_duration_days(self):
        start_date = "2017-12-8"
        end_date = "2017-12-12"
        self.assertEqual(self.solution.get_duration_days(start_date, end_date), 5)

    def test_calculate_rental_price(self):
        rental_example = {
            "id": 1,
            "car_id": 1,
            "start_date": "2017-12-8",
            "end_date": "2017-12-10",
            "distance": 100
        }
        self.assertEqual(self.solution.calculate_rental_price(rental_example, 3), 7000)




if __name__ == '__main__':
    unittest.main()
