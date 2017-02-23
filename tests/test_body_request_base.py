"""testing body requests base, yang nanti akan diturunkan ke
setiap request ke server portalpulsa.com"""

from nose import tools
from portalpulsa.body_request import BodyRequestBase
from portalpulsa.exceptions import InvalidInquiry
from portalpulsa.inquiry import Inquiry



@tools.raises(TypeError)
def test_bila_user_tidak_memasukkan_inquiry_param():
    BodyRequestBase()


def test_validate_inquiry_benar():
    body = BodyRequestBase(Inquiry.SALDO)
    tools.eq_(body.inquiry, 'S')

@tools.raises(InvalidInquiry)
def test_validate_inquiry_salah():
    body = BodyRequestBase('N')
