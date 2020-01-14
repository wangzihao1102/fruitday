from django.conf.urls import url

from memberapp import views

urlpatterns = [
    url(r'^detail/', views.detail_one),

]