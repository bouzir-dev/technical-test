from level3.main import Solution3


class Solution4(Solution3):

    @staticmethod
    def get_expense_dict(who, amount, type="credit"):
        """

        :param who: string
        :param amount: int
        :param type: string set to credit by default unless specified in the method invoking
        :return: dict
        """
        return {
            "who": who,
            "type": type,
            "amount": amount
        }

    def get_rental_details(self, rental, rental_days):
        """
            adapt rentals dict to match desired output
        """
        # retrieve old dict to extract values from it
        rental_dict = super().get_rental_details(rental, rental_days)
        actions = [
            self.get_expense_dict("driver", rental_dict.get("price"), "debit"),
            self.get_expense_dict("owner", int(rental_dict.get("price") * 0.7)),

        ]
        fees_list = [
            self.get_expense_dict(fee.split('_')[0], value)
            for (fee, value) in rental_dict.get("commission").items()
        ]

        return {"actions": [*actions, *fees_list]}


def main():
    Solution4().solve()


if __name__ == '__main__':
    main()
