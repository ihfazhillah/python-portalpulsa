from nose import tools
from portalpulsa.body_request import BodyRequestTrx
from portalpulsa.inquiry import Inquiry


def test_inquiry():
    trx = BodyRequestTrx(trxid=11234)
    tools.eq_(trx.inquiry, Inquiry.STATUS)
