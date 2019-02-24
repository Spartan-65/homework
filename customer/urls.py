from django.conf.urls import url

from customer import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.login),
    url(r'^register/', views.reg),
	url(r'^reset/',views.reset),
]
