from django.conf.urls import url
from second_app import views

urlpatterns = [
    url(r'^users',views.users,name='users'),
    url(r'^$',views.index,name='index'),
]

