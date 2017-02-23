from portalpulsa.body_request import BodyRequestHarga
from portalpulsa.inquiry import Inquiry

from nose import tools

def test_inquiry():
    harga = BodyRequestHarga('PLN')
    tools.eq_(harga.inquiry, Inquiry.HARGA)
