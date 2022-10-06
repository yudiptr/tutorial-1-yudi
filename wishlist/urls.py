from django.urls import path
from wishlist.views import *

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', show_wishlist_ajax, name='show_wishlist_ajax'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name="show_json"),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('json/<int:id>', show_json_id, name="show_json_id"),
    path('register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('login/', login_user, name='login'),
    path('ajax/submit/', create, name='tbl-form'),
]