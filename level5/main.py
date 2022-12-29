import json
from level4.main import Solution4
from level3.main import Solution2, Solution3


class Solution5(Solution4):

    def __init__(self):
        """
        extend base class init method and add new options
        we can skip file exception if not found because it's already implemented
        on base class Solution1
        """
        super().__init__()
        with open(self.input_file) as input_file:
            data = json.load(input_file)
            self.options = data.get("options")

    @staticmethod
    def calculate_option_cost(option):
        if option == "gps":
            return 500
        elif option == "baby_seat":
            return 200
        elif option == "additional_insurance":
            return 1000

    def get_rental_details(self, rental, rental_days):
        """
            adapt rentals dict to match desired output
        """

        drivy_option_fees = 0
        # inherit get_rental_details from grandparent class to reconstruct the actions list
        rental_dict = super(Solution4, self).get_rental_details(rental, rental_days)

        rental_options = [option.get("type") for option in self.options if option.get("rental_id") == rental.get("id")]
        options_cost = sum(self.calculate_option_cost(option) for option in rental_options) * rental_days

        if "additional_insurance" in rental_options:
            drivy_option_fees = rental_days * 1000
            commissions = rental_dict.get("commission")
            commissions.update({"drivy_fee": commissions.get("drivy_fee") + drivy_option_fees})
        actions = [
            self.get_expense_dict("driver", rental_dict.get("price") + options_cost, "debit"),
            self.get_expense_dict("owner", int(rental_dict.get("price") * 0.7 + options_cost - drivy_option_fees)),
        ]

        fees_list = [
            self.get_expense_dict(fee.split('_')[0], value)
            for (fee, value) in rental_dict.get("commission").items()
        ]
        return {
            "options": rental_options,
            "actions": [*actions, *fees_list]
        }


def main():
    Solution5().solve()


if __name__ == '__main__':
    main()
