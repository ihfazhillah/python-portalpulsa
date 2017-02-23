"""body_request, class untuk data request yang akan dikirim ke server"""
from portalpulsa.exceptions import ParamsNotFound, InvalidInquiry
from portalpulsa.inquiry import Inquiry

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
        pass
