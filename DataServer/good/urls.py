from django.conf.urls import url

from good import views

urlpatterns = [
    url(r'^search/', views.search),
]