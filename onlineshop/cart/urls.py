from django.conf.urls import url
from cart.views import cart_add, cart_detail, cart_remove

urlpatterns = [
    url(r'^items/$', cart_detail, name='cart_detail'),
    url(r'^add/(?P<product_id>\d+)/$', cart_add, name='cart_add'),
    url(r'^remove/(?P<product_id>\d+)/$', cart_remove, name='cart_remove'),
]
