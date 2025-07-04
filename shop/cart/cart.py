from django.conf import settings
from main.models import Product


class Cart:
  def __init__(self, request):
    # სესიის ინიციალიზაცია
    self.session = request.session

    # მივიღოთ მომხმარებლის სესია (კალათა)
    cart = self.session.get(settings.CART_SESSION_ID)

    if not cart:
      cart = self.session[settings.CART_SESSION_ID] = {}
    
    self.cart = cart
  

  