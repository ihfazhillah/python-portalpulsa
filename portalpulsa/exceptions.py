"""Daftar custom exceptions"""


class ParamsNotFound(Exception):
    """Bila parameter yang dibutuhkan tidak diberikan"""
    pass

class InactiveAPI(Exception):
    """Bila API tidak diaktifkan"""
    pass

class NotAllowedAPI(Exception):
    """Bila API tidak terdaftar, API user yang melakukan request"""
    pass

class AuthError(Exception):
    """Raised ketika user salah key,userid atau secret"""
    pass

class InvalidInquiry(Exception):
    """Raised ketika user salah memasukkan inquiry"""
    pass

class BankNotSupported(Exception):
    """Bila bank tidak disupport oleh portalpulsa."""
    pass
