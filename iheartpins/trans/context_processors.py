# from .tradeoffer import TCart
from .models import Listing


# def tcart(request):
#     return {'tcart': TCart(request)}


def listing(request):
    return {'listings': Listing(request)}