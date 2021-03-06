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

@tools.raises(ValueError)
def test_validate_nominal_lebih_kecil_dari_10000():
    dep = BodyRequestDeposit(Bank.BCA, 7000)

@tools.raises(ValueError)
def test_validate_nominal_lebih_besar_dari_1000000000():
    dep = BodyRequestDeposit(Bank.BCA, 1000001000)

@tools.raises(ValueError)
def test_validate_nominal_bukan_kelipatan_seribu():
    dep = BodyRequestDeposit(Bank.BCA, 11430)

def test_nominal_sepuluhribu():
    dep = BodyRequestDeposit(Bank.BCA, 10000)
    tools.eq_(dep.nominal, 10000)

def test_nominal_satu_miliar():
    dep = BodyRequestDeposit(Bank.BCA, 1000000000)
    tools.eq_(dep.nominal, 1000000000)
