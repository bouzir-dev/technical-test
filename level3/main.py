from level2.main import Solution2


class Solution3(Solution2):

    def get_rental_details(self, rental, rental_days):
        """
            add needed infos on the rentals result dict
        """
        price_dict = super().get_rental_details(rental, rental_days)
        total_price = price_dict.get("price")
        rental_commission = int(total_price * 0.3)
        assurance_fee = int(rental_commission * 0.5)
        assistance_fee = rental_days * 100
        drivy_fee = rental_commission - assurance_fee - assistance_fee
        return {
            **price_dict,
            "commission": {
                "insurance_fee": assurance_fee,
                "assistance_fee": assistance_fee,
                "drivy_fee": drivy_fee,
            }
        }


def main():
    Solution3().solve()


if __name__ == '__main__':
    main()
