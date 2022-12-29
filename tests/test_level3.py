import unittest
from level3.main import Solution3


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.solution = Solution3()

    def test_get_rental_details(self):
        example = {
            "id": 1,
            "car_id": 1,
            "start_date": "2017-12-8",
            "end_date": "2017-12-8",
            "distance": 100
        }
        rental_details = self.solution.get_rental_details(example, 1)
        expected_output = {
            "price": 3000,
            "commission": {
                "insurance_fee": 450,
                "assistance_fee": 100,
                "drivy_fee": 350
            }
        }
        self.assertEqual(rental_details, expected_output)


if __name__ == '__main__':
    unittest.main()
