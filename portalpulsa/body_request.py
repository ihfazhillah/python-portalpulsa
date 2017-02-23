"""body_request, class untuk data request yang akan dikirim ke server"""
from portalpulsa.exceptions import ParamsNotFound


class BodyRequestBase(object):
    """Base body_request"""

    def __init__(self, inquiry):
        self.inquiry = inquiry
