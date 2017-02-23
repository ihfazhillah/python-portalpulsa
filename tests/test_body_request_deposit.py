from portalpulsa.body_request import BodyRequestDeposit
from portalpulsa.bank import Bank
from portalpulsa.exceptions import BankNotSupported

from nose import tools


def test_inquiry():
    dep = BodyRequestDeposit(Bank.BCA, 10000)
    tools.eq_(dep.inquiry, 'D')

@tools.raises(BankNotSupported)
def test_validate_bank():
    dep = BodyRequestDeposit('link', 10000)

@tools.raises(ValueError)
def test_validate_nominal_not_integer():
    dep = BodyRequestDeposit(Bank.BCA, 'ini bukan integer')
