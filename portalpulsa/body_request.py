"""body_request, class untuk data request yang akan dikirim ke server"""
from portalpulsa.exceptions import BankNotSupported, InvalidInquiry
from portalpulsa.inquiry import Inquiry
from portalpulsa.bank import Bank

class BodyRequestBase(object):
    """Base body_request"""

    inquiry = None

    def __init__(self, inquiry):
        if not self.inquiry:
            self.inquiry = self._validate_inquiry(inquiry)

    @classmethod
    def _validate_inquiry(cls, inquiry):
        """memvalidasi inquiry, harus sesuai yang ada di 
        class Inquiry"""
        if not inquiry in Inquiry.__dict__.values():
            raise InvalidInquiry('Inquiry salah')
        return inquiry

class BodyRequestSaldo(BodyRequestBase):
    """Body_request untuk saldo"""

    inquiry = Inquiry.SALDO

    def __init__(self, inquiry=None):
        pass

class BodyRequestDeposit(BodyRequestBase):

    inquiry = Inquiry.DEPOSIT

    def __init__(self, bank, nominal, inquiry=None):
        self.bank = self._validate_bank(bank)
        self.nominal = self._validate_nominal(nominal)

    @classmethod
    def _validate_bank(cls, bank):
        """validasi bank, harus sesuai yang ada 
        di class Bank"""

        if not bank in Bank.__dict__.values():
            raise BankNotSupported("Bank belum disupport oleh portalpulsa")
        return bank

    @classmethod
    def _validate_nominal(cls, nominal):
        """validasi nominal,
        1. integer
        2. kelipatan 1000
        3. min 10000 max 1000000000
        """
        if not isinstance(nominal, int):
            raise ValueError("harus berupa integer")
        return nominal
