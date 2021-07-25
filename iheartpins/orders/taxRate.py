import re
import requests


def get_Tax(senderAddress, receiverAddress, orderAmount, shippingAmount):
    url = "https://api.sandbox.taxjar.com/v2/taxes"
    headers = {
        'Authorization':'Token token="4dc4af03b7c685ee35bf33a85537f87b"'
    }
    data = {
    "from_country": senderAddress["country"],
    "from_zip": senderAddress["zip"],
    "from_state": senderAddress["state"],
    "to_country": receiverAddress["country"],
    "to_zip": receiverAddress["zip"],
    "to_state": receiverAddress["state"],
    "amount": orderAmount,
    "shipping": shippingAmount,
    "line_items": []
    }
    response = requests.post(url=url, data=data, headers=headers)
    if response.status_code == 200:
        response = response.json()
        return response['tax']["amount_to_collect"]
    else:
        return "Incorrect data passed"
        
# print(get_Tax(
#     {
#         "country": "US",
#         "zip": "07001",
#         "state": "NJ"
#     },
#     {
#         "country": "US",
#         "zip": "07446",
#         "state": "NJ"
#     },
#     16.50, 1.5
# ))