from django.conf.urls import url

from . import views

urlpatterns = [

    url(r'^$', views.login_user, name='login_user'),

    url(r'^logout/', views.logout_user, name='logout_user'),

    url(r'^index/', views.index, name='index'),

    url(r'^create/', views.create_package, name='create_package'),

    url(r'^update/', views.update_package_status, name='update_package_status'),

    url(r'^track/', views.track_packages, name='track_packages'),
]