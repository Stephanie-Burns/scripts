
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import decimal


@dataclass
class Bill:
    name: str
    due_day: int
    cost: decimal

    def __str__(self) -> str:
        """
        Returns a string representation of the bill, showing its name, due date, and cost.
        """
        return f"{self.name.title():<15} | Due by: {self.due_day:<2} | Amount owed: {self.cost:<5}"


class Budget:
    """
    A class for managing a budget, including bills and payments.

    :param bills: list[Bill]
        A list of bills to be managed by the Budget instance.

    """

    def __init__(self, bills: list[Bill]):
        """
        Initializes a new Budget object with the provided list of bills.

        :param bills: list[Bill]
            A list of Bill objects to be managed by the Budget instance.
        """
        self.today = datetime.today().day
        self.bills = bills

    @staticmethod
    def _print_table(bills: list[Bill], total: int) -> None:
        """
        Prints a formatted table to the console showing the provided bills and their total cost.

        :param bills: list[Bill]
            A list of Bill objects to be included in the table.

        :param total: int
            The total cost of the bills to be included in the table.

        :return: None
            The method does not return anything, but prints a table of bills to the console.
        """
        print('=' * 50)
        print(*bills, sep='\n')
        print('-' * 50)
        print(f"{total:>50.2f}")

    def _sort_bills_by(self, sort_order: str) -> list[Bill]:
        """
        Sorts the bills list according to the specified order and returns the sorted list.

        :param sort_order: str
            The order in which to sort the bills list. Must be one of:
            'NAME', 'DUE_DAY', 'COST', or None (default).

        :return: list[Bill]
            A list of Bill objects sorted according to the specified sort order.
        """

        options = {
            "NAME"      : lambda x: x.name,
            "DUE_DAY"   : lambda x: x.due_day,
            "COST"      : lambda x: x.cost,
        }

        if sort_order in options:
            return sorted(self.bills, key=options[sort_order])

        else:
            raise KeyError(
                f"{sort_order} is not a recognized key. "
                f"Available Parameters: {', '.join(options.keys())}"
            )

    def payments_due(self, threshold: Optional[int] = None, sort_order: Optional[str] = None) -> None:
        """
        Prints a table of all bills that are due after a certain day, along with the total cost of those bills.

        :param threshold: Optional[int], defaults to None
            The minimum date (as an integer number of days since the start of the month)
            for which bills should be included in the table.
            If not provided, today's date will be used.

        :param sort_order: Optional[str], defaults to None
            The order in which to sort the bills before filtering. Should be one of 'NAME', 'DUE_DATE', 'COST'.
            If not provided, bills will not be sorted.

        :return: None
            The method does not return anything, but prints a table of bills to the console.
        """
        _today = threshold or self.today
        _bills = self.bills if not sort_order else self._sort_bills_by(sort_order)

        out = [b for b in _bills if b.due_day >= _today]
        total = sum(b.cost for b in out)

        self._print_table(out, total)

    def payments_all(self, sort_order: Optional[str] = None) -> None:
        """
        Prints a table of all the bills in the bills list with their
        corresponding cost, sorted by the specified sort_order if provided.

        :param sort_order : Optional[str], defaults to None
            The order in which to sort the bills list. Must be one of:
            'NAME', 'DUE_DAY', 'COST', or None (default).
            If not provided, bills will not be sorted.

        :return: None
            The method does not return anything, but prints a table of bills to the console.
        """

        _bills = self.bills if not sort_order else self._sort_bills_by(sort_order)
        total = sum(b.cost for b in _bills)

        self._print_table(_bills, total)


if __name__ == '__main__':

    from bills import BILLS

    t: list[Bill] = Budget(BILLS)

    t.payments_all("DUE_DAY")
    t.payments_due(threshold=15, sort_order="DUE_DAY")
