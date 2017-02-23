from portalpulsa.inquiry import Inquiry
from portalpulsa.body_request import BodyRequestSaldo
from nose import tools


def test_body_request_saldo_inquiry():
    body = BodyRequestSaldo()
    tools.eq_(body.inquiry, 'S')
