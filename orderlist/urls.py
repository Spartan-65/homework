from django.conf.urls import url
from django.contrib import admin

from orderlist import views

urlpatterns = [
    #url(r'^',admin.site.urls),
	url(r'^submit/',views.submit),
	url(r'^search',views.search),
]
