from level1.main import Solution1


class Solution2(Solution1):

    def calculate_duration_cost(self, rental_days, price_per_day):
        """

        :param rental_days: int
        :param price_per_day: int
        :return: cost = int
        I'm using simple mathematical formula for minimal run-time
        by refactoring coefficient into one variable called ratio
        """
        # Minimum cost per duration assuming minimum duration = 1 day
        cost = price_per_day
        if rental_days > 10:
            """ 
            ratio = 3 * 0.9 + 6 * 0.7 (3 is number of days between 1-4, 6 number of days between 5-10)
            0.9 is the coefficient after decreasing 10%, 0.7 is the coefficient after decreasing 30%
            cost = 1*ppd(already added) + 3*0.9*ppd + 6*0.7*ppd + rest_of_days*0.5*ppd ==> we can refactor
            """
            ratio = 6.9
            cost += ((rental_days - 10) * 0.5 + ratio) * price_per_day
        elif rental_days > 4:
            # ratio = 3 * 0.9
            ratio = 2.8
            cost += ((rental_days - 3) * ratio) * price_per_day
        else:
            # rental_days <= 4, if rental_days == 1 the next statement won't add anything
            cost += (rental_days - 1) * price_per_day * 0.9
        return int(cost)


def main():
    Solution2().solve()


if __name__ == '__main__':
    main()
