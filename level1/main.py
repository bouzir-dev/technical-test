import json
from datetime import datetime


class Solution1:
    input_file = 'data/input.json'
    output_file = 'data/output.json'

    def __init__(self):
        try:
            with open(self.input_file) as input_file:
                data = json.load(input_file)
                self.cars = data["cars"]
                self.rentals = data["rentals"]
        except FileNotFoundError:
            raise Exception('Input file could not be found.')

    @staticmethod
    def get_duration_days(start, end):
        """
            Get number of rental days

            Parameters {(start date, end date) type: string }
            ----------
            Returns duration : int
        """
        date_format = "%Y-%m-%d"
        start = datetime.strptime(start, date_format)
        end = datetime.strptime(end, date_format)
        delta = end - start
        duration = delta.days + 1
        if duration < 1:
            raise Exception('end_date must be greater or equal to start_date')
        # add one to days difference since we need number of terms not just difference
        return duration

    @staticmethod
    def calculate_duration_cost(rental_days, price_per_day):
        """
        :param rental_days: int
        :param price_per_day: int
        :return: int
        """
        return rental_days * price_per_day

    @staticmethod
    def calculate_distance_cost(distance, price_per_km):
        """
        :param distance: int
        :param price_per_km: int
        :return: int
        """

        return distance * price_per_km

    def calculate_rental_price(self, obj, rental_days):
        """
            calculate rental price for a rental object which is composed of duration cost + distance cost
            Parameters {(obj: rental object) type: dict }
            ----------
            Returns duration : int
        """
        # retrieve first matching car_id object from the cars input list
        car_object = next(
            (car for car in self.cars if car.get("id") == obj.get("car_id")),
            None
        )
        distance = obj.get("distance")

        rental_price = self.calculate_duration_cost(rental_days, car_object.get("price_per_day")) + \
            self.calculate_distance_cost(distance, car_object.get("price_per_km"))

        return rental_price

    def get_rental_details(self, rental, rental_days):
        return {"price": self.calculate_rental_price(rental, rental_days)}

    def get_rentals_result_list(self):
        """
            Populate rentals results list
            ----------
            Returns rentals_list : list of dicts
        """
        rentals_list = []
        for rental in self.rentals:
            rental_days = self.get_duration_days(rental.get("start_date"), rental.get("end_date"))
            rentals_list.append({
                "id": rental["id"],
                **self.get_rental_details(rental, rental_days)
            })

        return rentals_list

    def write_json_output(self):
        rentals_json = {"rentals": self.get_rentals_result_list()}
        with open(self.output_file, 'w') as json_file:
            json.dump(rentals_json, json_file, indent=2)

    def solve(self):
        self.write_json_output()


def main():
    obj = Solution1()
    obj.solve()


if __name__ == '__main__':
    main()
