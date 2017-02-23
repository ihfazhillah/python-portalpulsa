"""testing body requests base, yang nanti akan diturunkan ke
setiap request ke server portalpulsa.com"""

from nose import tools
from portalpulsa.body_request import BodyRequestBase



@tools.raises(TypeError)
def test_bila_user_tidak_memasukkan_inquiry_param():
    BodyRequestBase()
