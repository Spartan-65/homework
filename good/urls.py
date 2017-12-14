from django.conf.urls import url
from good import views

urlpatterns = [
    url(r'^search/', views.login),
    url(r'^register/', views.reg),
]