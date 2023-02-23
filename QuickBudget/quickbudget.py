
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
        return f"{self.name.title():<15} | Due by: {self.due_day:<2} | Amount owed: {self.cost:<5}"


class Budget:

    def __init__(self, bills: list[Bill]):
        self.today = datetime.today().day
        self.bills = bills

    @staticmethod
    def _print_table(bills: list[Bill], total: int) -> None:
        print('=' * 50)
        print(*bills, sep='\n')
        print('-' * 50)
        print(f"{total:>50.2f}")

    def _sort_bills_by(self, sort_order: str) -> list[Bill]:

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

        _today = threshold or self.today
        _bills = self.bills if not sort_order else self._sort_bills_by(sort_order)

        out = [b for b in _bills if b.due_day >= _today]
        total = sum(b.cost for b in out)

        self._print_table(out, total)

    def payments_all(self, sort_order: Optional[str] = None) -> None:

        _bills = self.bills if not sort_order else self._sort_bills_by(sort_order)
        total = sum(b.cost for b in _bills)

        self._print_table(_bills, total)


if __name__ == '__main__':

    from bills import BILLS

    t: list[Bill] = Budget(BILLS)

    t.payments_all("DUE_DAY")
    t.payments_due(threshold=15, sort_order="DUE_DAY")
