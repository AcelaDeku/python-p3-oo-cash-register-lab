# lib/testing/cash_register_test.py

import io
import sys
import pytest
from cash_register import CashRegister

class TestCashRegister:
    def setup_method(self):
        self.cash_register_with_discount = CashRegister(20)  # 20% discount
        self.cash_register_without_discount = CashRegister()

    def test_apply_discount_success_message(self):
        '''prints success message with updated total'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == "After the discount, the total comes to $800.00.\n"

    # other test methods...

# Run the tests with pytest
if __name__ == "__main__":
    pytest.main()
