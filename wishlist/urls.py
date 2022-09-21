from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml
from wishlist.views import show_json
from wishlist.views import show_xml_id
from wishlist.views import register
from wishlist.views import show_json_id
from wishlist.views import logout_user
from wishlist.views import login_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('json/<int:id>', show_json_id, name="show_json_id"),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
]