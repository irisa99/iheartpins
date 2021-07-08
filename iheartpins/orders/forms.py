from django import forms

class CheckoutForm(forms.Form):
    buyer = forms.IntegerField()
    buyer_name = forms.IntegerField()
    email = forms.EmailField(max_length=255)
    ship_to = forms.IntegerField()
    subtotal = forms.DecimalField()
    shipping = forms.DecimalField()
    sales_tax = forms.DecimalField()
    total_paid = forms.DecimalField()
    gateway = forms.CharField(max_length=255)





    #
    # for cart_item in Cart(request):
    #     OrderItem.objects.create(
    #         order=order,
    #         listing=cart_item['listing'],
    #         quantity=cart_item['quantity'],
    #         price=cart_item['listing'].price,
    #         seller=cart_item['listing'].pinventory.owner,