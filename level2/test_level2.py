import unittest
from level2.main import Solution2


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution2()

    def test_calculate_duration_cost(self):
        example = {
            "id": 3,
            "car_id": 1,
            "start_date": "2015-07-3",
            "end_date": "2015-07-14",
            "distance": 1000
        }
        price_per_day = 2000
        rental_days = self.solution.get_duration_days(example.get("start_date"), example.get("end_date"))
        self.assertEqual(rental_days, 12)

        self.assertEqual(self.solution.calculate_duration_cost(rental_days, price_per_day), 17800)


if __name__ == '__main__':
    unittest.main()
